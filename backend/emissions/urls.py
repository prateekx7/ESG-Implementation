from django.urls import path

from .views import (
    PendingRecordsView,
    ApproveRecordView,
    RejectRecordView,
    DashboardSummaryView
)

urlpatterns = [
    path(
        "pending/",
        PendingRecordsView.as_view()
    ),

    path(
        "approve/<int:record_id>/",
        ApproveRecordView.as_view()
    ),

    path(
        "reject/<int:record_id>/",
        RejectRecordView.as_view()
    ),

    path(
        "dashboard-summary/",
        DashboardSummaryView.as_view()
    ),
]