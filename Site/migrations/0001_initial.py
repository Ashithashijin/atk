# Generated by Django 3.2 on 2021-10-01 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('gallery', models.ImageField(blank=True, null=True, upload_to='gallery')),
                ('description', models.CharField(blank=True, default='', max_length=5000, null=True)),
                ('subtitle', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('delete_status', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]