from django.urls import path

from . import views

app_name = 'contest'

urlpatterns = [
    path('', views.proposal_create, name='create'),
    path('accepted/', views.accepted, name='accepted'),
]
