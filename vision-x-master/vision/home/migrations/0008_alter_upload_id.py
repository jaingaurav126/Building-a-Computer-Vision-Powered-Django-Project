# Generated by Django 3.2.3 on 2021-08-11 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20201102_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]