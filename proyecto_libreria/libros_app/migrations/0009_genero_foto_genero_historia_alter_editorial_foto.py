# Generated by Django 4.2.6 on 2023-11-01 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros_app', '0008_editorial_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='genero',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='generos', verbose_name='Género'),
        ),
        migrations.AddField(
            model_name='genero',
            name='historia',
            field=models.TextField(default='', verbose_name='Historia'),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='editoriales', verbose_name='Editorial'),
        ),
    ]
