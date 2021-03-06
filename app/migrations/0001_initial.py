# Generated by Django 2.1.1 on 2020-02-10 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('hot', models.IntegerField(default=0)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('weixin', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'mask_product',
            },
        ),
    ]
