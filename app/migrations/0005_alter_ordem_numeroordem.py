# Generated by Django 3.2.9 on 2021-11-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_ordem_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem',
            name='numeroordem',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]