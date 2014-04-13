from django.contrib.auth.forms import UserCreationForm
from website.models import Unapproved
from django import forms

class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Unapproved
        fields = ['username']

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if user_form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("somewhere")
        return render(request, self.template_name, { 'form' : form })

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
