# Generated by Django 4.1.3 on 2022-12-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=10000)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='products',
        ),
    ]
