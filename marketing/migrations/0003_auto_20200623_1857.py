# Generated by Django 3.0.7 on 2020-06-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_auto_20200623_1800'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['order', '-start_date', '-end_date']},
        ),
        migrations.AddField(
            model_name='slider',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
