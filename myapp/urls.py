from django.conf import settings
from django.urls import path
from . import views  
from django.conf.urls.static import static

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('',views.index,name='Index'),    
    path('newsletter/signup/', views.newsletter_signup, name='newsletter_signup'),
    path('newsletter/success/', views.newsletter_success, name='newsletter_success'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)