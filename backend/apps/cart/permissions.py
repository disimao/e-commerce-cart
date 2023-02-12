from rest_framework.permissions import BasePermission

from apps.cart.models import CartItem


class IsCartOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user


class IsCartItemOwner(BasePermission):
    def has_permission(self, request, view):
        is_owner = CartItem.objects.filter(
            cart__customer=request.user,
            **request.parser_context.get("kwargs", {})
        ).exists()
        return is_owner

    def has_object_permission(self, request, view, obj):
        print(obj, request)
        return obj.cart.customer == request.user
