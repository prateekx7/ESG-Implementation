from django.db import models
from emissions.models import EmissionRecord


class AuditLog(models.Model):

    ACTION_CHOICES = [
        ("created", "Created"),
        ("updated", "Updated"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    emission_record = models.ForeignKey(
        EmissionRecord,
        on_delete=models.CASCADE,
        related_name="audit_logs"
    )

    action = models.CharField(
        max_length=50,
        choices=ACTION_CHOICES
    )

    old_data = models.JSONField(
        null=True,
        blank=True
    )

    new_data = models.JSONField(
        null=True,
        blank=True
    )

    changed_by = models.CharField(max_length=255)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} - {self.emission_record.id}"