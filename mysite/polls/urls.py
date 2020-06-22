from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail),
    path('<int:question_id>/detail/', views.detail),
    path('<int:question_id>/results/', views.results),
    path('<int:question_id>/vote/', views.vote),
]