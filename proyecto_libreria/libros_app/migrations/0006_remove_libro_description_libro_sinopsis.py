# Generated by Django 4.2.6 on 2023-10-29 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros_app', '0005_libro_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='description',
        ),
        migrations.AddField(
            model_name='libro',
            name='sinopsis',
            field=models.TextField(blank=True, verbose_name='sinopsis'),
        ),
    ]