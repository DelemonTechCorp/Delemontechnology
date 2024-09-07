from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.home, name='home'),
    path('privacy', views.privacy, name='privacy'),
    path('terms', views.terms, name='terms'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('digital', views.digital, name='digital'),
    path('web', views.web, name='web'),
    path('services', views.services, name='services'),
    path('mobile', views.mobile, name='mobile'),
    path('ecommerce', views.ecommerce, name='ecommerce'),
    path('uiux', views.uiux, name='uiux'),
    path('animation', views.animation, name='animation'),
    path('projects', views.projects, name='projects'),
    path('luxuryacres', views.luxuryacres, name='luxuryacres'),
    path('chronocorp', views.chronocorp, name='chronocorp'),
    path('ppc', views.ppc, name='ppc'),
    path('seo', views.seo, name='seo'),
    path('careers', views.careers, name='careers'),
    path('team', views.team, name='team'),
    path('whoweare', views.whoweare, name='whoweare'),
    path('content', views.content, name='content'),
    path('social', views.social, name='social'),
    path('realestate', views.realestate, name='realestate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
