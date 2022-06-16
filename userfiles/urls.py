from django.urls import path,include
# from rest_framework import routers
from rest_framework.routers import DefaultRouter
from . import views
from .views import UploadViewSet

# files = UploadViewSet.as_view({'get': 'list'})
# upload = UploadViewSet.as_view({'post': 'create'})
#or the simpler method, auto router

router = DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")
router.register(r'upload', UploadViewSet, basename="retrieve")

urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('download/<int:id>', views.download_file),
    #path('view/', views.viewfiles),
]

#activation link demo:
#http://127.0.0.1:8000/#/activate/MTE/b71ute-e00c6d5571024948a4f48badc9cf6410