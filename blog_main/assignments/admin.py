from django.contrib import admin
from .models import About, SocialLink
# Register your models here.


# add button remove code 
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False

admin.site.register(About,AboutAdmin)


from django.contrib import admin
from .models import SocialLink

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("platform", "link", "created_at")
