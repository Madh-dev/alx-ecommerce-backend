from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, Group, Permission


# ======================
# 🟩 CUSTOM USER MODEL
# ======================
class User(AbstractUser):
    # Extend with extra fields if needed (e.g., phone, is_seller)
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # avoid clash with default
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # avoid clash
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username


# ======================
# 🟩 CATEGORY MODEL
# ======================
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# ======================
# 🟩 PRODUCT MODEL
# ======================
def product_image_upload_path(instance, filename):
    return f"products/{instance.slug}/{filename}"


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,  # keep products if category deleted
        null=True,
        related_name="products",
        db_index=True
    )
    image = models.ImageField(upload_to=product_image_upload_path, null=True, blank=True)

    inventory = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)  # soft delete

    created_at = models.DateTimeField(auto_now_add=True,db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=["price"]),
            models.Index(fields=["category"]),
            models.Index(fields=["-created_at"]),
        ]

    @property
    def stock_status(self):
        return "In Stock" if self.inventory > 0 else "Out of Stock"

    def __str__(self):
        return self.title


# ======================
# 🟦 AUTO GENERATE SLUGS
# ======================
@receiver(pre_save, sender=Product)
def generate_product_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


@receiver(pre_save, sender=Category)
def generate_category_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
