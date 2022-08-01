# Generated by Django 4.0.3 on 2022-07-26 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CounsellorProfile',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False, unique=True)),
                ('dp', models.ImageField(default='default.jpg', upload_to='Counsellors-Dps')),
                ('dob', models.DateField(null=True)),
                ('age', models.PositiveIntegerField(default=0)),
                ('location', models.CharField(max_length=30)),
                ('phone_no', models.CharField(max_length=14)),
                ('gender', models.CharField(max_length=10)),
                ('marital_status', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('counsellor', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Counsellors',
                'ordering': ['counsellor'],
            },
        ),
        migrations.CreateModel(
            name='WorkProfile',
            fields=[
                ('id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('org', models.CharField(db_column='Place of Work', max_length=50)),
                ('mobile_no', models.CharField(max_length=14)),
                ('location', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=50)),
                ('opening_hours', models.TimeField()),
                ('closing_hours', models.TimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='counsellors.counsellorprofile')),
            ],
            options={
                'verbose_name_plural': 'Places of work',
                'ordering': ['org'],
            },
        ),
    ]
