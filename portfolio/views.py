from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils import translation
from django.shortcuts import redirect


# Create your views here.
def obtain_dark_mode(request):
    dark_mode = request.COOKIES.get('darkMode')
    return dark_mode

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
    
    if lang_code:
        translation.activate(lang_code)
    else:
        translation.activate('es') 
    return render(request, 'aboutme.html', {'dark_mode': dark_mode})

def change_language(request, lang_code):
    translation.activate(lang_code)  
    request.session[translation.LANGUAGE_SESSION_KEY] = lang_code  
    return redirect(request.META.get('HTTP_REFERER', '/')) 
