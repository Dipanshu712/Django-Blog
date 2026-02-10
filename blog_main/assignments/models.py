from django.db import models

class About(models.Model):
    about_heading = models.CharField(max_length=25)
    about_description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_heading


class SocialLink(models.Model):
    PLATFORM_CHOICES = (
        ("facebook", "Facebook"),
        ("instagram", "Instagram"),
        ("linkedin", "LinkedIn"),
        ("twitter", "Twitter / X"),
        ("github", "GitHub"),
        ("youtube", "YouTube"),
    )

    platform = models.CharField(
        max_length=25,
        choices=PLATFORM_CHOICES,
        unique=True
    )
    link = models.URLField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def icon_class(self):
        return f"fa-brands fa-{self.platform}"


