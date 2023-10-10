from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from recruitment_notice.models import RecruitmentNotice
from recruitment_notice.serializers import RecruitmentNoticeSerializer, RecruitmentNoticeDetailSerializer


class RecruitmentNoticeView(APIView):
    def get(self, request):
        qs = RecruitmentNotice.objects.all()
        serializer = RecruitmentNoticeSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = RecruitmentNoticeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecruitmentNoticeDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(RecruitmentNotice, pk=pk)

    def get(self, request, pk, format=None):
        recruitment_notice_info = self.get_object(pk)
        serializer = RecruitmentNoticeDetailSerializer(recruitment_notice_info)
        return Response(serializer.data)

    def patch(self, request, pk):
        recruitment_notice_info = self.get_object(pk)
        serializer = RecruitmentNoticeSerializer(recruitment_notice_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recruitment_notice_info = self.get_object(pk)
        recruitment_notice_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
