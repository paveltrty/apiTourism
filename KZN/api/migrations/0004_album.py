# Generated by Django 4.2.2 on 2023-07-02 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_place_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='post_images/')),
                ('Post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.place')),
            ],
        ),
    ]
