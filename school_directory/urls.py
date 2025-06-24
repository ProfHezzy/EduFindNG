# your_project_name/urls.py (e.g., Qisa-Project-01/Qisa-Project-01/urls.py)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# No direct import of home_view here.
# The homepage will be included via core.urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1. Main site-wide URLs (homepage, about, contact, etc.) handled by the 'core' app.
    #    It's usually best to include the core app's URLs at the root path directly.
    path('', include('core.urls')),

    # 2. Accounts app URLs, correctly under /accounts/
    path('accounts/', include('accounts.urls')),

    # 3. Other app URLs, each under their respective prefixes
    path('schools/', include('schools.urls')),
    path('reviews/', include('reviews.urls')),
    path('favorites/', include('favorites.urls')),
    path('notifications/', include('notifications.urls')),
    path('search/', include('search.urls')),
    path('adminpanel/', include('adminpanel.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # If you have media too