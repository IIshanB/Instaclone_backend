# Generated by Django 4.2.9 on 2024-02-09 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userprofile_profile_pic_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkEdge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='users.userprofile')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='users.userprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
