# Generated by Django 3.2.21 on 2023-11-28 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('name', models.CharField(max_length=10, verbose_name='分类标签')),
            ],
            options={
                'verbose_name': '歌曲分类',
                'verbose_name_plural': '歌曲分类',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('name', models.CharField(max_length=50, verbose_name='歌名')),
                ('singer', models.CharField(max_length=50, verbose_name='歌手')),
                ('time', models.CharField(max_length=10, verbose_name='时长')),
                ('album', models.CharField(max_length=50, verbose_name='专辑')),
                ('languages', models.CharField(max_length=20, verbose_name='语种')),
                ('type', models.CharField(max_length=20, verbose_name='类型')),
                ('release', models.DateField(verbose_name='发行时间')),
                ('img', models.FileField(upload_to='songImg/', verbose_name='歌曲图片')),
                ('lyrics', models.FileField(blank=True, default='暂无歌词', upload_to='songLyric/', verbose_name='歌词')),
                ('file', models.FileField(upload_to='songFile/', verbose_name='歌曲文件')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.label', verbose_name='歌名分类')),
            ],
            options={
                'verbose_name': '歌曲信息',
                'verbose_name_plural': '歌曲信息',
            },
        ),
        migrations.CreateModel(
            name='Dynamic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('plays', models.IntegerField(default=0, verbose_name='播放次数')),
                ('search', models.IntegerField(default=0, verbose_name='搜索次数')),
                ('download', models.IntegerField(default=0, verbose_name='下载次数')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.song', verbose_name='歌名')),
            ],
            options={
                'verbose_name': '歌曲动态',
                'verbose_name_plural': '歌曲动态',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('text', models.CharField(max_length=500, verbose_name='内容')),
                ('user', models.CharField(max_length=20, verbose_name='用户')),
                ('date', models.DateField(auto_now=True, verbose_name='日期')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.song', verbose_name='歌名')),
            ],
            options={
                'verbose_name': '歌曲评论',
                'verbose_name_plural': '歌曲评论',
            },
        ),
    ]
