from django.db import models
from django.db.models import JSONField
from users.models import User

REPORT_STATUS = (
    ("pending", "Pending"),
    ("finished", "Finished"),
    ("error", "Error"),
)


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    creation_date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to="reports")
    status = models.CharField(max_length=20, choices=REPORT_STATUS, default="pending")
    parameters = JSONField()

    def __str__(self):
        return self.name
