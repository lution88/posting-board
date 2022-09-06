from django.urls import path

from .views import PostsAPI

urlpatterns = [
    path("posting/", PostsAPI.as_view()),
    path("posting/<int:posting_id>/", PostsAPI.as_view()),
]
