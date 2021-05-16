from rest_framework import fields, serializers

from .models import DialyModel


class DialySerializer(serializers.ModelSerializer):
    # TODO: baseとして継承する
    title = serializers.CharField(max_length=50)
    content = serializers.CharField(max_length=400)
    isDeleted = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = DialyModel
        fields = '__all__'
