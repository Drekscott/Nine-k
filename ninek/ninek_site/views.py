from django.shortcuts import render
from .models import About, Page, Category
# Create your views here.
def about(request):

    cont_dict = About.objects.all()

    return render(request,'ninek_site/about.html', cont_dict)
def index(request):

    category_list = Category.objects.order_by('-views')[:3]
    context_dict = {'categories': category_list}

    return render(request, 'ninek_site/index.html', context_dict)

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
