# Generated by Django 3.2.3 on 2021-05-24 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectModelSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TodoModelSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=256, verbose_name='текст')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='обновил')),
                ('active', models.BooleanField(default=True, verbose_name='активный')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='todoapp.projectmodelset')),
            ],
        ),
    ]
