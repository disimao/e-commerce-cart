from rest_framework.filters import BaseFilterBackend


class CustomerFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        pk = request.user.pk
        if pk:
            return queryset.filter(customer=pk)
        return queryset.none()


class CustomerCartItemFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        cart_id = request.parser_context.get("kwargs", {}).get("cart_id")
        pk = request.user.pk
        if pk:
            return queryset.filter(cart__customer=pk, cart_id=cart_id)
        return queryset.none()
