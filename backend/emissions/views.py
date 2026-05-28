from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import EmissionRecord
from .serializers import EmissionRecordSerializer

from audits.utils import create_audit_log


class PendingRecordsView(APIView):

    def get(self, request):

        records = EmissionRecord.objects.filter(
            review_status="pending"
        )

        serializer = EmissionRecordSerializer(
            records,
            many=True
        )

        return Response(serializer.data)


class ApproveRecordView(APIView):

    def post(self, request, record_id):

        try:
            record = EmissionRecord.objects.get(
                id=record_id
            )

        except EmissionRecord.DoesNotExist:
            return Response(
                {"error": "Record not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        old_data = {
            "review_status": record.review_status
        }

        record.review_status = "approved"
        record.approved_by = "analyst@breatheesg.com"
        record.approved_at = timezone.now()

        record.save()

        create_audit_log(
            emission_record=record,
            action="approved",
            old_data=old_data,
            new_data={
                "review_status": "approved"
            },
            changed_by="analyst@breatheesg.com"
        )

        return Response({
            "message": "Record approved"
        })


class RejectRecordView(APIView):

    def post(self, request, record_id):

        try:
            record = EmissionRecord.objects.get(
                id=record_id
            )

        except EmissionRecord.DoesNotExist:
            return Response(
                {"error": "Record not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        old_data = {
            "review_status": record.review_status
        }

        record.review_status = "rejected"

        record.save()

        create_audit_log(
            emission_record=record,
            action="rejected",
            old_data=old_data,
            new_data={
                "review_status": "rejected"
            },
            changed_by="analyst@breatheesg.com"
        )

        return Response({
            "message": "Record rejected"
        })

class DashboardSummaryView(APIView):

    def get(self, request):

        total = EmissionRecord.objects.count()

        pending = EmissionRecord.objects.filter(
            review_status="pending"
        ).count()

        approved = EmissionRecord.objects.filter(
            review_status="approved"
        ).count()

        suspicious = EmissionRecord.objects.filter(
            suspicious=True
        ).count()

        return Response({
            "total_records": total,
            "pending_reviews": pending,
            "approved_records": approved,
            "suspicious_records": suspicious
        })
    