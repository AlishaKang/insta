from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User 

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User 
        field = UserCreationForm.Meta.fields
        fields = ('username', 'profile_image', )

class CustomAuthenicationForm(AuthenticationForm):
    pass