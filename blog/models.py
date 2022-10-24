# blog/models.py
from django.conf import settings
from django.db import models


class Post(models.Model):
    """
    Represents a blog post
    """
    DRAFT = 'draft'
    PUBLISHED = 'published'
    BIRDS = 'birds'
    GAMES = 'games'
    RAP_MUSIC = 'rap music'
    NONSENSE = 'nonsense'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]
    TOPIC_CHOICES = [
        (BIRDS, 'Birds'),
        (RAP_MUSIC, 'Rap Music'),
        (GAMES, "Games"),
        (NONSENSE, 'Nonsense')
    ]
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        null=True,
        unique_for_date='published',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='blog_posts',
        null=True,
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible',
    )
    content = models.TextField()
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date & time this article was published'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    prepopulated_fields = {'slug': ('title',)}

    slug = models.SlugField(
        null=False,
        unique_for_date='published',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='blog_posts',
        null=False,
    )
    topic = models.CharField(
        max_length=10,
        choices=TOPIC_CHOICES,
        default=title,
        help_text='The topics that are discussed in the post',
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
