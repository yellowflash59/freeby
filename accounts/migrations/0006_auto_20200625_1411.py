# Generated by Django 3.0.7 on 2020-06-25 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_emaialmarketingsignup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmaialMarketingSignup',
            new_name='EmailMarketingSignup',
        ),
    ]