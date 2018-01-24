from django.shortcuts import render, redirect, HttpResponse

def index(request):
	return render(request, 'surveys/index.html')

def process(request):		#handle the form and sessions
		try:
			request.session['count']+=1
		except KeyError:
			request.session['count']=1

		request.session['name']=request.POST['name']
		request.session['location']=request.POST['location']
		request.session['language']=request.POST['language']
		request.session['comment']=request.POST['comment']
		return redirect('/result')
		# return HttpResponse('hello')

def result(request):
	return render(request, 'surveys/result.html')

def reset(request):
	if 'count' in request.session:
		del request.session['count']
	return redirect('/')
# Create your views here.
