from django.urls import path
from django.urls.resolvers import URLPattern
from .views import FileUploadView

urlpatterns = [
    path('upload', FileUploadView.as_view())
]