from django.contrib import admin
from .models.products import Product
from .models.category import Category
from .models.customers import Customer
from .models.orders import Order
from .models.locations import Coordinate

admin.site.register(Coordinate)

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Customer)
class AdminViewCustomer(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'phone']
    list_display = ['first_name', 'last_name', 'phone', 'email']


@admin.register(Order)
class AdminViewOrder(admin.ModelAdmin):
    search_fields = ['address', 'phone', 'customer']
    list_display = ['customer', 'product', 'quantity', 'price', 'date', 'status', 'delivery']
