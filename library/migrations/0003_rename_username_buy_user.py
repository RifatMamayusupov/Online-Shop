# Generated by Django 4.2.10 on 2024-02-13 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_category_self_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buy',
            old_name='username',
            new_name='user',
        ),
    ]