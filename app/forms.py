from django import forms
g=[('Male','M'),('Female','F')]
courses=[('PYTHON','Python'),('HTML','Html'),('CSS','Css'),('SQL','Sql'),('JAVASCRIPT','JS')]
class NameForm(forms.Form):
    name=forms.CharField(max_length=20)
    age=forms.IntegerField(min_value=18)
    email=forms.EmailField()
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)
    address=forms.CharField(max_length=100,widget=forms.Textarea)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    courses=forms.MultipleChoiceField(choices=courses,widget=forms.CheckboxSelectMultiple)