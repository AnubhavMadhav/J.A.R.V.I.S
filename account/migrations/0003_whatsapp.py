# Generated by Django 3.1.4 on 2020-12-03 18:13

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatsApp',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('contact', models.CharField(max_length=100)),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
    ]