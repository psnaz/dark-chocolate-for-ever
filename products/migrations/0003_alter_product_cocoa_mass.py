# Generated by Django 3.2 on 2023-01-27 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230127_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cocoa_mass',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]