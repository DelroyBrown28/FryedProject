from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from basic_core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('staff/', include('staff.urls', namespace='staff')),
    path('cart/', include('cart.urls', namespace='cart')),
]

# Connects to static files if DEBUG mode is true
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
