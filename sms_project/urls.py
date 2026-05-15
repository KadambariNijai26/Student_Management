from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('accounts/', include('accounts.urls')),

    # Core (home/dashboard)
    path('', include('core.urls')),

    # Apps
    path('attendance/', include('attendance.urls')),
    path('marks/', include('marks.urls')),
    path('fees/', include('fees.urls')),
    path('students/', include('students.urls')),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)