import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.

User =  get_user_model()


class Category(models.Model):
    title   = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title





class Post(models.Model):
    id  = models.UUIDField(primary_key = True, default=uuid.uuid4, editable = False)
    author          = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    title           = models.CharField(max_length=100)
    slug            = models.SlugField(max_length=250, unique=True)
    categories      = models.ManyToManyField(Category)
    tags            = models.ManyToManyField(Tag)
    picture         = models.ImageField(null=True, blank=True, upload_to="blog/posts/%day/%month/%year")
    description     = models.TextField(help_text="Kindly provide a brief description of the items for the right owner to provide the detailed")
    previous_post   = models.ForeignKey('self', related_name = 'previous', on_delete = models.SET_NULL, blank = True, null = True)
    next_post       = models.ForeignKey('self', related_name = 'next', on_delete = models.SET_NULL, blank = True, null = True)
    publish         = models.BooleanField(default=False, help_text="Check this box for your post to be published.")
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    view_count      = models.IntegerField(default = 0)
    comment_count   = models.IntegerField(default = 0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.slug), self.id])

    @property
    def get_comment_counts(self):
        return self.comment_count
    
    @property
    def get_view_counts(self):
        return self.view_count


def create_slug(instance, new_slug = None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_reciever, sender=Post)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # email = models.EmailField(max_length = 75)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.user
        # return 'Comment by {} on {}'.format(self.name, self.post)