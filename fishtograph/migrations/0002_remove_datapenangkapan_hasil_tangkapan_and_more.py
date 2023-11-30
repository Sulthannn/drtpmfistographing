# Generated by Django 4.2.6 on 2023-10-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishtograph', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datapenangkapan',
            name='hasil_tangkapan',
        ),
        migrations.AlterField(
            model_name='datapenangkapan',
            name='alat_tangkap',
            field=models.CharField(choices=[('LD', 'Lempura Dasar'), ('PG', 'Payang'), ('BB', 'Bagan Berperahu'), ('JIP', 'Jaring Insang Tetap'), ('JIB', 'Jaring Insang Berlapis')], default='LD', max_length=255),
        ),
    ]
