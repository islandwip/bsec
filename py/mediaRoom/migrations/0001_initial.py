# Generated by Django 3.2.4 on 2021-06-24 06:19

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AwardAchivement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='uploads/')),
                ('form', models.FileField(upload_to='uploads/form/')),
                ('link', models.CharField(max_length=2083)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('closing_date', models.DateField()),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='InnovationIdeas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='InnovationNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='uploads/')),
                ('date', models.DateField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='NOC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='NotableEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='uploads/')),
                ('date', models.DateField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OfficeOrderCircular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='uploads/')),
                ('date', models.DateField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PressRelease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='uploads/')),
                ('date', models.DateField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='uploads/')),
                ('date', models.DateField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VideoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=2083)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
    ]