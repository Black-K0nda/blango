"""blango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.static import serve
from django.urls import path
import blog.views
import os
import debug_toolbar
from django.conf import settings
import blango_auth.views
from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm


urlpatterns = [
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/", include('allauth.urls')),
    path("accounts/profile/", blango_auth.views.profile, name='profile'),
    path('', include('blog.urls', 'blog')),
    path("post/<slug>/", blog.views.post_detail, name='blog-post-detail'),
    path('admin/', admin.site.urls),  # Keep
    path("ip/", blog.views.get_ip),
    path(
        "accounts/register/",
        RegistrationView.as_view(form_class=BlangoRegistrationForm),
        name="django_registration_register",
    ),
    path("accounts/", include("django_registration.backends.activation.urls")),
    path("api/v1/", include("blog.api.urls")),
    # path('accounts/', include('django.contrib.auth.urls')),  # Keep
    # url(r'^oauth/', include('social_django.urls', namespace='social')),  # Keep
]
if settings.DEBUG:
  urlpatterns += [
    path("__debug__/", include(debug_toolbar.urls)),
  ]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", blog.views.index)
# ]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
         'show_indexes': True},
        name='site_path'
        ),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
