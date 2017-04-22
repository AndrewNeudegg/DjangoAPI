from django.contrib import admin  # Import Admin, not strictly required here, present for debugging.
from django.conf.urls import url, include  # Included for automated routing.
from rest_framework import routers, permissions  # For automated routing.
from rest import views  # Import all of the defined views.
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500  # Sort out these views

router = routers.DefaultRouter()  # Create the defualt router and add paths.
### Features full case insensitivity, from random, Random, RaNdOm, cause people be people.
router.register(r'^(?i)random', views.RandomBlockViewSet)
router.register(r'^(?i)sensordata', views.SensorDataBlockViewSet)
router.register(r'^(?i)partner', views.PartnerBlockBlockViewSet)
router.register(r'^(?i)update', views.UpdateBlockBlockViewSet)

### The following router.register(values) permit the login auth-api.
### Reference: http://www.django-rest-framework.org/tutorial/quickstart/#urls
router.register(r'^(?i)users', views.UserViewSet)
router.register(r'^(?i)groups', views.GroupViewSet)

### The following lean heavily upon the work of the above page, but are required
### make the OAuth token generator function.
### (The standard Django login functions are re-routed through these methods.)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^(?i)admin/', admin.site.urls),  # Front end admin.
    url(r'^(?i)api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Back-end admin
    url(r'^(?i)o/', include('oauth2_provider.urls', namespace='oauth2_provider')),  # OAuth Admin
]

handler404 = views.error404
handler500 = views.error500
