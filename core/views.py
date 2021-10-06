from django.views.generic.base import TemplateView
from django.shortcuts import render 

class HomePageView(TemplateView):
    #template_name = es una especio de atributo de la clase 
    template_name = "core/home.html"

    def get(self, request,*args, **kwargs):
        #se hace un return render se le pasa la peticion, el template name , para despues pasar el diccionario de contexto 
        return render (request, self.template_name, {'title':"The Web Django"})

class SamplePageView(TemplateView):
    template_name="core/sample.html"

