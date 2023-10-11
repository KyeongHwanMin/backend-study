# Generated by Django 4.0.10 on 2023-10-11 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecruitmentNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(help_text='채용 포지션', max_length=50)),
                ('compensation', models.SmallIntegerField(default=0, help_text='채용 보상금')),
                ('content', models.TextField(blank=True)),
                ('skill', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='생성 날짜')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='수정 날짜')),
                ('company', models.ForeignKey(help_text='회사 ID', on_delete=django.db.models.deletion.CASCADE, related_name='recruitment_notices', to='company.company')),
            ],
            options={
                'db_table': 'recruitmentNotice',
            },
        ),
    ]
