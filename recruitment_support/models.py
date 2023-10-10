from django.db import models
from django.contrib.auth.models import User

class Support(models.Model):
    user = models.OneToOneField(to="auth.User", on_delete=models.CASCADE)
    recruitment_notice = models.ForeignKey(to="recruitment_notice.Recruitment_Notice", null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "support"
