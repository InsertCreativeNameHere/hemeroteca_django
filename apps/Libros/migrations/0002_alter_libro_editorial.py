# Generated by Django 4.2.5 on 2023-10-02 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='editorial',
            field=models.CharField(max_length=49),
        ),
    ]
