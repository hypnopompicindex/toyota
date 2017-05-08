from django.conf.urls import url, include
from rest_framework import routers
from wheelstand.api import views
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'model', views.ModelsViewSet)
router.register(r'trim', views.TrimViewSet)
router.register(r'modelsshown', views.ModelsShownViewSet)
router.register(r'accessories', views.AccessoriesViewSet)
router.register(r'location', views.LocationViewSet)
router.register(r'colours', views.ColoursViewSet)
router.register(r'interiors', views.InteriorsViewSet)
router.register(r'dealerprovince', views.DealerProvinceViewSet)
router.register(r'dealers', views.DealersViewSet)
router.register(r'dealercity', views.DealerCityViewSet)
router.register(r'modelsshowninteriors', views.ModelsShownInteriorsViewSet)
router.register(r'modelsshowngallery', views.ModelsShownGalleryViewSet)
router.register(r'allaccessories', views.AllAccessoriesViewSet)
router.register(r'accessoriesshown', views.AccessoriesShownViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^testdrive/$', views.TestDriveList.as_view()),
    url('^allapi/$', views.AllAPIView.as_view()),
    url('^allapiimages/$', views.AllAPIImagesView.as_view()),
    url('^json/$', views.ExampleView.as_view()),

#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]