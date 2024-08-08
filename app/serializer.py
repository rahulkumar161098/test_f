
from app.models import Product
from rest_framework import serializers

# code reusability
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        # fields=['name', 'price']    # specific fields
        fields='__all__'     # all fields