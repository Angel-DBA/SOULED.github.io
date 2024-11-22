from django.contrib import admin
from .models import Product
from .models import Form
from .models import User
from .models import Cart
from .models import CartItem

admin.site.register(Product)
admin.site.register(Form)
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(CartItem)


# Register your models here.
