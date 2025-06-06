from rest_framework import serializers
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=None)

    class Meta:
        model = CartItem
        fields = [ 'id','product_name', 'product_price', 'product_quantity']