from allauth.account.views import SignupView
from .forms import CustomSignupForm

class CustomSignupView(SignupView):
    templates_name = "account/signup.html"
    form_class = CustomSignupForm