# Generated by Django 4.2.8 on 2024-03-23 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='book_covers/'),
        ),
        migrations.AddField(
            model_name='book',
            name='sample',
            field=models.FileField(blank=True, null=True, upload_to='book_samples'),
        ),
        migrations.AlterField(
            model_name='bookcontributor',
            name='contributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reviews.contributor'),
        ),
    ]
