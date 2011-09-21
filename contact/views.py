# -*- coding: utf8 -*-
from django.shortcuts import render_to_response 
from mtaro.contact.forms import ContactForm 
def contact(request): 
    #if request.method == 'POST': 
        form = ContactForm(request.POST) 
        if form.is_valid(): 
            cd = form.cleaned_data 
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('e-mail', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/') 
        else:
            form = ContactForm(
                initial={'subject': "Мне нравится сайт)"}			
			)
            return render_to_response('contact/contact_form.html', {'form': form}) 