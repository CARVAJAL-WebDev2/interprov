# Generated by Django 3.1.6 on 2021-05-02 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OpenTourList', '0009_auto_20210429_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='TourId',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='OpenTourList.tourist'),
        ),
    ]
