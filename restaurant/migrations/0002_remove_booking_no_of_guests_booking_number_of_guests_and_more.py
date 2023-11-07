# Generated by Django 4.2.5 on 2023-11-05 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='no_of_guests',
        ),
        migrations.AddField(
            model_name='booking',
            name='number_of_guests',
            field=models.IntegerField(default=1, help_text='Number of guests in the reservation'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(help_text='Date and time of the reservation'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(help_text='Available quantity of the menu item'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Price of the menu item', max_digits=10),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(help_text='Name of the menu item', max_length=255),
        ),
    ]