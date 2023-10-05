# Generated by Django 4.2.4 on 2023-09-03 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='courses.course'),
        ),
    ]
