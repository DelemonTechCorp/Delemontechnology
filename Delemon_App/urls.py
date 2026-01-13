from django.urls import path
from .import views
from django.views.generic import RedirectView


urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.home, name='home'),
    path('robots', views.robots_txt, name="robots_txt"),
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
    path('ios-app-development-services', views.iphone, name='ios'),
    path('android-app-development-services', views.android, name='android'),
    path('flutter-app-development-services', views.flutter, name='flutter'),    
    path('ecommerce-development-solutions', views.ecommerce, name='ecommerce'),
    path('react-development-solutions',views.react,name='react'),
    path('ui-ux-design-for-better-experience', views.uiux, name='uiux'),
    path('animation-design-and-services', views.animation, name='animation'),
    path('clinical', views.clinical, name='clinical'),
    path('product-design',views.product_design,name='product_design'),
    path('print-design',views.print_design,name='print_design'),
    path('graphic-design',views.graphic_design,name='graphic'),    
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
    
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    # path('teams', views.teams, name='teams'),
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('sitemap.xml', views.sitemap, name='sitemap'),
    
    # ------------- REDIRECTED VIEWS----------------- #
    path('advertising-and-media-buying', RedirectView.as_view(url='/advertising-for-better-experience', permanent=True), name='advertising_and_media_buying_redirect'),
    path('advertising-for-better-experience', views.advertising, name='advertising'),  
    
    path('angular-development', RedirectView.as_view(url='/angular-development-solutions', permanent=True), name='angular_development_redirect'),
    path('angular-development-solutions', views.angular, name='angular'),
    
    path('blockchain-development', RedirectView.as_view(url='/blockchain-development-solutions', permanent=True), name='blockchain_development_redirect'),
    path('blockchain-development-solutions', views.blockchain, name='blockchain'),
    
    path('branding-and-identity', RedirectView.as_view(url='/branding-for-better-experience', permanent=True), name='branding_and_identity_redirect'),
    path('branding-for-better-experience', views.branding, name='branding'),
    
    path('custom-software-development', RedirectView.as_view(url='/customeweb-development-solutions', permanent=True), name='custom_software_development_redirect'),
    path('customeweb-development-solutions', views.customeweb, name='customeweb'),
    
    path('digital-design-services', RedirectView.as_view(url='/digital-design', permanent=True), name='digital_design_services_redirect'),
    path('digital-design', views.digital_design, name='digital_design'),
    
    path('dotnet-development', RedirectView.as_view(url='/dotnet-development-solutions', permanent=True), name='dotnet_development_redirect'),
    path('dotnet-development-solutions', views.dotnet, name='dotnet'),
    
    path('email-marketing', RedirectView.as_view(url='/email-marketing-services', permanent=True), name='email_marketing_redirect'),
    path('email-marketing-services', views.email, name='email'),
    
    path('influencer-marketing', RedirectView.as_view(url='/influencer-marketing-services', permanent=True), name='influencer_marketing_redirect'),
    path('influencer-marketing-services', views.influencer, name='influencer'),
    
    path('java-development', RedirectView.as_view(url='/java-development-solutions', permanent=True), name='java_development_redirect'),
    path('java-development-solutions', views.java, name='java'),

    path('logo-design-services', RedirectView.as_view(url='/logo-design', permanent=True), name='logo_design_services_redirect'),
    path('logo-design', views.logo_design, name='logo_design'),
    
    path('magento-development-services', RedirectView.as_view(url='/magento-development-solutions', permanent=True), name='magento_development_services_redirect'),
    path('magento-development-solutions', views.magento, name='magento'),
    
    path('market-research', RedirectView.as_view(url='/research-marketing-services', permanent=True), name='market_research_redirect'),
    path('research-marketing-services', views.research, name='research'),
    
    path('nodejs-development', RedirectView.as_view(url='/nodejs-development-solutions', permanent=True), name='nodejs_development_redirect'),
    path('nodejs-development-solutions', views.nodejs, name='nodejs'),
    
    path('php-development', RedirectView.as_view(url='/php-development-solutions', permanent=True), name='php_development_redirect'),
    path('php-development-solutions', views.php, name='php'),

    path('python-development', RedirectView.as_view(url='/python-development-solutions', permanent=True), name='python_development_redirect'),
    path('python-development-solutions', views.python, name='python'),
    
    path('react-development-solutions', RedirectView.as_view(url='/react-development', permanent=True), name='react_redirect'),
    path('react-development', views.react, name='react'),
    
    path('shopify-development-services', RedirectView.as_view(url='/shopify-development-solutions', permanent=True), name='shopify_redirect'),
    path('shopify-development-solutions', views.shopify, name='shopify'),
    
    path('software-testing-qa', RedirectView.as_view(url='/softwaretesting-development-solutions', permanent=True), name='softwaretesting_redirect'),
    path('softwaretesting-development-solutions', views.softwaretesting, name='softwaretesting'),
    
    path('woocommerce-development-services', RedirectView.as_view(url='/woocommerce-development-solutions', permanent=True), name='woocommerce_redirect'),
    path('woocommerce-development-solutions', views.woocommerce, name='woocommerce'),
    
    path('wordpress-development-services', RedirectView.as_view(url='/wordpress-development-solutions', permanent=True), name='wordpress_redirect'),
    path('wordpress-development-solutions', views.wordpress, name='wordpress'),
    
    path('blog/', RedirectView.as_view(url='/technology-blog/', permanent=True), name='blog_redirect'),
    path('technology-blog/', views.blog, name='blog'),


]

