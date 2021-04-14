# from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'


def user_info(request):
    # user_info = User.objects.get(request.user)
    context = {
        # 'userinfo': user_info
    }
    return render(request, 'user_info.html', context)
