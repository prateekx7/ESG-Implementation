from django.db import models
from organizations.models import Organization


class DataSource(models.Model):

    SOURCE_TYPES = [
        ("sap", "SAP"),
        ("utility", "Utility"),
        ("travel", "Travel"),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=50,
        choices=SOURCE_TYPES
    )

    original_filename = models.CharField(max_length=255)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    uploaded_by = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return f"{self.organization.name} - {self.source_type}"


class RawRecord(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processed", "Processed"),
        ("failed", "Failed"),
        ("suspicious", "Suspicious"),
    ]

    data_source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE,
        related_name="raw_records"
    )

    raw_data = models.JSONField()

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="pending"
    )

    error_message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"RawRecord {self.id}"