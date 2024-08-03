# Generated by Django 5.0.7 on 2024-08-02 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogtechnology', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published']},
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'پیشنویس'), ('published', 'منشترشده')], default='published', max_length=10, verbose_name='وضعیت انتشار'),
        ),
    ]
