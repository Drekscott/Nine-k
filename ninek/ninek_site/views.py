from django.shortcuts import render
from .models import About, Page, Category, Media
# Create your views here.
def about(request):

    cont_dict = About.objects.all()

    return render(request,'ninek_site/about.html', cont_dict)
def index(request):


    context_dict = {}
    page_list = Page.objects.all().order_by('category', 'likes')[:5]
    category_list = Category.objects.order_by('-views')[:5]
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    media = Media.objects.all()
    context_dict['medias'] = media
    return render(request, 'ninek_site/index.html', context_dict)

def get_cat_list():
    category_list = Category.objects.all()
    context_dict['categories'] = category_list
    return render('ninek/category_list.html', context_dict)

def category(request, category_name_slug):
    context_dict = {}

    try:

        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name


        pages = Page.objects.filter(category=category)


        context_dict['pages'] = pages

        context_dict['category'] = category
    except Category.DoesNotExist:

        pass


    return render(request, 'ninek_site/category.html', context_dict)

def page(request, page_name_slug):
    context_dict = {}

    try:

        page = Page.objects.get(slug=page_name_slug)
        context_dict['page_title'] = page.title
        categories = Category.objects.filter(page=page)
        context_dict['page'] = page
    except Page.DoesNotExist:
        pass
    return render(request, 'ninek_site/page.html', context_dict)

def media(request):
    context = {}
    media = Media.objects.all()
    context['medias'] = media
    return render(request, 'ninek_site/media.html', context)
