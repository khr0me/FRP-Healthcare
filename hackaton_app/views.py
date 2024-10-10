from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Post

class Pages:
	def home(request) -> object:
		return render(request, 'index.html')

	#####################
	### ITALIAN PAGES ###
	#####################
	def problem(request) -> object:
		return render(request, 'problems.html') 
	def solution(request) -> object:
		return render(request, 'solutions.html') 

	def about(request) -> object:
		return render(request, 'about.html')
	
	def post(request) -> object:
		data = {
			'posts': Post.objects.all()
		}
		return render(request, 'forum.html', data)

class PostCreate (CreateView):
	model = Post
	fields = ['author', 'content']
	template_name = 'create.html'
	def form_valid(self, form):
		form.save()
		return redirect('post forum')
