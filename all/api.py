from rest_framework import routers, serializers, viewsets
from all.models import UploadModel

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UploadModel
        fields = ('name')


class FileViewSet(viewsets.ModelViewSet):
    all_files = UploadModel.objects.all()
    serializer_class = FileSerializer


router = routers.DefaultRouter()
router.register('api/files', FileViewSet)