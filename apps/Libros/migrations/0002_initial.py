# Generated by Django 4.2.7 on 2023-11-20 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Libros', '0001_initial'),
        ('Users', '0001_initial'),
        ('Storage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Users.author'),
        ),
        migrations.AddField(
            model_name='copy',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Libros.libro'),
        ),
        migrations.AddField(
            model_name='copy',
            name='ubication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Storage.seccion'),
        ),
    ]
