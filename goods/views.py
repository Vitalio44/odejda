from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Goods, Category
from pars import func1


def main_page(request):
    category_item = Category.objects.all()
    context = {"category_item": category_item}
    return render(request, "index.html", context)


def update_data(request):
    if not request.user.is_authenticated():
        raise Http404
    return render(request, "update.html")


def get_update_data(request):
    if not request.user.is_authenticated():
        raise Http404
    func1()
    return HttpResponseRedirect(reverse('main'))


def category(request, slug):
    category_item = get_object_or_404(Category, slug=slug)
    category_goods = Goods.objects.filter(goods_category=category_item)
    paginator = Paginator(category_goods, 20)  # Show 20 goods item
    page = request.GET.get('page')
    try:
        category_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        category_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        category_page = paginator.page(paginator.num_pages)
    context = {
        "category_item": category_item,
        "category_page": category_page
    }
    return render(request, "category.html", context)
