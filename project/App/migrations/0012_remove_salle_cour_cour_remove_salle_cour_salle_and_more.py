# Generated by Django 4.2.1 on 2023-05-16 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_cour_etudiant_filiere_salle_users_salle_cour_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salle_cour',
            name='cour',
        ),
        migrations.RemoveField(
            model_name='salle_cour',
            name='salle',
        ),
        migrations.DeleteModel(
            name='Presence_Cour',
        ),
        migrations.DeleteModel(
            name='Salle',
        ),
        migrations.DeleteModel(
            name='Salle_Cour',
        ),
    ]
