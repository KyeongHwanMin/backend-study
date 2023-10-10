from rest_framework.response import Response
from company.models import Company
from rest_framework.views import APIView
from company.serializers import CompanySerializer


class CompanyView(APIView):
    def get(self, request):
        qs = Company.objects.all()
        serializer = CompanySerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

