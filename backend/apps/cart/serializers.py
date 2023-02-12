from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    UUIDField,
)

from apps.cart.models import Cart, CartItem
from apps.product.models import Product
from apps.product.serializers import ProductSerializer


class ReadOnlyCartItemSerializer(ModelSerializer):
    product = ProductSerializer(many=False)
    sub_total = SerializerMethodField(method_name="total")

    class Meta:
        model = CartItem
        fields = ["id", "cart", "product", "quantity", "sub_total"]

    def total(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.price


class CartItemSerializer(ModelSerializer):
    product_id = UUIDField()

    class Meta:
        model = CartItem
        fields = ["id", "product_id", "quantity"]

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise ValidationError(
                "There is no product associated with the given ID"
            )

        return value


class CartSerializer(ModelSerializer):
    id = UUIDField(read_only=True)
    items = ReadOnlyCartItemSerializer(many=True, read_only=True)
    total = SerializerMethodField(method_name="total")

    class Meta:
        model = Cart
        fields = "__all__"

    def total(self, cart: Cart):
        items = cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total

    def validate_customer(self, obj):
        request = self.context.get("request")
        if obj != request.user:
            raise ValidationError("Customer id doesn't exist")
        return obj
