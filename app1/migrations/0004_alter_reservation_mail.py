# Generated by Django 4.2.10 on 2024-03-06 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_reservation_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
