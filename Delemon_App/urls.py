from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.home, name='home'),
     path('homenew', views.homenew, name='homenew'),
    path('landingservice', views.landingservice, name='landingservice'),
    path('privacy-policy-digital-services', views.privacy, name='privacy'),
    path('terms-and-conditions-digital-marketing', views.terms, name='terms'),
    path('contact-digital-experts', views.contact, name='contact'),
    path('about-digital-technology', views.about, name='about'),
    path('digital-marketing-and-advertising-services', views.digital, name='digital'),
    path('web-development-and-design-solutions', views.web, name='web'),
    path('full-digital-services', views.services, name='services'),
    path('mobile-app-development-services', views.mobile, name='mobile'),
    path('ecommerce-development-solutions', views.ecommerce, name='ecommerce'),
    path('ui-ux-design-for-better-experience', views.uiux, name='uiux'),
    path('animation-design-and-services', views.animation, name='animation'),
    path('digital-project-portfolio', views.projects, name='projects'),
    path('luxury-acres-digital-project', views.luxuryacres, name='luxuryacres'),
    path('chrono-corp-innovative-solutions', views.chronocorp, name='chronocorp'),
    path('ppc-advertising-management-services', views.ppc, name='ppc'),
    path('pps-production-services', views.pps, name='pps'),
    path('seo-optimization-and-services', views.seo, name='seo'),
    path('sem-marketing-and-services', views.sem, name='sem'),
    path('digital-career-opportunities', views.careers, name='careers'),
    path('our-expert-digital-team', views.team, name='team'),
    path('who-we-are-digital-experts', views.whoweare, name='whoweare'),
    path('content-marketing-strategy-services', views.content, name='content'),
    path('social-media-marketing-strategies', views.social, name='social'),
    path('real-estate-digital-listings', views.realestate, name='realestate'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    # path('teams', views.teams, name='teams'),
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
     path('sitemap.xml', views.sitemap, name='sitemap'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
