from django.utils.text import slugify
from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.urls import reverse
import re
from ckeditor.fields import RichTextField   # simple CKEditor



class Keyword(models.Model):
    word = models.CharField(max_length=100, unique=True, verbose_name="Keyword")
    url = models.URLField(max_length=500, verbose_name="URL")

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = "Keyword"
        verbose_name_plural = "Keywords"


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True,max_length=500)
    image = models.ImageField(upload_to='blogs/')
    author_image = models.ImageField(upload_to='authors/')
    content = RichTextField()
    author_name = models.CharField(max_length=100)
    author_social_links = models.JSONField(default=dict)
    seo_Title = models.CharField(max_length=255,null=True)
    seo_Description = models.TextField(null=True)
    references = models.JSONField(default=list, blank=True, help_text="List of references in the format [{'title': '...', 'url': '...'}]")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # def replace_keywords_with_links(self, description):
    #     """
    #     Replace keywords in the description with hyperlinks to their respective URLs.
    #     """
    #     keywords = Keyword.objects.all()
    #     for keyword in keywords:
           
    #         pattern = rf'(?<!>)\b{re.escape(keyword.word)}\b'  
    #         description = re.sub(
    #             pattern,
    #             f'<a href="{keyword.url}" target="_blank">{keyword.word}</a>',
    #             description,
    #             flags=re.IGNORECASE 
    #         )
    #     return description

    # def formatted_description(self):
    #     """
    #     Convert the description with hyperlinks and markdown-style headers for rendering.
    #     """
    #     text = self.content

 
    #     text = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    #     text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    #     text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    #     text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)

    #     text = re.sub(r'^\* (.+)$', r'<li>\1</li>', text, flags=re.MULTILINE)

    #     if '<li>' in text:
    #         text = f"<ul>{text}</ul>"

    #     text = self.replace_keywords_with_links(text)

   
    #     return mark_safe(text)

    # formatted_description.short_description = 'Description (with links)'

    # def get_absolute_url(self):
    #     return reverse('blogview', kwargs={'id': self.id})

    
    def formatted_description(self):
        """
        Convert the description with hyperlinks and markdown-style headers for rendering.
        """
        text = self.content

        # Replace markdown-style headers with HTML headers
        text = re.sub(r'^##### (.+)$', r'<h5>\1</h5>', text, flags=re.MULTILINE)
        text = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
        text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
        text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
        text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)

        # Replace bullet points

        # Replace keywords with links
        # text = self.replace_keywords_with_links(text)

        # Mark the ffeninal text as safe HTML for rendering
        return mark_safe(text)

    formatted_description.short_description = 'Description (with links)'
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})




class TeamModel(models.Model):
    name=models.CharField(max_length=200)
    POST_CHOICES = [
        ('Graphic Designer', 'Graphic Designer'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Developer', 'Developer'),
        ('Video Editer', 'Video Editer'),
        ('Content Writer', 'Content Writer'),
        ('Sales Executive', 'Sales Executive'),
        ('Admin', 'Admin'),
    ]
    designation=models.CharField(max_length=200,choices=POST_CHOICES)
    profileimage=models.ImageField(upload_to='images')
    phone = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    linkdln = models.CharField(max_length=255, blank=True, null=True)
    mail = models.CharField(max_length=255, blank=True, null=True)
    specalization = models.CharField(max_length=300, blank=True, null=True)
    post = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)


    def _str_(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True,max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def replace_keywords_with_links(self, description):
        """
        Replace keywords in the description with hyperlinks to their respective URLs.
        """
        keywords = Keyword.objects.all()
        for keyword in keywords:
            # Regex ensures whole word matching and avoids HTML tag replacements
            pattern = rf'(?<!>)\b{re.escape(keyword.word)}\b'
            description = re.sub(
                pattern,
                f'<a href="{keyword.url}" target="_blank">{keyword.word}</a>',
                description,
                flags=re.IGNORECASE
            )
        return description

    def formatted_content(self):
        """
        Convert content with hyperlinks, markdown-style headers, and list formatting for rendering.
        """
        text = self.content

        # Replace markdown-style headers with HTML headers
        text = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
        text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
        text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
        text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)

        # Replace bullet points
        text = re.sub(r'^\* (.+)$', r'<li>\1</li>', text, flags=re.MULTILINE)

        # Wrap list items in <ul> if they exist
        if '<li>' in text:
            text = f"<ul>{text}</ul>"

        # Replace keywords with hyperlinks
        text = self.replace_keywords_with_links(text)

        # Mark the final text as safe HTML
        return mark_safe(text)

    formatted_content.short_description = 'Formatted Content'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

class ContactRequest(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    company = models.CharField(max_length=255, blank=True, null=True)
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact Request from {self.name}"