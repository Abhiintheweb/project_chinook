from rest_framework import routers
from api.views.actor_view import ActorViewset
from api.views.customer_view import CustomerViewset
from django.urls import path
from django.conf.urls import include


router = routers.DefaultRouter()
router.register('actors', ActorViewset)
router.register('customers', CustomerViewset)

urlpatterns = [path('', include(router.urls)),]
