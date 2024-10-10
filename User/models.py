from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
# Create your models here.

class Customer(AbstractUser):
    phone = models.CharField(max_length=15)
    shipping_address = models.TextField(null=True, blank=True)
    billing_address = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_picture/', default='profile_picture/default.jpg')
    date_of_birth = models.DateField()


    # Override group and user_permissions to avoid conflicts
    groups = models.ManyToManyField(
        Group, 
        related_name='customer_set', # Provide unique name for related_name
        blank=True, 
        help_text="The groups this user belongs to.", 
        verbose_name="groups"
    )

    user_permissions = models.ManyToManyField(
        Permission, 
        related_name='customer_set', 
        blank=True,
        help_text="Specific permissions for this user.", 
        verbose_name="user permissions"
    )

    def __str__(self):
        return f'{self.username}'
    
    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'