# Generated by Django 5.1 on 2024-09-01 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_delete_categoria'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
