from django.shortcuts import get_object_or_404,redirect,HttpResponse,render
from .models import Topic,Category,Comment,CarouselImage
from django.template import loader
from user.views import User
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def index(request):
    topics = Topic.objects.order_by('LastUpdate').reverse().all()
    categories = Category.objects.all()
    comments = Comment.objects.all()
    carouselFirst = CarouselImage.objects.first()
    carouselItems = CarouselImage.objects.all()

    carouselItems = carouselItems.exclude(id=carouselFirst.id)

    context = {
        'topics':topics,
        'categories':categories,
        'comments':comments,
        'carouselFirst':carouselFirst,
        'carouselItems':carouselItems,
    }

    return render(request,'pages/index.html',context)




@login_required
def createSubject(request):

    if request.method == 'POST':
        titlePrefix = request.POST['titlePrefix']
        title = request.POST['title']
        categoryName = request.POST['category']
        editor = request.POST['editor']

        category = Category.objects.get(name=categoryName)

        user = request.user.username

        topic = Topic(titlePrefix=titlePrefix,title=title,category=category,subject=editor,author=user)
        print('Konu Açıldı!')
        topic.save()
        return redirect("/")

    categories = Category.objects.all()

    context = {
        'categories':categories,
    }

    return render(request,'pages/newTopic.html',context)


def subjectDetails(request,slug):
    currentTopic = Topic.objects.get(slug=slug)
    comments = Comment.objects.filter(topic_id=currentTopic.id)
    topics = Topic.objects.order_by('LastUpdate').reverse()

    if request.method == 'POST':
        message = request.POST['editor']
        user = request.user

        comment = Comment(user=user,message=message,topic=currentTopic)
        
        comment.save()
        currentTopic.LastUpdate = datetime.now()
        currentTopic.save()
        return redirect("/konu/"+slug) 
    

    currentTopic.viewCounter += 1
    currentTopic.save()

    topics = Topic.objects.order_by('LastUpdate').reverse()
    template = loader.get_template('pages/subjectDetails.html')

    context = {
        'topic':currentTopic,
        'topics':topics,
        'comments':comments,
        'commentCounter':len(comments)
    }

    return HttpResponse(template.render(context, request))

def getCategory(request,slug):
    category = Category.objects.get(slug=slug)
    template = loader.get_template('pages/category.html')
    topics = Topic.objects.filter(category_id=category.id)

    context = {
        'category':category,
        'topics':topics,
    }

    return HttpResponse(template.render(context, request))

def search(request,q):
    topics = Topic.objects.all()


    return render(request,'pages/searchResult.html')

def userDetails(request,id):
    user = User.objects.get(id=id)

    context = {
        'user':user,
    }

    return render(request,'pages/userDetails.html',context)

