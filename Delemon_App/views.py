from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.core.paginator import Paginator
import logging
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'main/home.html')

def robots_txt(request):
    robots_content = """
    User-agent: *
    Disallow: /admin/
    Allow: /
    Sitemap: https://www.delemontechnology.com/sitemap.xml
    """
    return HttpResponse(robots_content, content_type="text/plain")

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

# def team(request):
#     team_members = TeamModel.objects.all()

#     return render(request, 'main/team.html', {'team_members': team_members})

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

def pps(request):
    return render(request, 'main/podcastp.html')

def sem(request):
    return render(request, 'main/sem.html')

def content(request):
    return render(request, 'main/content.html')

def social(request):
    return render(request, 'main/social.html')

def whoweare(request):
    return render(request, 'main/whoweare.html')

def realestate(request):
    return render(request, 'main/realestate.html')
def homenew(request):
    return render(request, 'main/Homenew.html')


def landingservice(request):
    return render(request, 'main/landingservice.html')

def blog(request):
    blogs = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/blog.html', {'page_obj': page_obj,'blogs':blogs})

logger = logging.getLogger(__name__)

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    latest_blogs = Blog.objects.order_by('-created_at')[:4]
    news_items = News.objects.filter(is_published=True).order_by('-published_date')
    related_news_items = news_items.exclude(id=news.id)[:3]

    if request.method == 'POST':
        # Collect form data
        name = request.POST.get('customername')
        mobile = request.POST.get('phone')
        email = request.POST.get('email')
        service = request.POST.get('service')
        company = request.POST.get('company', '')  # Default to an empty string if not provided

        # Validate form data
        if not all([name, mobile, email, service]):
            messages.error(request, "All fields are required.")
        else:
            try:
                # Save the contact request
                ContactRequest.objects.create(
                    name=name,
                    mobile=mobile,
                    email=email,
                    company=company,  # Optional
                    service=service
                )
                messages.success(request, "Your contact request has been submitted successfully.")
                return redirect('news_detail', slug=slug)
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")

    return render(request, 'main/news_detail.html', {
        'news': news,
        'related_news_items': related_news_items,
        'latest_blogs': latest_blogs,
    })


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    related_blogs = Blog.objects.exclude(id=blog.id)[:4]

    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        company = request.POST.get('company')
        service = request.POST.get('services')

        # Create the contact request
        ContactRequest.objects.create(
            name=name,
            mobile=mobile,
            email=email,
            company=company,
            service=service
        )

        # Send a thank-you email
        send_mail(
            subject='Thank You for Contacting Us',
            message=(
                f"Hi {name},\n\n"
                "Thank you for reaching out to us. We have received your contact request and "
                "will get back to you shortly.\n\n"
                "Best regards,\nDelemon Technology"
            ),
            from_email='sales@delemontechnology.com',  # Replace with your email
            recipient_list=[email],
            fail_silently=False,  # Set to True to suppress errors during email sending
        )

        # Display success message and redirect
        messages.success(request, "Your contact request has been submitted successfully.")
        return redirect('blog_detail', slug=slug)

    return render(request, 'main/blog_detail.html', {'blog': blog, 'related_blogs': related_blogs})







from django.db.models import Case, When, Value, IntegerField
from .models import TeamModel

# def team(request):
#     # Define the updated required order of designations
#     order = [
#         'Developer',
#         'Graphic Designer',
#         'Video Editer',
#         'Content Writer',
#         'Digital Marketing',
#         'Admin',
#         'Sales Executive'
#     ]

#     # Ordering logic using Case and When to enforce custom ordering
#     ordering = Case(
#         *[When(designation=role, then=Value(index)) for index, role in enumerate(order)],
#         output_field=IntegerField()
#     )

#     # Get all team members and order them based on the custom order
#     teams = TeamModel.objects.all().order_by(ordering)

#     # Filter by designation individually to pass separately to the template
#     graphic = teams.filter(designation='Graphic Designer')
#     digital = teams.filter(designation='Digital Marketing')
#     devop = teams.filter(designation='Developer')
#     video = teams.filter(designation='Video Editer')
#     content = teams.filter(designation='Content Writer')
#     admin = teams.filter(designation='Admin')
#     sales = teams.filter(designation='Sales Executive')

#     # Prepare the context dictionary
#     context = {
#         'teams': teams,
#         'graphic': graphic,
#         'digital': digital,
#         'devop': devop,
#         'video': video,
#         'content': content,
#         'admin': admin,
#         'sales': sales,
#     }

#     return render(request, 'main/team.html', context)

from django.db.models import Case, When, Value, IntegerField
from django.shortcuts import render
from .models import TeamModel

def team(request):
    # Define the required order of designations
    order = [
        'Developer',
        'Graphic Designer',
        'Video Editer',
        'Content Writer',
        'Digital Marketing',
        'Admin',
        'Sales Executive'
    ]

    # Ordering logic using Case and When to enforce custom ordering
    ordering = Case(
        *[When(designation=role, then=Value(index)) for index, role in enumerate(order)],
        output_field=IntegerField()
    )

    # Define default company contact details
    default_contact = {
        'phone': '+971503482299',
        'whatsapp': '+971503482299',
        'instagram': 'delemon_technology',
        'linkdln': 'https://www.linkedin.com/company/delemon-technology',
        'mail': 'sales@delemontechnology.com'
    }

    # Get all team members and order them based on the custom order
    teams = TeamModel.objects.all().order_by(ordering)

    # Assign default values if contact details are missing
    for member in teams:
        member.phone = member.phone or default_contact['phone']
        member.whatsapp = member.whatsapp or default_contact['whatsapp']
        member.instagram = member.instagram or default_contact['instagram']
        member.linkdln = member.linkdln or default_contact['linkdln']
        member.mail = member.mail or default_contact['mail']

    # Filter by designation individually to pass separately to the template
    graphic = teams.filter(designation='Graphic Designer')
    digital = teams.filter(designation='Digital Marketing')
    devop = teams.filter(designation='Developer')
    video = teams.filter(designation='Video Editer')
    content = teams.filter(designation='Content Writer')
    admin = teams.filter(designation='Admin')
    sales = teams.filter(designation='Sales Executive')

    # Prepare the context dictionary
    context = {
        'teams': teams,
        'graphic': graphic,
        'digital': digital,
        'devop': devop,
        'video': video,
        'content': content,
        'admin': admin,
        'sales': sales,
    }

    return render(request, 'main/team.html', context)


def news_list(request):
    """
    View to display a list of published news articles with pagination.
    """
    # Fetch all published news ordered by published_date (newest first)
    news_items = News.objects.filter(is_published=True).order_by('-published_date')

    # Paginate the results (6 news per page)
    paginator = Paginator(news_items, 6)
    page_number = request.GET.get('page')  # Get the page number from the query parameter
    page_obj = paginator.get_page(page_number)  # Get the appropriate page object

    context = {
        'page_obj': page_obj,  # Pass the paginated object to the template
    }
    return render(request, 'main/news.html', context)



def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    latest_blogs = Blog.objects.order_by('-created_at')[:4]
    news_items = News.objects.filter(is_published=True).order_by('-published_date')
    related_news_items = news_items.exclude(id=news.id)[:3]

    if request.method == 'POST':
        # Collect form data
        name = request.POST.get('customername')
        mobile = request.POST.get('phone')
        email = request.POST.get('email')
        service = request.POST.get('service')

        # Validate form data
        if not all([name, mobile, email, service]):
            messages.error(request, "All fields are required.")
        else:
            try:
                # Save the contact request
                ContactRequest.objects.create(
                    name=name,
                    mobile=mobile,
                    email=email,
                    company="",  # Optional if not in the form
                    service=service
                )

                send_mail(
                    subject='Thank You for Contacting Us',
                    message=(
                        f"Hi {name},\n\n"
                        "Thank you for reaching out to us. We have received your contact request and "
                        "will get back to you shortly.\n\n"
                        "Best regards,\nDelemon Technology"
                    ),
                    from_email='sales@delemontechnology.com',  # Replace with your email
                    recipient_list=[email],
                    fail_silently=False,  # Set to True to suppress errors during email sending
        )
                messages.success(request, "Your contact request has been submitted successfully.")
                return redirect('news_detail', slug=slug)
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")

    return render(request, 'main/news_detail.html', {
        'news': news,
        'related_news_items': related_news_items,
        'latest_blogs': latest_blogs,
    })






from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from .models import Blog, News


def sitemap(request):
    # Define the base domain
    base_url = request.build_absolute_uri('/')[:-1].strip('/')

    # Define static pages with priorities
    static_pages = [
        {'loc': reverse('home'), 'priority': '1.0'},
        {'loc': reverse('about'), 'priority': '0.8'},
        {'loc': reverse('privacy'), 'priority': '0.8'},
        {'loc': reverse('terms'), 'priority': '0.8'},
        {'loc': reverse('contact'), 'priority': '0.9'},
        {'loc': reverse('services'), 'priority': '0.9'},
        {'loc': reverse('careers'), 'priority': '0.7'},
        {'loc': reverse('digital'), 'priority': '0.7'},
        {'loc': reverse('web'), 'priority': '0.7'},
        {'loc': reverse('mobile'), 'priority': '0.7'},
        {'loc': reverse('ecommerce'), 'priority': '0.7'},
        {'loc': reverse('uiux'), 'priority': '0.7'},
        {'loc': reverse('animation'), 'priority': '0.7'},
        {'loc': reverse('projects'), 'priority': '0.7'},
        {'loc': reverse('luxuryacres'), 'priority': '0.7'},
        {'loc': reverse('chronocorp'), 'priority': '0.7'},
        {'loc': reverse('ppc'), 'priority': '0.7'},
        {'loc': reverse('seo'), 'priority': '0.7'},
        {'loc': reverse('content'), 'priority': '0.7'},
        {'loc': reverse('social'), 'priority': '0.7'},
        {'loc': reverse('realestate'), 'priority': '0.7'},
        {'loc': reverse('whoweare'), 'priority': '0.7'},
        {'loc': reverse('team'), 'priority': '0.7'},
        {'loc': reverse('blog'), 'priority': '0.8'},
        {'loc': reverse('news_list'), 'priority': '0.8'},
    ]

    # Fetch dynamic pages from the database
    blogs = Blog.objects.filter(created_at__lte=timezone.now())
    news = News.objects.filter(is_published=True, published_date__lte=timezone.now())

    # Build the XML structure
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    # Add static pages
    for page in static_pages:
        xml_content += "  <url>\n"
        xml_content += f"    <loc>{base_url}{page['loc']}</loc>\n"
        xml_content += f"    <priority>{page['priority']}</priority>\n"
        xml_content += "  </url>\n"

    # Add dynamic blog pages
    for blog in blogs:
        xml_content += "  <url>\n"
        xml_content += f"    <loc>{base_url}{blog.get_absolute_url()}</loc>\n"
        xml_content += "    <priority>1.0</priority>\n"
        xml_content += "  </url>\n"

    # Add dynamic news pages
    for article in news:
        xml_content += "  <url>\n"
        xml_content += f"    <loc>{base_url}{reverse('news_detail', kwargs={'slug': article.slug})}</loc>\n"
        xml_content += "    <priority>1.0</priority>\n"
        xml_content += "  </url>\n"

    # Close the XML structure
    xml_content += '</urlset>'

    return HttpResponse(xml_content, content_type='application/xml')



