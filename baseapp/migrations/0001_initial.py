# Generated by Django 5.1.3 on 2024-11-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chapter', models.CharField(blank=True, max_length=250, null=True, verbose_name='add chapter')),
                ('Added_article', models.TextField(blank=True, null=True, verbose_name='add content of the article')),
            ],
        ),
        migrations.CreateModel(
            name='FirstHomepagePicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='blank-profile-picture.png', upload_to='homepage_photos/')),
                ('caption', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Inqury',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactname', models.CharField(default='contact name', max_length=50)),
                ('contactemail', models.CharField(max_length=70)),
                ('contactsubject', models.EmailField(max_length=250)),
                ('contactmessage', models.TextField(default=' contact message')),
            ],
        ),
        migrations.CreateModel(
            name='SecondHomepagePicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='blank-profile-picture.png', upload_to='homepage_photos/')),
                ('caption', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ThirdHomepagePicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='blank-profile-picture.png', null=True, upload_to='homepage_photos/')),
                ('caption', models.CharField(max_length=200)),
            ],
        ),
    ]
