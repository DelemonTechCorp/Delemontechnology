from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
class TeamModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation','post', 'profileimage_display')
    list_filter = ('designation',)
    search_fields = ('name', 'designation')

    def profileimage_display(self, obj):
        if obj.profileimage:
            return obj.profileimage.url
        return "No Image"
    profileimage_display.short_description = 'Profile Image'

admin.site.register(TeamModel, TeamModelAdmin)

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('word', 'url')  # Display keyword and URL in the admin list view
    search_fields = ('word',)  # Enable search by keyword
    ordering = ('word',)  # Order keywords alphabetically


# News Admin
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'is_published')  # Display these fields in the list view
    list_filter = ('is_published', 'published_date')  # Add filters for "is_published" and "published_date"
    search_fields = ('title', 'content')  # Enable search functionality for title and content
    prepopulated_fields = {'slug': ('title',)}  # Auto-populate slug from title
    readonly_fields = ('formatted_content',)  # Display formatted content as a readonly field
    fields = ('title', 'slug', 'content', 'image', 'is_published', 'published_date', 'formatted_content')
    ordering = ('-published_date',)  # Order by newest articles first

    def formatted_content(self, obj):
        """
        Display the formatted content (preview with links and HTML formatting) in the admin panel.
        """
        return obj.formatted_content()

    formatted_content.short_description = "Formatted Content (Preview)"

class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'company', 'service', 'created_at')

admin.site.register(ContactRequest, ContactRequestAdmin)