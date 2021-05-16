from django.urls import path

from .views import DialyViewSet

urlpatterns = [
    path('dialy', DialyViewSet.as_view(), name="dialy")
]
