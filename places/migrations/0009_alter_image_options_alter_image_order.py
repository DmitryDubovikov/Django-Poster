# Generated by Django 4.2.1 on 2023-05-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_remove_image_title_image_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
