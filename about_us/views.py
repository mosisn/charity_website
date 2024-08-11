from accounts.models import User
from django.shortcuts import render

def about_us(request):
    # View for about-us page
    users = User.objects.all()
    user_names = [user.get_full_name() for user in users]
    context = {
        'user_names': user_names
    }
    return render(request, 'about_us.html', context)