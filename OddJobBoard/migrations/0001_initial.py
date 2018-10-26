# Generated by Django 2.1.2 on 2018-10-22 23:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OddJobBoard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('area', models.TextField(blank=True)),
                ('work', models.TextField(blank=True)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]