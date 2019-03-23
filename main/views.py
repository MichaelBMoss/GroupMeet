from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from accounts.models import Interests_m
from accounts.models import Activation
from django.contrib.auth.models import User

class IndexPageView(TemplateView):
    template_name = 'main/index.html'


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'


def questions_page(request):
    print('called questions page')
    context = {
        }
    if request.user.is_authenticated:
        if request.method == 'POST':
            Interests_m.objects.filter(user=request.user).delete()
            try:
                my_interests_list = request.POST.getlist('interest')
                Interests_m.objects.create(
                    interest1=my_interests_list[0],
                    interest2=my_interests_list[1],
                    interest3=my_interests_list[2],
                    interest4=my_interests_list[3],
                    interest5=my_interests_list[4],
                    user=request.user,
                    email=request.user.email,
                )
            except:
                return redirect('/questions_error')        
            return redirect('/search')
        else:
            print('else is happening-------------------------------')
            return render(request, 'questions.html', context)
    else:
        return redirect('/')

def questions_error(request):
    context = {}
    return render(request, 'questions_error.html', context)

def search_page(request):
    context = {}
    if request.user.is_authenticated:
        interests = Interests_m.objects.order_by('id')
        if request.method == 'POST':
            print('if is happening--------------------------------')
            my_search_list = request.POST.getlist('search')
            choice = my_search_list[0].replace("_", " ")
            context = {
                'interests' : interests,
                'choice' : choice,
                }
            return render(request, 'search.html', context)
        else:
            print('else is happening------------------------------------')
            context = {
                'interests' : interests,
                }
            return render(request, 'search.html', context)
    else:
        return redirect('/')

