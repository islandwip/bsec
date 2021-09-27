# Generated by Django 3.2.4 on 2021-06-15 05:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetManagementCompaniesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('address', ckeditor.fields.RichTextField()),
                ('contact', models.TextField()),
                ('date', models.DateField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CentralDepository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CreditRatingAgenciesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('address', ckeditor.fields.RichTextField()),
                ('contact', models.TextField()),
                ('date', models.DateField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CustodiansList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('address', ckeditor.fields.RichTextField()),
                ('contact', models.TextField()),
                ('certification_date', models.DateField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FundManagersList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MerchantBankersList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('address', ckeditor.fields.RichTextField()),
                ('contact', models.TextField()),
                ('date', models.DateField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StockExchanges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TrusteesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('intactive', 'inactive')], default='active', max_length=10)),
            ],
        ),
    ]
