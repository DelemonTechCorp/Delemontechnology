from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def privacy(request):
    return render(request, 'main/privacy.html')

def terms(request):
    return render(request, 'main/terms.html')

def contact(request):
    return render(request, 'main/contact.html')

def services(request):
    return render(request, 'main/services.html')

def careers(request):
    return render(request, 'main/careers.html')

def digital(request):
    return render(request, 'main/digital.html')

def web(request):
    return render(request, 'main/web.html')

def team(request):
    return render(request, 'main/team.html')

def mobile(request):
    return render(request, 'main/mobile.html')

def ecommerce(request):
    return render(request, 'main/ecommerce.html')

def uiux(request):
    return render(request, 'main/uiux.html')

def animation(request):
    return render(request, 'main/animation.html')

def projects(request):
    return render(request, 'main/projects.html')

def luxuryacres(request):
    return render(request, 'main/luxuryacres.html')

def chronocorp(request):
    return render(request, 'main/chronocorp.html')

def ppc(request):
    return render(request, 'main/ppc.html')

def seo(request):
    return render(request, 'main/seo.html')

def content(request):
    return render(request, 'main/content.html')

def social(request):
    return render(request, 'main/social.html')

def whoweare(request):
    return render(request, 'main/whoweare.html')

def realestate(request):
    return render(request, 'main/realestate.html')