from .models import Student
from django import forms


class StudentForm(forms.ModelForm):
    # name = forms.CharField(label='姓名', max_length=128)
    # sex = forms.CharField(label='性别', choices=Student.SEX_ITEMS)
    # profession = forms.CharField(label='职业', max_length=128)
    # email = forms.CharField(label='邮箱', max_length=128)
    # qq = forms.CharField(label='QQ', max_length=128)
    # phone = forms.CharField(label='手机', max_length=128)

    def clean_qq(self):
        cleaned_date = self.cleaned_data['qq']
        if not cleaned_date.isdigit():
            raise forms.ValidationError('必须为数字!')

        return int(cleaned_date)

    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession', 'email', 'qq', 'phone'
        )
