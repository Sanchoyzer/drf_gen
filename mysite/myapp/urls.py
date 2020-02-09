from django.conf.urls import include, url
from myapp import views


urlpatterns = [

  url(r'^question/(?P<id>[0-9]+)/$', views.QuestionAPIView.as_view()),
  url(r'^question/$', views.QuestionAPIListView.as_view()),

  url(r'^choice/(?P<id>[0-9]+)/$', views.ChoiceAPIView.as_view()),
  url(r'^choice/$', views.ChoiceAPIListView.as_view()),

]
