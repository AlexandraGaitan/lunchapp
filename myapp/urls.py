from django.conf.urls import include, url
from django.contrib import  admin
from rest_framework import routers
from restaurant import views
	


# router = routers.DefaultRouter()
# router.register(r'api/menus', views.MenuViewSet)
# router.register(r'api/orders', views.OrderViewSet)

urlpatterns = [
	url(r'^api/menus', views.MenuViewSet),
    url(r'^api/orders/', views.OrderViewSet),
    url(r'^admin/', admin.site.urls),
    url(r'^restaurant/', include('restaurant.urls', namespace='restaurant')), 
	
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))    
]
