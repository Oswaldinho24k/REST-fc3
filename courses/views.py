from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class Registro(View):
	def get(self, request):
		template = "registro.html"
		return render(request, template)
