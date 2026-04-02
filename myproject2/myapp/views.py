from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


# Create your views here.
def homePageView(request):
    return HttpResponse("My New App! again")

def first(request):
   template = loader.get_template('first.html')
   return HttpResponse(template.render())
    # return render(request,'first.html')

def members(request):
  mymembers = Member.objects.all().values()
#   template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return render(request,'all_members.html',context)
#   return HttpResponse(template.render(context, request))



# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
def testing(request): 
  template = loader.get_template('template.html') 
  context = { 
  'fruits':['banana','apple','kiwi','grapes'] 
  } 
  return HttpResponse(template.render(context, request)) 


