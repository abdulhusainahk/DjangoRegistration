from django import forms
from tem.models import Employee, PO, DeliveryMethods, Login, CO, CoPoMapp, Upload_Int, Upload_Ext, ExamScheme, \
	TeachingScheme, Weights, Teaches, Teacher, Admin


class UploadForm(forms.ModelForm):
	class Meta:
		model = Upload_Int
		fields = "__all__"


class TsForm(forms.ModelForm):
    class Meta:
        model = TeachingScheme
        fields = {'theory', 'practicle', 'tutorial'}


class EsForm(forms.ModelForm):
    class Meta:
        model = ExamScheme
        fields = {'onlineinsem', 'endsem', 'termwork', 'Practicle', 'oral'}


class WeightForm(forms.ModelForm):
    class Meta:
        model = Weights
        fields = {'ext_weight', 'target'}


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class TeachesForm(forms.ModelForm):
    class Meta:
        model = Teaches
        fields = "__all__"
   
	    
class UploadForm1(forms.ModelForm):
	class Meta:
		model = Upload_Ext
		fields = "__all__"


class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = "__all__"


class DmForm(forms.ModelForm):
    class Meta:
        model = DeliveryMethods
        fields = {'chalktalk', 'ict', 'gd','ifv','et','sur','mp','lab'}


class PosForm(forms.ModelForm):
	class Meta:
		model = PO
		fields = "__all__"
		

class COForm(forms.ModelForm):
	class Meta:
		model = CO
		fields = {'Outcome','assignments','units', 'insem', 'endsem', 'practicle', 'TW'}
		
		
class LoginForm(forms.ModelForm):
	class Meta:
		model = Login
		fields = "__all__"
		
		
class MappingForm(forms.ModelForm):
    class Meta:
        model = CoPoMapp
        fields = {'VPO1', 'VPO2', 'VPO3', 'VPO4', 'VPO5', 'VPO6', 'VPO7', 'VPO8', 'VPO9', 'VPO10', 'VPO11', 'VPO12'}
        widgets = {
			'VPO1': forms.Select(attrs={'style': 'width:40px'}),
	        'VPO2': forms.Select(attrs={'style': 'width:40px'}),
	        'VPO3': forms.Select(attrs={'style': 'width:40px'}),
	        'VPO4': forms.Select(attrs={'style': 'width:40px'}),
	        'VPO5': forms.Select(attrs={'style': 'width:40px'}),
	        'VPO6': forms.Select(attrs={'style': 'width:40px'}),
	        'VPO7': forms.Select(attrs={'style': 'width:40px'}),
	        'VPO8': forms.Select(attrs={'style': 'width:40px'}),
	        'VPO9': forms.Select(attrs={'style': 'width:40px'}),
	        'VPO10': forms.Select(attrs={'style': 'width:40px'}),
	        'VPO11': forms.Select(attrs={'style': 'width:40px'}),
	        'VPO12': forms.Select(attrs={'style': 'width:40px'}),
	        
		}

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        widgets = {
            'Password': forms.PasswordInput(),
        }
        fields = "__all__"


class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = "__all__"
