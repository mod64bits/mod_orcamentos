from django.contrib import admin
from django.urls import path


admin.site.site_header = 'MOD64BITS'
admin.site.site_title = 'MOD64BITS ADMIN'
admin.site.index_title = 'Administração mod64bits'

urlpatterns = [
    path('admin/', admin.site.urls),
]

