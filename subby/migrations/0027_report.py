# Generated by Django 2.0.6 on 2018-08-01 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import subby.managers.reportmanager


class Migration(migrations.Migration):

    dependencies = [
        ('subby', '0026_auto_20180731_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.IntegerField(choices=[(0, 'Information not matched'), (1, 'Spam Postings'), (2, 'User send spam emails'), (3, 'Other issues')], default=0)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('sublet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sublet', to='subby.Sublet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('objects', subby.managers.reportmanager.ReportManager()),
            ],
        ),
    ]
