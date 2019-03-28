from django import forms

    
class RegistrationForm(forms.Form):
      username = forms.CharField(label='Имя пользователя', max_length=15)
      password = forms.CharField(label='Пароль', max_length=15,
                                 widget = forms.PasswordInput())
      email = forms.CharField(label='Эл-почта', max_length=25)
      
      username.widget.attrs.update(size='45')
      password.widget.attrs.update(size='45')
      email.widget.attrs.update(size='45')
      
      
class EditForm(forms.Form):
      ad_title = forms.CharField(label='Заголовок', max_length=50)
      ad_text = forms.CharField(label='Текст объявления', max_length=255,
                                widget=forms.Textarea)
      
      ad_title.widget.attrs.update(size='60')
      ad_text.widget.attrs.update(cols='58', rows="10")
