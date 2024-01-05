from netbox.api.routers import NetBoxRouter
from . import views

app_name = "netbox_documents"

router = NetBoxRouter()
router.register("cable-documents", views.CableDocumentViewSet)
router.register("site-documents", views.SiteDocumentViewSet)
router.register("location-documents", views.LocationDocumentViewSet)
router.register("device-documents", views.DeviceDocumentViewSet)
router.register("device-type-documents", views.DeviceTypeDocumentViewSet)
router.register("circuit-documents", views.CircuitDocumentViewSet)

urlpatterns = router.urls
