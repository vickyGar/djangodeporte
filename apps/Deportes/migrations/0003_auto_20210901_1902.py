# Generated by Django 2.0.6 on 2021-09-02 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Deportes', '0002_auto_20210825_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='garment',
            old_name='name',
            new_name='client',
        ),
        migrations.RemoveField(
            model_name='garment',
            name='shop',
        ),
    ]