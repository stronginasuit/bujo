# Generated by Django 3.1.5 on 2021-01-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bujodb',
            name='day',
            field=models.CharField(choices=[('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('Th', 'Thursday'), ('F', 'Friday'), ('Sa', 'Saturday'), ('Su', 'Sunday'), ('X', 'Otherstuff')], default='X', max_length=2),
        ),
    ]
