from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static

from . import views
from app import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('app.urls')),
    path('accounts/', include('accounts.urls')),
    path('', article_views.article_list, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
