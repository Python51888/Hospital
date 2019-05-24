from django.db import models


class Dept(models.Model): #---部门
    dept_name = models.CharField(max_length=20)
    dept_manager = models.CharField(max_length=20)
    dept_manager_telep = models.CharField(max_length=20)
    dept_floor = models.CharField(max_length=20)


class Patient(models.Model): #---患者
    patient_name = models.CharField(max_length=20)
    patient_sex = models.CharField(max_length=10)
    patient_age = models.CharField(max_length=10)
    patient_telep = models.CharField(max_length=20)
    patient_idcard = models.CharField(max_length=30)
    patient_dept = models.ForeignKey(Dept, on_delete=models.CASCADE)


class Doctor(models.Model): #---医生
    doctor_id = models.CharField(max_length=20)
    doctor_name = models.CharField(max_length=20)
    doctor_sex = models.CharField(max_length=20)
    doctor_age = models.CharField(max_length=20)
    doctor_telep = models.CharField(max_length=20)
    doctor_position = models.CharField(max_length=20)
    doctor_dept = models.ForeignKey(Dept, on_delete=models.CASCADE)


class Room(models.Model): #---房间
    room_id = models.CharField(max_length=10)
    room_patient_id = models.CharField(max_length=20)
    room_patient_name = models.CharField(max_length=20)
    room_patient_dept = models.ForeignKey(Dept, on_delete=models.CASCADE)


class Work(models.Model): #工作安排
    work_doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    work_doctor_name = models.CharField(max_length=20)
    work_time = models.CharField(max_length=20)
    work_doctor_dept = models.ForeignKey(Dept, on_delete=models.CASCADE)


class Deal_method(models.Model): #处理方法
    deal_patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    deal_room_id = models.CharField(max_length=20)
    deal_doctor_name = models.CharField(max_length=20)
    medicine_detail = models.CharField(max_length=50)
    diagnosis_time = models.CharField(max_length=20)  #---诊断时间
    diagnosis_result = models.CharField(max_length=50) #---诊断结果
    doctor_suggestions = models.CharField(max_length=50) #---医生建议


class Medicine(models.Model): #---药品
    medicine_name = models.CharField(max_length=20)
    medicine_num = models.IntegerField()


class User(models.Model): #---用户
    user_name = models.CharField(max_length=50)
    user_passwd = models.CharField(max_length=20)
