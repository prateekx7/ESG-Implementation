import pandas as pd

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CSVUploadSerializer
from .models import DataSource, RawRecord

from organizations.models import Organization
from emissions.models import EmissionRecord

from .utils import (
    normalize_unit,
    calculate_emissions,
    is_suspicious
)


class UploadCSVView(APIView):

    def post(self, request):

        serializer = CSVUploadSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        organization = Organization.objects.get(
            id=serializer.validated_data["organization_id"]
        )

        source_type = serializer.validated_data["source_type"]

        file = serializer.validated_data["file"]

        data_source = DataSource.objects.create(
            organization=organization,
            source_type=source_type,
            original_filename=file.name,
            uploaded_by="analyst@breatheesg.com"
        )

        df = pd.read_csv(file)

        processed = 0
        suspicious_count = 0
        failed = 0

        for _, row in df.iterrows():

            try:

                raw_record = RawRecord.objects.create(
                    data_source=data_source,
                    raw_data=row.to_dict(),
                    status="pending"
                )

                category = str(
                    row.get("category", "")
                ).lower()

                value = float(
                    row.get("activity_value", 0)
                )

                unit = row.get("unit", "")

                normalized_unit, normalized_value = (
                    normalize_unit(value, unit)
                )

                emissions = calculate_emissions(
                    category,
                    normalized_value
                )

                suspicious = is_suspicious(
                    normalized_value
                )

                if suspicious:
                    suspicious_count += 1
                    raw_record.status = "suspicious"
                else:
                    raw_record.status = "processed"

                raw_record.save()

                EmissionRecord.objects.create(
                    organization=organization,
                    data_source=data_source,
                    scope=row.get("scope", "scope_1"),
                    category=category,
                    activity_value=normalized_value,
                    original_unit=unit,
                    normalized_unit=normalized_unit,
                    co2e_emissions=emissions,
                    suspicious=suspicious
                )

                processed += 1

            except Exception as e:

                failed += 1

                RawRecord.objects.create(
                    data_source=data_source,
                    raw_data=row.to_dict(),
                    status="failed",
                    error_message=str(e)
                )

        return Response({
            "message": "Upload processed",
            "processed": processed,
            "suspicious": suspicious_count,
            "failed": failed
        })