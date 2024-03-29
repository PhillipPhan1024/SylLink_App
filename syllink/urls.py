from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

app_name = "syllink"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('upload/', views.upload_file, name='upload'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)