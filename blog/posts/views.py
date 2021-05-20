from django.shortcuts import render
from .models import Post
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def PostList(request):
    post_list = Post.objects.all()
    print("post list")
    print(post_list)
    return render (request,"index.html",{"post_list":post_list})


def PostDetail(request,post_id):
    post = Post.objects.filter(id = post_id).first()
    title = post.title
    created_on = post.created_on
    author = post.author
    content = post.content
    return render (request,"post_detail.html",{"post":post,"title":title,"created_on":created_on,"author":author,"content":content})




# @login_required(redirect_field_name='login_user')
def PostCreate(request):
        if not request.user.is_authenticated:
            return redirect('/')
        else:
            if request.method=='POST':
                title = request.POST['title']
                content = request.POST['content']
                author = request.user.username
                print(author)
                post = Post.objects.create(title = title ,content = content,author = author)
                post.save()
                return redirect('/list')
            else:
                return render(request, 'create.html')