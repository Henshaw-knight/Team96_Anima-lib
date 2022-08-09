# Generated by Django 4.0.6 on 2022-08-09 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_message_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyLib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('liked', models.BooleanField(default=False)),
                ('saved', models.BooleanField(default=False)),
                ('downloaded', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='My_Lib',
        ),
        migrations.RemoveField(
            model_name='message',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profilepic.jpg', upload_to='profile_pictures'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lib',
            name='anima_type',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='mylib',
            name='animation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.lib'),
        ),
        migrations.AddField(
            model_name='mylib',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]