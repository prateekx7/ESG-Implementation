from .models import AuditLog


def create_audit_log(
    emission_record,
    action,
    old_data,
    new_data,
    changed_by
):

    AuditLog.objects.create(
        emission_record=emission_record,
        action=action,
        old_data=old_data,
        new_data=new_data,
        changed_by=changed_by
    )