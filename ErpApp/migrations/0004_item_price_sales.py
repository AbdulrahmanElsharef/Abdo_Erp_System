# Generated by Django 4.2 on 2023-05-10 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ErpApp', '0003_alter_category_image_alter_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price_sales',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]