
from django.contrib import admin
from django.urls import path, include

# create for Media
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # creater path for project urls
    path('', include('worker.urls', namespace='workerurls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
