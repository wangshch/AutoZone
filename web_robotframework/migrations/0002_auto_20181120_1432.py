# Generated by Django 2.1.1 on 2018-11-20 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_robotframework', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_web_steps',
            name='webcase_models',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apitest.Create_product'),
        ),
    ]