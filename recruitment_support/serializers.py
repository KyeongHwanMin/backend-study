from rest_framework import serializers
from recruitment_support.models import Support


class RecruitmentSupportSerializer(serializers.ModelSerializer):


    class Meta:
        model = Support
        fields = [
            'company',
            'recruitment_potion',
            'recruitment_compensation',
            'recruitment_content',
            'skill',
        ]