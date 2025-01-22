from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import (
    CableDocument,
    SiteDocument,
    LocationDocument,
    DeviceDocument,
    DeviceTypeDocument,
    CircuitDocument,
)
# from dcim.api.nested_serializers import (
#     NestedCableSerializer,
#     NestedSiteSerializer,
#     NestedLocationSerializer,
#     NestedDeviceSerializer,
#     NestedDeviceTypeSerializer,
# )
# from circuits.api.nested_serializers import NestedCircuitSerializer
from dcim.api.serializers import SiteSerializer, LocationSerializer, DeviceSerializer, DeviceTypeSerializer, CableSerializer
from circuits.api.serializers import CircuitSerializer, ProviderSerializer
from .fields import UploadableBase64FileField


# Cable Document Serializer
class CableDocumentSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_documents-api:cabledocument-detail"
    )

    cable = CableSerializer(nested=True)
    document = UploadableBase64FileField(required=False)

    class Meta:
        model = CableDocument
        fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
            "cable",
            "comments",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )
        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
            "cable",
            "comments",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )


class NestedCableDocumentSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_documents-api:cabledocument-detail"
    )

    class Meta:
        model = CableDocument
        fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
        )
        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
        )


# Site Document Serializer
class SiteDocumentSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_documents-api:sitedocument-detail"
    )

    site = SiteSerializer(nested=True)
    document = UploadableBase64FileField(required=False)

    class Meta:
        model = SiteDocument
        fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
            "site",
            "comments",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )
        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
            "site",
            "comments",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )


class NestedSiteDocumentSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_documents-api:sitedocument-detail"
    )

    class Meta:
        model = SiteDocument
        fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
        )
        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
        )


# Location Document Serializer
class LocationDocumentSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_documents-api:locationdocument-detail"
    )

    location = LocationSerializer(nested=True)
    site = SiteSerializer(nested=True)
    document = UploadableBase64FileField(required=False)

    class Meta:
        model = LocationDocument
        fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
            "site",
            "location",
            "comments",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )
        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
            "site",
            "location",
            "comments",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )


class NestedLocationDocumentSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_documents-api:locationdocument-detail"
    )

    class Meta:
        model = LocationDocument
        fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
        )
        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
        )


# Device Document Serializer
class DeviceDocumentSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_documents-api:devicedocument-detail"
    )

    device_type = DeviceTypeSerializer(nested=True)
    document = UploadableBase64FileField(required=False)

    class Meta:
        model = DeviceDocument
        fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
            "device",
            "comments",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )
        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
            "device",
            "comments",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )


class NestedDeviceDocumentSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_documents-api:devicedocument-detail"
    )

    class Meta:
        model = DeviceDocument
        fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
        )
        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
        )


class DeviceTypeDocumentSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_documents-api:devicetypedocument-detail"
    )

    device_type = DeviceTypeSerializer(nested=True)
    document = UploadableBase64FileField(required=False)

    class Meta:
        model = DeviceTypeDocument
        fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
            "device_type",
            "comments",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )
        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
            "device_type",
            "comments",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )


# Circuit Document Serializer
class CircuitDocumentSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_documents-api:circuitdocument-detail"
    )

    circuit = CircuitSerializer(nested=True)
    document = UploadableBase64FileField(required=False)

    class Meta:
        model = CircuitDocument
        fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
            "circuit",
            "comments",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )
        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
            "circuit",
            "comments",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )


class NestedCircuitDocumentSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_documents-api:circuitdocument-detail"
    )

    class Meta:
        model = CircuitDocument
        fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
        )
        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "document",
            "external_url",
            "document_type",
            "filename",
        )
