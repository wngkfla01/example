# Generated by Django 3.1.4 on 2021-01-08 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
        ('articleapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to='projectapp.project'),
        ),
    ]
