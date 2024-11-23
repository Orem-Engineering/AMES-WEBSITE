# Generated by Django 5.1.3 on 2024-11-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Newsletter subscribers email', max_length=254, unique=True)),
            ],
            options={
                'verbose_name': 'Subscribers',
            },
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(help_text='email subject ', max_length=255, unique=True)),
                ('Recipients', models.ManyToManyField(help_text='email subject ', to='newsletterapp.subscriber')),
            ],
            options={
                'verbose_name': 'Email Template',
            },
        ),
    ]
