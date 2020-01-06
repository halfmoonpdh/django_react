from django.urls import path
from .views import *

app_name = "app"

urlpatterns = [
    path('demo_user/', IndexView.as_view()),
    path('poster/', PosterView.as_view())
]
