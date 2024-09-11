# Generated by Django 5.1 on 2024-09-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('flight_type', models.CharField(choices=[('Nacional', 'Nacional'), ('Internacional', 'Internacional')], max_length=15)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
