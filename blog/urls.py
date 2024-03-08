from django.urls import path

from blog import views

app_name='blog'
urlpatterns = [
    path("", views.index, name='home'),
    path("post/<slug>/", views.post_detail, name='blog-post-detail'),
]