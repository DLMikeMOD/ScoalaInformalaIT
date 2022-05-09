from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='active',
            field=models.BooleanField(default=1),
        ),
    ]