from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from recruitment_support.models import Support
from recruitment_support.serializers import RecruitmentSupportSerializer


class RecruitementSupportView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        qs = Support.objects.filter(user=request.user)
        serializer = RecruitmentSupportSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data["user"] = request.user.id
        print(request.user)
        serializer = RecruitmentSupportSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
