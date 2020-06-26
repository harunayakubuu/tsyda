from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, Http404
from .models import Category, Post, Tag
from .forms import CategoryForm, CategoryUpdateForm, PostForm, TagForm
from django.views.generic.edit import DeleteView
# Create your views here.

def posts(request):
    recent = Post.objects.order_by('-created')[:3]
    posts = Post.objects.filter(publish=True)    
    paginator = Paginator(posts, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        # 'posts': posts
        'recent': recent,
        'page_obj': page_obj
    }
    return render(request, 'frontend/blog/posts.html', context)

def post_detail(request, post, pk):
    post = get_object_or_404(
        Post,
        slug=post,
        id = pk
    )
    context = {
        'post': post
    }
    return render(request, 'frontend/blog/post-detail.html', context)



def admin_post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'backend/blog/post-list.html', context)

def admin_post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'backend/blog/post-detail-admin.html', context)

def post_create(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    
    # if not request.user.is_authenticated:
    #     raise Http404
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
    # if request.method == 'POST':
        if form.is_valid():
            # form.save()
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('/blog/post/list/')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'backend/blog/post-create.html', context)

def post_update(request, id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/blog/post/list/')
    context = {
        'form': form,
        'instance': instance
    }
    return render(request, 'backend/blog/post-update.html', context)

def post_delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/blog/post/list/')
    # return render(request, 'backend/blog/post-delete.html')


def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST or None)
        if form.is_valid:
            form.save()
            return redirect('/blog/category/list/')
    else:
        form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'backend/blog/category_add.html', context)

def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'backend/blog/category_list.html', context)

def category_update(request, id):
    instance = get_object_or_404(Category, id=id)
    form = CategoryUpdateForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/blog/category/list/')
    context = {
        'form': form,
        'instance': instance
    }
    return render(request, 'backend/blog/category_update.html', context)

def category_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('/blog/category/list/')



def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/blog/tag/list/')
    else:
        form = TagForm()
    context = {
        'form': form
    }
    return render(request, 'backend/blog/tag_add.html', context)

def tag_list(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags
    }
    return render(request, 'backend/blog/tag_list.html', context)

def tag_update(request, id=None):
    instance = get_object_or_404(Tag, id=id)
    form = TagForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/blog/tag/list/')
    context = {
        'form': form,
        'instance': instance
    }
    return render(request, 'backend/blog/tag_update.html', context)

class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'backend/blog/tag_delete.html'
# def tag_delete(request, id):
#     tag = Tag.objects.get(id=id)
#     tag.delete()
#     return redirect('/blog/tag/list/')