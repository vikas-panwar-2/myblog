# Generated by Django 3.2.3 on 2021-05-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_post_id_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
