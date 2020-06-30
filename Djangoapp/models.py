from django.core.validators import validate_comma_separated_integer_list
from django.db import models

weight_choice = [
	(0.1, 0.1),
	(0.2, 0.2),
	(0.3, 0.3),
	(0.4, 0.4),
	(0.5, 0.5),
	(0.6, 0.6),
	(0.7, 0.7),
	(0.8, 0.8),
	(0.9, 0.9),
	(1.0, 1.0),
]

pochoice = [
	(0,0),
(1,1),
(2,2),
(3,3),
]


class Employee(models.Model):
	course = models.CharField(primary_key=True, max_length=20)
	password = models.CharField(max_length=50)
	CourseName = models.CharField(max_length=50)
	
	class Meta:
		db_table = "employee"


class Upload_Int(models.Model):
	Code_patt = models.ForeignKey(Employee, on_delete=models.CASCADE)
	A1 = models.FloatField(default=0)
	A2 = models.FloatField(default=0)
	A3 = models.FloatField(default=0)
	A4 = models.FloatField(default=0)
	A5 = models.FloatField(default=0)
	ut1 = models.FloatField(default=0)
	ut2 = models.FloatField(default=0)
	ut3 = models.FloatField(default=0)
	ut4 = models.FloatField(default=0)
	ut5 = models.FloatField(default=0)
	tw = models.FloatField(default=0)
	
	class Meta:
		db_table = "upload"


class Upload_Ext(models.Model):
	Code_patt = models.ForeignKey(Employee, on_delete=models.CASCADE)
	insem = models.FloatField()
	endsem = models.FloatField()
	practicals = models.FloatField()
	TW = models.FloatField(null=True, blank=True)
	
	class Meta:
		db_table = "upload1"


class Admin(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'admin'


class TeachingScheme(models.Model):
    Code_patt = models.ForeignKey(Employee, on_delete=models.CASCADE, unique=True)
    theory = models.CharField(max_length=5)
    practicle = models.CharField(max_length=5)
    tutorial = models.CharField(max_length=5)

    class Meta:
        db_table = 'teachingscheme'
	    
	    
class ExamScheme(models.Model):
	Code_patt = models.ForeignKey(Employee, on_delete=models.CASCADE, unique=True)
	onlineinsem = models.IntegerField(blank=True, null=True)
	endsem = models.IntegerField(blank=True, null=True)
	termwork = models.IntegerField(blank=True, null=True)
	Practicle = models.IntegerField(blank=True, null=True)
	oral = models.IntegerField(blank=True, null=True)
	
	class Meta:
		db_table = "examscheme"


class CO(models.Model):
	CO_id = models.CharField(primary_key=True, max_length=20)
	Outcome = models.TextField(max_length=500)
	assignments = models.CharField(max_length=20, validators=[validate_comma_separated_integer_list])
	units = models.CharField(max_length=20, validators=[validate_comma_separated_integer_list])
	insem = models.BooleanField()
	endsem = models.BooleanField()
	practicle = models.BooleanField()
	TW = models.BooleanField()
	class Meta:
		db_table = 'co'


class Assesment(models.Model):
	CO_id = models.OneToOneField(CO, on_delete=models.CASCADE)
	assignment = models.FloatField(default=0)
	practicle = models.FloatField(default=0)
	termwork = models.FloatField(default=0)
	unittests = models.FloatField(default=0)
	insem = models.FloatField(default=0)
	endsem = models.FloatField(default=0)
	assessment = models.FloatField(default=0)
	level = models.IntegerField(default=0)
	
	class Meta:
		db_table = "assesment"


class DeliveryMethods(models.Model):
	Code_patt = models.ForeignKey(Employee, on_delete=models.CASCADE)
	chalktalk = models.BooleanField()
	ict = models.BooleanField()
	gd = models.BooleanField()
	ifv = models.BooleanField()
	et = models.BooleanField()
	sur = models.BooleanField()
	mp = models.BooleanField()
	lab = models.BooleanField()
	
	class Meta:
		db_table = 'deliverymethods'


class CoPoMapp(models.Model):
	CO_id = models.OneToOneField(CO, on_delete=models.CASCADE)
	VPO1 = models.IntegerField(choices=pochoice,default=2)
	VPO2 = models.IntegerField(choices=pochoice,default=2)
	VPO3 = models.IntegerField(choices=pochoice,default=2)
	VPO4 = models.IntegerField(choices=pochoice,default=2)
	VPO5 = models.IntegerField(choices=pochoice,default=2)
	VPO6 = models.IntegerField(choices=pochoice,default=2)
	VPO7 = models.IntegerField(choices=pochoice,default=2)
	VPO8 = models.IntegerField(choices=pochoice,default=2)
	VPO9 = models.IntegerField(choices=pochoice,default=1)
	VPO10 = models.IntegerField(choices=pochoice,default=2)
	VPO11 = models.IntegerField(choices=pochoice,default=2)
	VPO12 = models.IntegerField(choices=pochoice,default=2)
	
	class Meta:
		db_table = 'copomapp'


class PO(models.Model):
	id = models.IntegerField(primary_key=True)
	po = models.TextField()
	
	class Meta:
		db_table = "po"


class Login(models.Model):
	course = models.CharField(primary_key=True, max_length=10)
	password = models.CharField(max_length=10)
	
	class Meta:
		db_table = "Login"


class Weights(models.Model):
    Code_patt = models.ForeignKey(Employee, on_delete=models.CASCADE, unique=True)
    int_weight = models.FloatField()
    ext_weight = models.FloatField(choices=weight_choice)
    target = models.IntegerField()

    class Meta:
        db_table = "weights"


class Teacher(models.Model):
    t_id = models.IntegerField(primary_key=True)
    t_name = models.CharField(max_length=30)
    t_contact = models.BigIntegerField()

    class Meta:
        db_table = "teacher"


class Teaches(models.Model):
    t_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Code_patt = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Class = models.CharField(max_length=20)
    sem = models.IntegerField()
    A_Y = models.IntegerField()

    class Meta:
        db_table = "teaches"


class Report(models.Model):
    Course_name = models.CharField(max_length=20)
    CO_id = models.OneToOneField(CO, on_delete=models.CASCADE)
    assessment = models.FloatField()
    Y_N = models.CharField(max_length=3)
    VPO1 = models.IntegerField(null=True, blank=True)
    VPO2 = models.IntegerField(null=True, blank=True)
    VPO3 = models.IntegerField(null=True, blank=True)
    VPO4 = models.IntegerField(null=True, blank=True)
    VPO5 = models.IntegerField(null=True, blank=True)
    VPO6 = models.IntegerField(null=True, blank=True)
    VPO7 = models.IntegerField(null=True, blank=True)
    VPO8 = models.IntegerField(null=True, blank=True)
    VPO9 = models.IntegerField(null=True, blank=True)
    VPO10 = models.IntegerField(null=True, blank=True)
    VPO11 = models.IntegerField(null=True, blank=True)
    VPO12 = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "report"
