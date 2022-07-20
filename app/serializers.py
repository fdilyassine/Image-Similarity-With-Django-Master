from rest_framework.serializers import ModelSerializer
from app.models import Vector

class VectorSerializer(ModelSerializer):
    class Meta:
        model = Vector
        fields = '__all__'