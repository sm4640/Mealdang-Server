# Generated by Django 5.0.7 on 2024-07-22 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=20, unique=True)),
                ('nickname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('gender', models.CharField(max_length=2)),
                ('age', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('is_diabetes', models.BooleanField(default=False)),
                ('fasting_blood_sugar', models.IntegerField(blank=True, null=True)),
                ('post_meal_blood_sugar', models.IntegerField(blank=True, null=True)),
                ('is_subscribe', models.BooleanField(default=False)),
                ('cumulative_podo', models.IntegerField(default=0)),
                ('used_podo', models.IntegerField(default=0)),
                ('remained_podo', models.IntegerField(default=0)),
                ('recommend_count', models.IntegerField(default=0)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
