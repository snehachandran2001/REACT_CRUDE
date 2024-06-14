# Generated by Django 5.0.6 on 2024-06-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=50, null=True)),
                ('student_address', models.TextField()),
                ('student_department', models.CharField(max_length=50, null=True)),
                ('student_image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
