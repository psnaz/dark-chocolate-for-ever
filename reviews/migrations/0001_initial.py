# Generated by Django 3.2 on 2023-03-13 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0004_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('submitted', models.DateTimeField(auto_now=True)),
                ('message', models.CharField(max_length=1000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]