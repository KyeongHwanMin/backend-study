from company.models import Company
from .models import Recruitment_Notice
from rest_framework import serializers
from company.serializers import CompanySerializer


class RecruitmentNoticeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.company_name', read_only=True)
    nation = serializers.CharField(source='company.nation', read_only=True)
    area = serializers.CharField(source='company.area', read_only=True)

    class Meta:
        model = Recruitment_Notice
        fields = [
            'id',  # 또는 'recruitment_notice_id': serializers.IntegerField(source='id', read_only=True)
            'company_name',
            'nation',
            'area',
            'company',  # POST를 위해 필요
            'recruitment_potion',
            'recruitment_compensation',
            'recruitment_content',
            'skill',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('company', None)  # GET 응답에서 company ID 필드를 제거
        return representation


# class RecruitmentNoticeSerializer(serializers.ModelSerializer):
#     company = CompanySerializer()
#
#     def create(self, validated_data):
#
#         company_data = validated_data.pop('company')
#         company_instance = Company.objects.get(**company_data)
#         recruitment_notice = Recruitment_Notice.objects.created(company=company_instance, **validated_data)
#
#         return recruitment_notice
#
#     class Meta:
#         model = Recruitment_Notice
#         fields = [
#             'company',
#             'recruitment_potion',
#             'recruitment_compensation',
#             'recruitment_content',
#             'skill',
#         ]

# class RecruitmentNoticeSerializer(serializers.Serializer):
#     company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())  # 이 부분 변경
#     recruitment_potion = serializers.CharField(max_length=128)
#     recruitment_compensation = serializers.IntegerField()
#     recruitment_content = serializers.CharField()
#     skill = serializers.CharField(max_length=128)
#
#     def create(self, validated_data):
#
#         recruitment_notice = Recruitment_Notice.objects.create(**validated_data)
#         return recruitment_notice
#
#     def update(self, instance, validated_data):
#         instance.company = validated_data.get('company', instance.company)
#         instance.recruitment_potion = validated_data.get('recruitment_potion', instance.recruitment_potion)
#         instance.recruitment_compensation = validated_data.get('recruitment_compensation', instance.recruitment_compensation)
#         instance.recruitment_content = validated_data.get('recruitment_content', instance.recruitment_content)
#         instance.skill = validated_data.get('skill', instance.skill)
#         instance.save()
#         return instance

