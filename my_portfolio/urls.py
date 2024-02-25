from django.contrib import admin
from django.urls import path, include
from my_portfolio.views import about
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',about, name = 'about'),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('projects/', include('projects.urls')),
    path('review/', include('review.urls')),
    path('skill/', include('skill.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)



 