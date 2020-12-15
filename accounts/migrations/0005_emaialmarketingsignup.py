# Generated by Django 3.0.7 on 2020-06-25 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200619_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmaialMarketingSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
    ]
