from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from recruitment_notice.models import Recruitment_Notice
from recruitment_notice.serializers import RecruitmentNoticeSerializer


class RecruitmentNoticeView(APIView):
    def get(self, request):
        qs = Recruitment_Notice.objects.all()
        serializer = RecruitmentNoticeSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecruitmentNoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RecruitmentNoticeDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Recruitment_Notice, pk=pk)

    def get(self, request, pk, format=None):
        recruitment_notice = self.get_object(pk)
        serializer = RecruitmentNoticeSerializer(recruitment_notice)
        return Response(serializer.data)
