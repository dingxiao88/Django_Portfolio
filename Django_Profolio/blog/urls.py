

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_page),
    path('<int:blog_id>/', views.blog_text),
]
	