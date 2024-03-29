# Generated by Django 3.2.25 on 2024-03-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='made_with',
            field=models.CharField(default='100% natural ingredients', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(default='Product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
    ]
