# Generated by Django 5.1 on 2024-08-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgriUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_no', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('status', models.CharField(choices=[('farmer', 'Farmer'), ('labor', 'Labor')], max_length=6)),
                ('amount_of_land', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
