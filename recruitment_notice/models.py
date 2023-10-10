from django.db import models

class Recruitment_Notice(models.Model):
    company = models.ForeignKey(to="company.Company", on_delete=models.CASCADE,
                                related_name="recruitment_notices", help_text="회사 ID")
    recruitment_potion = models.CharField(max_length=128, help_text="채용 포지션")
    recruitment_compensation = models.IntegerField(help_text="채용 보상금")
    recruitment_content = models.TextField(blank=True)
    skill = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, help_text="생성 날짜")
    modified_at = models.DateTimeField(auto_now=True, help_text="수정 날짜")

    class Meta:
        db_table = "recruitment_notice"
