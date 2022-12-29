from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms
# Create your views here.

def index(request):
 	return render(request,'index.html')
@csrf_exempt
def form_name_view(request):
 	form = forms.FormName()

 	if request.method == 'POST':
 		form = forms.FormName(request.POST)

 		if form.is_valid():
 			print("validators SUCSSESSS")
 			print("NMAE: "+form.cleaned_data['name'])
 			print("EMAIL : "+form.cleaned_data['email_verify'])
 			print("TEXT : "+form.cleaned_data['text'])

 	return render(request,'form_page.html',{'form':form})