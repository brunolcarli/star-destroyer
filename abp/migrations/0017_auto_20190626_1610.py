# Generated by Django 2.1.4 on 2019-06-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abp', '0016_trainer_badges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='badges',
            field=models.ManyToManyField(to='abp.Badges'),
        ),
    ]
