from rest_framework.response import Response

from company.models import Company
from rest_framework.views import APIView
from company.serializers import CompanySerializer


class CompanyView(APIView):
    def get(self, request):
        qs = Company.objects.all()
        serializer = CompanySerializer(qs, many=True)
        return Response(serializer.data)
    pass
