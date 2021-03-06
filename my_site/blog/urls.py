from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="front-page"),
    path("posts", views.all_posts, name="all-posts"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
]
