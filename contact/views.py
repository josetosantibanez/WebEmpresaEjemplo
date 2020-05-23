from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForms

# Create your views here.

def contact(request):
    contact_form = ContactForms()

                                                
    if request.method == "POST":
        contact_form = ContactForms(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Todo fue bien, enviamos correo y redireccionamos
            email = EmailMessage(
                "La caffetiera: Nuevo mensaje de contacto",#asunto
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),#cuerpo
                "no-contestar@inbox.mailtrap.io",#email_origen
                ["xerigazon1997@gmail.com"],#email_destino
                reply_to=[email]#reply_to=[email]
                )
            try:                                            
                email.send()
                #Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                #Todo ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")

    return render(request,'contact/contact.html',{'form':contact_form})