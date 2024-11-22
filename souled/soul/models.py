from django.db import models




# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)  # This will automatically be an auto-incrementing integer.
    username = models.CharField(max_length=100, unique=True)  # Username should be unique.
    email = models.EmailField(unique=True)  # Email should be unique.
    password = models.CharField(max_length=255)  # Store the password securely (hashed).

    def __str__(self):
        return self.username


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/')
    
    def __str__(self):
        return self.name
      
class Form(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'Message from {self.name}'
      
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)  # Relates to the User table
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the cart was created

    def __str__(self):
        return f'Cart {self.id} for {self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)  # Quantity of the product in the cart

    def __str__(self):
        return f'{self.product.name} (x{self.quantity})'
    
    

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    






