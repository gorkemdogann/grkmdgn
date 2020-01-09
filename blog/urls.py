from django.urls import path
from .views import BlogPageView, BlogDetailView

urlpatterns = [

    path('', BlogPageView.as_view(), name="index"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name="post"),


]
