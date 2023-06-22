# Generated by Django 4.0.5 on 2022-09-09 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear'), ('W', 'watches'), ('S', 'Shoes'), ('Sl', 'sleeper'), ('Sa', 'Sandal'), ('tr', 'traditional mens')], max_length=7),
        ),
    ]
