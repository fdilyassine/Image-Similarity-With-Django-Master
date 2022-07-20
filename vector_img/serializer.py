class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'