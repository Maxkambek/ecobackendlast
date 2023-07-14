# Generated by Django 4.2 on 2023-04-20 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_ky', models.CharField(max_length=100, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Calculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Calculator',
                'verbose_name_plural': 'Calculator',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=212, verbose_name='Name')),
                ('name_en', models.CharField(max_length=212, null=True, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=212, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=212, null=True, verbose_name='Name')),
                ('name_ky', models.CharField(max_length=212, null=True, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('title', models.CharField(max_length=250, verbose_name='Position')),
                ('title_en', models.CharField(max_length=250, null=True, verbose_name='Position')),
                ('title_uz', models.CharField(max_length=250, null=True, verbose_name='Position')),
                ('title_ru', models.CharField(max_length=250, null=True, verbose_name='Position')),
                ('title_ky', models.CharField(max_length=250, null=True, verbose_name='Position')),
                ('phone', models.CharField(max_length=70, verbose_name='Phone')),
                ('address', models.CharField(max_length=223, verbose_name='Manzili')),
                ('address_en', models.CharField(max_length=223, null=True, verbose_name='Manzili')),
                ('address_uz', models.CharField(max_length=223, null=True, verbose_name='Manzili')),
                ('address_ru', models.CharField(max_length=223, null=True, verbose_name='Manzili')),
                ('address_ky', models.CharField(max_length=223, null=True, verbose_name='Manzili')),
            ],
            options={
                'verbose_name': 'Direktorlar',
                'verbose_name_plural': 'Direktorlar',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222, verbose_name='Title')),
                ('title_en', models.CharField(max_length=222, null=True, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=222, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=222, null=True, verbose_name='Title')),
                ('title_ky', models.CharField(max_length=222, null=True, verbose_name='Title')),
                ('subtitle', models.CharField(blank=True, max_length=333, null=True, verbose_name='Subtitle')),
                ('subtitle_en', models.CharField(blank=True, max_length=333, null=True, verbose_name='Subtitle')),
                ('subtitle_uz', models.CharField(blank=True, max_length=333, null=True, verbose_name='Subtitle')),
                ('subtitle_ru', models.CharField(blank=True, max_length=333, null=True, verbose_name='Subtitle')),
                ('subtitle_ky', models.CharField(blank=True, max_length=333, null=True, verbose_name='Subtitle')),
                ('image', models.ImageField(upload_to='news', verbose_name='Image')),
                ('content', models.TextField(verbose_name='Content')),
                ('content_en', models.TextField(null=True, verbose_name='Content')),
                ('content_uz', models.TextField(null=True, verbose_name='Content')),
                ('content_ru', models.TextField(null=True, verbose_name='Content')),
                ('content_ky', models.TextField(null=True, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('text', models.CharField(max_length=123)),
                ('text_en', models.CharField(max_length=123, null=True)),
                ('text_uz', models.CharField(max_length=123, null=True)),
                ('text_ru', models.CharField(max_length=123, null=True)),
                ('text_ky', models.CharField(max_length=123, null=True)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Spirituality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Spirituality/', verbose_name='Image')),
                ('title', models.CharField(max_length=333, verbose_name='Title')),
                ('title_en', models.CharField(max_length=333, null=True, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=333, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=333, null=True, verbose_name='Title')),
                ('title_ky', models.CharField(max_length=333, null=True, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('content_en', models.TextField(null=True, verbose_name='Content')),
                ('content_uz', models.TextField(null=True, verbose_name='Content')),
                ('content_ru', models.TextField(null=True, verbose_name='Content')),
                ('content_ky', models.TextField(null=True, verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Spirituality',
                'verbose_name_plural': 'Spirituality',
            },
        ),
        migrations.CreateModel(
            name='NewsDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='news/')),
                ('content', models.TextField(null=True, verbose_name='Content')),
                ('content_en', models.TextField(null=True, verbose_name='Content')),
                ('content_uz', models.TextField(null=True, verbose_name='Content')),
                ('content_ru', models.TextField(null=True, verbose_name='Content')),
                ('content_ky', models.TextField(null=True, verbose_name='Content')),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_detail', to='main.news')),
            ],
            options={
                'verbose_name': 'Image of News',
                'verbose_name_plural': 'Image of News',
            },
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=212, verbose_name='Name')),
                ('name_en', models.CharField(max_length=212, null=True, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=212, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=212, null=True, verbose_name='Name')),
                ('name_ky', models.CharField(max_length=212, null=True, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('title', models.CharField(max_length=250, verbose_name='Position')),
                ('title_en', models.CharField(max_length=250, null=True, verbose_name='Position')),
                ('title_uz', models.CharField(max_length=250, null=True, verbose_name='Position')),
                ('title_ru', models.CharField(max_length=250, null=True, verbose_name='Position')),
                ('title_ky', models.CharField(max_length=250, null=True, verbose_name='Position')),
                ('phone', models.CharField(max_length=70, verbose_name='Phone')),
                ('address', models.CharField(max_length=223, verbose_name='Manzili')),
                ('address_en', models.CharField(max_length=223, null=True, verbose_name='Manzili')),
                ('address_uz', models.CharField(max_length=223, null=True, verbose_name='Manzili')),
                ('address_ru', models.CharField(max_length=223, null=True, verbose_name='Manzili')),
                ('address_ky', models.CharField(max_length=223, null=True, verbose_name='Manzili')),
                ('description', models.TextField(verbose_name='Filial haqida malumot')),
                ('description_en', models.TextField(null=True, verbose_name='Filial haqida malumot')),
                ('description_uz', models.TextField(null=True, verbose_name='Filial haqida malumot')),
                ('description_ru', models.TextField(null=True, verbose_name='Filial haqida malumot')),
                ('description_ky', models.TextField(null=True, verbose_name='Filial haqida malumot')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.branch', verbose_name='Branch')),
            ],
            options={
                'verbose_name': 'Hodimlar',
                'verbose_name_plural': 'Hodimlar',
            },
        ),
    ]
