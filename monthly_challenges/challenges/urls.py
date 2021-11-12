from django.urls import path
from . import views

urlpatterns = [
    # order matters here! if we want to check numbers first, need
    # int first
    path("", views.index, name="home"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
