from django.db import models

class Support_detail(models.Model):
    user  = models.OneToOneField(to="User", on_delete=models.CASCADE)
    recruitment_notice = models.ForeignKey(to="recruitment_notice.Recruitment_Notice", null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "support_detail"
