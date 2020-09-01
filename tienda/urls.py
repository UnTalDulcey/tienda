"""tienda URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from empresas.views import Test2View, HomeView, Details, add_product_cart_view
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path('jet/', include('jet.urls', 'jet')),
    path('', HomeView.as_view(),name='home'),
    #path('prueba', Test2View.as_view(),name='prueba'),
    path('detail/<int:pk>/', Details.as_view(),name='detalle'),
    path('add-product/', add_product_cart_view,name='add_product'),
    path('admin/', admin.site.urls),
    path('buy/<int:pk>/', Test2View.as_view(),name='compra'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL,
                       document_root=settings.MEDIA_ROOT)
