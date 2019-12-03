from django.urls import path

from api.views import QuestionList, QuestionDetail

urlpatterns = [
    path('pages/', QuestionList.as_view(), name='page_list'),
    path('pages/<int:pk>', QuestionDetail.as_view(), name='page_detail')
]
