# Generated by Django 4.0.4 on 2024-10-14 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jauth", "0004_remove_accountkituser_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facebookaccesstoken",
            name="access_token",
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name="googleaccesstoken",
            name="access_token",
            field=models.CharField(max_length=2048),
        ),
    ]
