# Generated by Django 2.1.3 on 2018-11-26 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bearing',
            name='parent_equipment_group',
        ),
        migrations.RemoveField(
            model_name='engine',
            name='parent_equipment_group',
        ),
        migrations.RemoveField(
            model_name='gear',
            name='parent_equipment_group',
        ),
        migrations.RemoveField(
            model_name='gearbox',
            name='parent_equipment_group',
        ),
        migrations.RemoveField(
            model_name='motor',
            name='parent_equipment_group',
        ),
        migrations.RemoveField(
            model_name='rotor',
            name='parent_equipment_group',
        ),
        migrations.RemoveField(
            model_name='stator',
            name='parent_equipment_group',
        ),
        migrations.AddField(
            model_name='component',
            name='parent_machine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.Machine'),
        ),
        migrations.AddField(
            model_name='machine',
            name='parent_equipment_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.EquipmentGroup'),
        ),
    ]
