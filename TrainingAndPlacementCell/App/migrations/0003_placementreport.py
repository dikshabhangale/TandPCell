# Generated by Django 4.0.3 on 2022-10-02 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_rename_file_mou_mou'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacementReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('report', models.FileField(upload_to='Mou')),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
