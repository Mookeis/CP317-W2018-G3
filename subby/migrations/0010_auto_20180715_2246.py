# Generated by Django 2.0.6 on 2018-07-16 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subby', '0009_sublet_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='sublet',
            name='latitude',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sublet',
            name='longitude',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
    ]
