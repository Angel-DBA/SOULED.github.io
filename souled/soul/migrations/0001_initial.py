# Generated by Django 5.1.3 on 2024-11-22 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Form",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("stock", models.IntegerField(default=0)),
                ("image", models.ImageField(upload_to="product_images/")),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=100, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(default=1)),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="soul.cart",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="soul.product"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cart",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="soul.user"
            ),
        ),
    ]
