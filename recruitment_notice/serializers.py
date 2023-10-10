from rest_framework.serializers import ModelSerializer
from recruitment_notice.models import Recruitment_Notice


class RecruitmentNoticeSerializer(ModelSerializer):
    class Meta:
        model = Recruitment_Notice
        fields = [
            'company',
            'recruitment_potion',
            'recruitment_compensation',
            'recruitment_content',
            'skill',

        ]
