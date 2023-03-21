from django.shortcuts import render
from django.views import  View
from .models import *
# Create your views here.

class Index(View):
    def get(self,request):
        langs = Language.objects.filter(taken=False)
        chosen = Language.objects.filter(taken=True)

        params = {
            "langs": langs,
            "chosen": chosen
        }
        return render(request, 'main/index.html', params)
    def post(self,request):
        post_data = request.POST
        print(post_data)
        lang = Language.objects.get(pk=int(post_data['langs']))
        group = None
        if Group.objects.filter(pk=int(post_data['group_name'])).exists():
            group = Group.objects.get(pk=int(post_data['group_name']))
        else:
            group = Group(group_name=int(post_data['group_name']))
            group.save()

        if len(Language.objects.filter(group_id=group.id)) > 0:
            print("Already assigend something")
        else:
            n_lang = Language.objects.get(pk=int(post_data['langs']))
            n_lang.group = group
            n_lang.taken = True
            n_lang.save()
        langs = Language.objects.filter(taken=False)
        chosen = Language.objects.filter(taken=True)
        print(chosen)
        params = {
            "langs":langs,
            "chosen": chosen
        }
        return render(request, 'main/index.html', params)

