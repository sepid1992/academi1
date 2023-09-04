
from django.contrib import admin
from django.urls import path
from project.views import*
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',project),
    path('contact/',contact),
    path('show/',shop),
    path('about/',about),
    path('instructor/',instructor),
    path('courses/',courses),
    path('gallery/',gallery)
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


