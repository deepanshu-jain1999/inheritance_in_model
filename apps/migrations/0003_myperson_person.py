# Generated by Django 2.0.2 on 2018-03-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_place_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MyPerson',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('apps.person',),
        ),
    ]
