from django.shortcuts import render
from django.views.generic import View

class editorView(View):
    def get(self,*args,**kwargs):
        return render(self.request,'editor.html')
    
    def post(self,*args, **kwargs):
        pass
    