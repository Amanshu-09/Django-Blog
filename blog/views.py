from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
# class blogs(ListView):
#     model = Post
#     template_name = 'blogs.html'
#     ordering = ['-posted_on']

class blog_detail(DetailView):
    model = Post
    template_name = 'blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(blog_detail, self).get_context_data(*args, **kwargs)
        post = Post.objects.get(id=self.kwargs['pk'])
        total_likes = post.total_likes()
        context['total_likes'] = total_likes
        liked = False
        if post.likes.filter(id = self.request.user.id):
            liked = True
        context['liked'] = liked
        return context

class create_blog(CreateView):
    model = Post
    template_name = 'create_blog.html'
    form_class = PostForm

class edit_blog(UpdateView):
    model = Post
    template_name = 'update_blog.html'
    form_class = EditForm

class delete_blog(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('blogs')

def user_blogs(request):
    try:
        p = Paginator(Post.objects.filter(author=str(request.user.id)).order_by('-posted_on'), 3)
        page = request.GET.get('page')
        posts = p.get_page(page)
    except:
        posts = None
    return render(request, 'registration/user_blogs.html', {'posts':posts})

def like_post(request, pk):
    post = Post.objects.get(id=pk)
    if post.likes.filter(id = request.user.id):
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog_detail', args=(str(pk))))

def post_comment(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        commenter = User.objects.get(id=request.POST.get('commenter'))
        comment = request.POST.get('comment')

        rec = Comment(post=post, commenter=commenter, comment=comment)
        rec.save()
    return HttpResponseRedirect(reverse('blog_detail', args=(str(pk))))

def post_reply(request, pi,ci):
    if request.method == 'POST':
        parent_comment = Comment.objects.get(id=ci)
        replier = User.objects.get(id=request.POST.get('replier'))
        reply = request.POST.get('reply')

        rec = Reply(parent_comment=parent_comment, replier=replier, reply=reply)
        rec.save()
    return HttpResponseRedirect(reverse('blog_detail', args=(str(pi))))

def search(request):
    if request.method == 'POST':
        searched_item = request.POST.get('searched-item')
        posts = Post.objects.filter(Q(title__contains=searched_item) | Q(body__contains=searched_item) | Q(category__contains=searched_item)).order_by('-posted_on')
        return render(request, 'search.html', {'posts':posts, 'searched':'You Searched For : '+searched_item})
    return render(request, 'search.html', {'searched':'Try to search from searchbar !'})

def category(request, cat):
        posts = Post.objects.filter(category__contains=cat).order_by('-posted_on')
        return render(request, 'category.html', {'posts':posts, 'category':cat})

def blogs(request):
    p = Paginator(Post.objects.all().order_by('-posted_on'), 3)
    page = request.GET.get('page')
    blogs = p.get_page(page)

    return render(request, 'blogs.html', {'blogs':blogs})