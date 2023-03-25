# Generated by Django 4.1 on 2023-03-18 14:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('value', models.SmallIntegerField(blank=True, null=True, verbose_name='Value')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('start_date', models.DateTimeField(verbose_name='Start date')),
                ('end_date', models.DateTimeField(verbose_name='End date')),
            ],
            options={
                'verbose_name': 'Exam',
                'verbose_name_plural': 'Exams',
            },
        ),
        migrations.CreateModel(
            name='ExamQuestion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='exams.exam', verbose_name='Exam')),
            ],
            options={
                'verbose_name': 'ExamQuestion',
                'verbose_name_plural': 'ExamQuestions',
            },
        ),
    ]