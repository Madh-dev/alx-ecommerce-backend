from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


# ======================
# 🟩 Pagination
# ======================
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"


# ======================
# 🟩 Category ViewSet
# ======================
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination

    # Filters + Search + Sorting
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filter by name or slug
    filterset_fields = ["name", "slug"]

    # Query search
    search_fields = ["name", "description"]

    # Sorting
    ordering_fields = ["name"]
    ordering = ["name"]


# ======================
# 🟩 Product ViewSet
# ======================
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True).select_related("category")
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    # Filters + Search + Sorting
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filter by category or active status
    filterset_fields = ["category", "is_active"]

    # Query search
    search_fields = ["title", "description", "category__name"]

    # Sorting
    ordering_fields = ["price", "created_at", "updated_at"]
    ordering = ["-created_at"]

    # Override destroy to implement soft delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(
            {"detail": f"Product '{instance.title}' has been deactivated (soft deleted)."},
            status=status.HTTP_200_OK,
        )
    
    # Custom action to reactivate a product
    @action(detail=True, methods=["post"])
    def reactivate(self, request, pk=None, slug=None):
        instance = self.get_object()
        if instance.is_active:
            return Response(
                {"detail": f"Product '{instance.title}' is already active."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        instance.is_active = True
        instance.save()
        return Response(
            {"detail": f"Product '{instance.title}' has been reactivated."},
            status=status.HTTP_200_OK,
        )

