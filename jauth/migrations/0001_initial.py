# Generated by Django 2.2.3 on 2019-07-15 17:13

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ext_user_id', models.CharField(db_index=True, max_length=32, unique=True)),
                ('me', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GoogleAccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=255)),
                ('expire_time', models.DateTimeField(db_index=True)),
                ('ext_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='jauth.GoogleUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FacebookUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ext_user_id', models.CharField(db_index=True, max_length=32, unique=True)),
                ('me', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FacebookAccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=255)),
                ('expire_time', models.DateTimeField(db_index=True)),
                ('ext_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='jauth.FacebookUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountKitUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ext_user_id', models.CharField(db_index=True, max_length=32, unique=True)),
                ('me', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountKitAccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=255)),
                ('expire_time', models.DateTimeField(db_index=True)),
                ('ext_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='jauth.AccountKitUser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]