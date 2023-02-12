from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.filters import OrderingFilter

from apps.cart.serializers import (
    CartSerializer,
    CartItemSerializer,
    ReadOnlyCartItemSerializer,
)
from apps.cart.models import Cart, CartItem
from apps.cart.filters import (
    CustomerFilterBackend,
    CustomerCartItemFilterBackend,
)
from apps.cart.permissions import IsCartOwner, IsCartItemOwner


class CartViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
        IsCartOwner,
    )
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = [OrderingFilter, CustomerFilterBackend]
    ordering_fields = ["products__name", "products__price", "products__score"]
    lookup_field = "id"

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class CartItemViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
        IsCartItemOwner,
    )
    queryset = CartItem.objects.all()
    filter_backends = [CustomerCartItemFilterBackend]
    serializer_class = CartItemSerializer

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ReadOnlyCartItemSerializer

        return CartItemSerializer

    def perform_create(self, serializer):
        serializer.save(cart_id=self.kwargs["cart_id"])
