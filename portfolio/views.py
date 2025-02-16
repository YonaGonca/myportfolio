from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils import translation
from django.shortcuts import redirect


# Create your views here.
def index(request):
    lang_code = request.session.get(translation.LANGUAGE_SESSION_KEY)
    if lang_code:
        translation.activate(lang_code)
    else:
        translation.activate('es') 
    return render(request, 'index.html')

def projects(request):
    lang_code = request.session.get(translation.LANGUAGE_SESSION_KEY)
    if lang_code:
        translation.activate(lang_code)
    else:
        translation.activate('es') 
    return render(request, 'projects.html')

def aboutme(request):
    lang_code = request.session.get(translation.LANGUAGE_SESSION_KEY)
    if lang_code:
        translation.activate(lang_code)
    else:
        translation.activate('es') 
    return render(request, 'aboutme.html')

def change_language(request, lang_code):
    translation.activate(lang_code)  
    request.session[translation.LANGUAGE_SESSION_KEY] = lang_code  
    return redirect(request.META.get('HTTP_REFERER', '/')) 
