from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils import translation
from django.shortcuts import redirect
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.
def obtain_dark_mode(request):
    dark_mode = request.COOKIES.get('darkMode')
    return dark_mode

def obtain_language(request):
    language = request.COOKIES.get('language')
    return language

def index(request):
    lang_code = request.session.get(translation.LANGUAGE_SESSION_KEY)
    dark_mode = obtain_dark_mode(request)

    if lang_code:
        translation.activate(lang_code)
    else:
        translation.activate('es') 
    return render(request, 'index.html', {'dark_mode': dark_mode})

def projects(request):
    lang_code = request.session.get(translation.LANGUAGE_SESSION_KEY)
    dark_mode = obtain_dark_mode(request)

    if lang_code:
        translation.activate(lang_code)
    else:
        translation.activate('es') 
    return render(request, 'projects.html', {'dark_mode': dark_mode})

def aboutme(request):
    lang_code = request.session.get(translation.LANGUAGE_SESSION_KEY)
    dark_mode = obtain_dark_mode(request)
    language = obtain_language(request)
    
    if lang_code:
        translation.activate(lang_code)
    else:
        translation.activate('es') 
    return render(request, 'aboutme.html', {'dark_mode': dark_mode, 'language': language})

def change_language(request, lang_code):
    translation.activate(lang_code)  
    request.session[translation.LANGUAGE_SESSION_KEY] = lang_code  
    return redirect(request.META.get('HTTP_REFERER', '/')) 

from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = f"Portfolio New Contact Message from {name}"
            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            send_mail(
                subject,
                full_message,
                email, 
                ["ygoncalves5a@gmail.com"], 
            )

            return redirect(request.META.get("HTTP_REFERER", "/"))

    else:
        form = ContactForm()

    return redirect("/#contact")

