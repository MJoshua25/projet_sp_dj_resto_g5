# Generated by Django 2.2.6 on 2019-10-08 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temoignage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statut', models.BooleanField(default=False)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('nom', models.CharField(max_length=160)),
                ('commentaire', models.TextField()),
                ('job', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Temoignage',
                'verbose_name_plural': 'Temoignages',
            },
        ),
    ]
