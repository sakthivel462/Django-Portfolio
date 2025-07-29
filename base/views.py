from django.shortcuts import render
from django.http import HttpResponse
from . models import Project
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.
def home(request):
    project = Project.objects.all()
    context = {'project':project}
    return render(request, 'base/index.html', context)
def post(request, pk):
    post = Project.objects.get(id=pk)
    context= {'post':post}
    return render(request, 'base/post.html',context)

def sendEmail(request):
    if request.method == 'POST':
    
        template = render_to_string('base/email_template.html', {
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
            })
        
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,['sakthivelrajasekar2503@gmail'])
        email.fail_silently=False
        email.send()
        
    return  render(request, 'base/send_email.html')