from django.db import models

class Support(models.Model):
    user = models.OneToOneField(to="auth.User", on_delete=models.CASCADE)
    recruitment_notice = models.ForeignKey(to="recruitment_notice.RecruitmentNotice", null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "support"
