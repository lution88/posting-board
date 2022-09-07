from django.urls import path

from .views import PostsAPI, PostAPI

urlpatterns = [
    path("posting/", PostsAPI.as_view()),
    path("posting/<int:posting_id>/", PostAPI.as_view()),
]
