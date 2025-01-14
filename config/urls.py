from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from apps.blog.feeds import LatestPostsFeed

from config import settings

handler403 = 'apps.blog.views.tr_handler403'
handler404 = 'apps.blog.views.tr_handler404'
handler500 = 'apps.blog.views.tr_handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feeds/latest/', LatestPostsFeed(), name='latest_post_feed'),
    path('', include('apps.blog.urls')),
    path('', include('apps.accounts.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]