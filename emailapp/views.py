from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def home(request):
    return render(request, 'emailtemplate.html')


def send_email(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        uemail = request.POST.get('uemail')
        html_content = render_to_string(
            'emailtemplate.html', {"username": uname})

        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            'testing', text_content, settings.EMAIL_HOST_USER, [uemail])
        email.attach_alternative(html_content, 'text/html')
        email.send()
        return render(request, 'email.html', {'username': 'send an email'})
    else:
        return render(request, 'email.html')
