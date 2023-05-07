from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from adminpanel.views import HomeView
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('purchase/', include('payment.urls')),
    path('cars/', include('car.urls')),
    path('admin-panel/', include('adminpanel.urls')),
    path('', HomeView.as_view(), name='home')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
