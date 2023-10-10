from django.urls import path
from recruitment_notice.views import RecruitmentNoticeView

urlpatterns = [
    path('recruitment-notice', RecruitmentNoticeView.as_view()),
]