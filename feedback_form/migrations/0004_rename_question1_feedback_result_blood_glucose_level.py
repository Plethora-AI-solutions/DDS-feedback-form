# Generated by Django 5.1.3 on 2024-11-25 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_form', '0003_remove_feedback_result_question2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback_result',
            old_name='question1',
            new_name='blood_glucose_level',
        ),
    ]
