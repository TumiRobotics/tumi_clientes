# Generated by Django 4.1.4 on 2022-12-28 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tumi', '0003_inspeccioninfo_estadoinspeccion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inspeccioninfo',
            old_name='resultadoUrl',
            new_name='archivoDxf',
        ),
        migrations.AddField(
            model_name='inspeccioninfo',
            name='archivoLas',
            field=models.CharField(default='', max_length=512),
        ),
    ]
