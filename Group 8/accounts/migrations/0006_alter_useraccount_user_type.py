# Generated by Django 4.2.7 on 2023-12-17 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_useraccount_is_verified_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='user_type',
            field=models.CharField(choices=[('APPLICANT', 'Applicant'), ('STAFF', 'Staff'), ('COMMITTEE_MEMBER', 'Committee Member'), ('INSTRUCTOR', 'Instructor'), ('ADMIN', 'Admin')], default='APPLICANT', max_length=50),
        ),
    ]