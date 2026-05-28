from rest_framework import serializers


class CSVUploadSerializer(serializers.Serializer):
    organization_id = serializers.IntegerField()
    source_type = serializers.CharField()
    file = serializers.FileField()