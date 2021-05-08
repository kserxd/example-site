from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('login/', include('login.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
