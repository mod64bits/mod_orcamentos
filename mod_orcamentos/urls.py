from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'MOD64BITS'
admin.site.site_title = 'MOD64BITS ADMIN'
admin.site.index_title = 'Administração mod64bits'

from apps.base.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', HomePageView.as_view(), name="Home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

