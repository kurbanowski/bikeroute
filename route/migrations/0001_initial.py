# Generated by Django 3.2.4 on 2021-06-07 21:28

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BikeRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NoName', max_length=256)),
                ('polyline', djgeojson.fields.LineStringField()),
            ],
        ),
    ]
