# Generated by Django 4.1.7 on 2023-03-20 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("crosswordApp", "0003_crossword_clues_hor_crossword_clues_ver_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="crossword",
            name="clues_hor",
        ),
        migrations.RemoveField(
            model_name="crossword",
            name="clues_ver",
        ),
        migrations.RemoveField(
            model_name="crossword",
            name="grid",
        ),
    ]
