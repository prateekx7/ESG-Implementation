from django.db import models
from organizations.models import Organization
from ingestion.models import DataSource


class EmissionRecord(models.Model):

    SCOPE_CHOICES = [
        ("scope_1", "Scope 1"),
        ("scope_2", "Scope 2"),
        ("scope_3", "Scope 3"),
    ]

    REVIEW_STATUS = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    data_source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )

    scope = models.CharField(
        max_length=50,
        choices=SCOPE_CHOICES
    )

    category = models.CharField(max_length=255)

    activity_value = models.FloatField()

    original_unit = models.CharField(max_length=50)

    normalized_unit = models.CharField(max_length=50)

    co2e_emissions = models.FloatField()

    activity_date = models.DateField(null=True)

    review_status = models.CharField(
        max_length=50,
        choices=REVIEW_STATUS,
        default="pending"
    )

    approved_by = models.CharField(
        max_length=255,
        blank=True
    )

    approved_at = models.DateTimeField(
        null=True,
        blank=True
    )

    suspicious = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.co2e_emissions} kgCO2e"