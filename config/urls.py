from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('company/', include('company.urls')),
    path('recruitment-notice/', include('recruitment_notice.urls')),
    path('recruitment-support/', include('recruitment_support.urls')),
]
