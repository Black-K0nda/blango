from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import os
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from blog.api.views import UserDetail, TagViewSet, PostViewSet

# Create a router and register the viewsets.
router = DefaultRouter()
router.register("tags", TagViewSet)
router.register('posts', PostViewSet)
# Define the schema view.
schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version="v1",
        description="API for Blango Blog",
    ),
    url=f"https://{os.environ.get('CODIO_HOSTNAME')}-8000.codio.io/api/v1/",
    public=True,
)

# Define the urlpatterns.
urlpatterns = [
    # path("posts/", PostList.as_view(), name="api_post_list"),
    # path("posts/<int:pk>/", PostDetail.as_view(), name="api_post_detail"),
    path("users/<str:email>/", UserDetail.as_view(), name="api_user_detail"),
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("", include(router.urls)),
]