# Generated by Django 4.0.3 on 2022-03-25 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameplayer',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
