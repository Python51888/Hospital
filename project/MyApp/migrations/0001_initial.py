# Generated by Django 2.2.1 on 2019-05-19 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=20)),
                ('dept_manager', models.CharField(max_length=20)),
                ('dept_manager_telep', models.CharField(max_length=20)),
                ('dept_floor', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.CharField(max_length=20)),
                ('doctor_name', models.CharField(max_length=20)),
                ('doctor_sex', models.CharField(max_length=20)),
                ('doctor_age', models.CharField(max_length=20)),
                ('doctor_telep', models.CharField(max_length=20)),
                ('doctor_position', models.CharField(max_length=20)),
                ('doctor_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Dept')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=20)),
                ('medicine_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_passwd', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_doctor_name', models.CharField(max_length=20)),
                ('work_time', models.CharField(max_length=20)),
                ('work_doctor_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Dept')),
                ('work_doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=10)),
                ('room_patient_id', models.CharField(max_length=20)),
                ('room_patient_name', models.CharField(max_length=20)),
                ('room_patient_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Dept')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=20)),
                ('patient_sex', models.CharField(max_length=10)),
                ('patient_age', models.CharField(max_length=10)),
                ('patient_telep', models.CharField(max_length=20)),
                ('patient_idcard', models.CharField(max_length=30)),
                ('patient_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Dept')),
            ],
        ),
        migrations.CreateModel(
            name='Deal_method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_room_id', models.CharField(max_length=20)),
                ('deal_doctor_name', models.CharField(max_length=20)),
                ('medicine_detail', models.CharField(max_length=50)),
                ('diagnosis_time', models.CharField(max_length=20)),
                ('diagnosis_result', models.CharField(max_length=50)),
                ('doctor_suggestions', models.CharField(max_length=50)),
                ('deal_patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Patient')),
            ],
        ),
    ]