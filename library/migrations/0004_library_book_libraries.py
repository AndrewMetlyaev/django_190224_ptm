# Generated by Django 5.0.6 on 2024-06-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_category_book_publisher_id_book_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('site', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='libraries',
            field=models.ManyToManyField(related_name='books', to='library.library'),
        ),
    ]
