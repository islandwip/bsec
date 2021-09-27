# Generated by Django 3.2.4 on 2021-06-14 09:22

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AffectedSmallInvestorCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AffectedSmallInvestorNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='uploads/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CautionNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('notice_content', ckeditor.fields.RichTextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentGuideLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', ckeditor.fields.RichTextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='InvestorComplaintFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='uploads/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='InvestorEduProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='IpoLotteryResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='uploads/')),
                ('submission_date', models.DateTimeField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AffectedSmallInvestorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='uploads/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investorInformation.affectedsmallinvestorcategory')),
            ],
        ),
    ]
