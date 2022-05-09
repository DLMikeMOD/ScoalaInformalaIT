# Generated by Django 4.0.4 on 2022-05-02 16:37
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('app1', '0001_initial'),
        ('app2', '0001_initial'),
    ]
    operations = [
        migrations.AddField(
            model_name='companies',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.location'),
            preserve_default=False,
        ),
    ]