# Generated by Django 2.1.4 on 2019-06-25 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abp', '0014_badges_reference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badges',
            name='dark',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='dragon',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='electric',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='ghost',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='grass',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='ice',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='normal',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='poison',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='rock',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='water',
        ),
    ]
