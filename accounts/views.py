from django.shortcuts import render
from django.views.generic import ListView , DetailView ,View


class profile(View):
    def get(self,*args,**kwargs):
        return render(self.request,'account/profile.html')