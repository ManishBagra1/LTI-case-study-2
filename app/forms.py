from django import forms
from .Data import citystate
from django.core.exceptions import ValidationError  

class djangoform(forms.Form):
    sid = forms.IntegerField()
    def clean_sid(self):
        data = self.cleaned_data.get('sid')
        file = open('app/Data/students.csv','r')
        IDs = []
        for line in file:
            x = line.strip().split(',')
            IDs.append(x[0])
        IDs.remove(IDs[0])
        IDs= [int(i) for i in IDs]
        file.close()

        if not data in IDs:
            raise ValidationError(f"No student Exist with id : {data}")
        return data
            
class DateInput(forms.DateInput):
	input_type = 'date'
class contactform(forms.Form):
	sid = forms.IntegerField(label='Student Id')

	def clean_sid(self):
		data = self.cleaned_data['sid']
		if data in self.id_list():
			raise ValidationError("id already exist")
		return data	

	name = forms.CharField(label='Student Name')

	gender = forms.ChoiceField(label="Gender",
								choices=[('Male','Male'),('Female','Female')],
								widget=forms.RadioSelect)

	dob = forms.DateField(widget=DateInput)

	temp = citystate.citylistforform()   # importing data for city list 

	city = forms.ChoiceField(label="City",choices=temp)

	temp1 = citystate.statelistforform()   # importing data for state list

	state = forms.ChoiceField(label="State",
							   choices=temp1)


	email = forms.EmailField(label="E-mail")

	def clean_email(self):
		data = self.cleaned_data['email']
		if data.lower() in self.email_list():
			raise ValidationError("email already exist")
		return 	data

	qualification = forms.ChoiceField(label='Qualification',choices=[(None,'Choose Your qualification'),('B.E','B.E'),('B.Tech','B.Tech'),('B.sc','B.sc'),('M.Tech','M.Tech'),('M.sc','M.sc')])
	
	stream = forms.ChoiceField(label='Stream',choices=[(None,'Choose Your Stream'),('Computer Science','Computer Science'),('Electrical','Electrical'),('Electronics','Electronics'),('Mechanical','Mechanical'),('Civil','Civil')])


	def  id_list(self):
		file = open('app/Data/students.csv','r')
		IDs = []
		for line in file:
			x = line.strip().split(',')
			IDs.append(x[0])
		IDs.remove(IDs[0])
		IDs= [int(i) for i in IDs]
		file.close()
		return IDs

	def email_list(self):
		file = open('app/Data/students.csv','r')
		Emails = []
		for line in file:
			x = line.strip().split(',')
			Emails.append(x[6])

		Emails.remove(Emails[0])	
		Emails= [i.lower() for i in Emails]
		file.close()
		return Emails
            
                
                
            
            
            
