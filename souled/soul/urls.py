from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views





urlpatterns = [
    path('products/', views.products, name='products'),  
    path('user/', views.user, name='user'),
    path('', views.home, name='home'),
    path('submit-message/', views.message_view, name='submit_message'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)