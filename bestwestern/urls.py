"""bestwestern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import HomeView, ContactFormView, ServicesView, RoomsView, ReservationPoliciesView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('contacto/', ContactFormView.as_view(), name='contact_form'),
    path('servicios/', ServicesView.as_view(), name='servicios'),
    path('rooms/', RoomsView.as_view(), name='rooms'),
    path('politicas-reservacion/', ReservationPoliciesView.as_view(), name='reservation_policies'),

]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)