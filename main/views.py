import random

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from . import models

# Create your views here.


def home_view(request):
    products_ = models.Product.objects.all()

    ch1 = random.choice(products_)
    ch2 = random.choice(products_)
    while ch1 == ch2:
        ch2 = random.choice(products_)
    ch3 = random.choice(products_)
    while ch1 == ch2 or ch2 == ch3:
        ch3 = random.choice(products_)

    rates = models.Rates.objects.all()[0]

    return render(request, 'home.html', {
        'c1': ch1,
        'c2': ch2,
        'c3': ch3,
        'td2': rates.goldRate,
        'td3': rates.silverRate,
        'td4': rates.date_added,
    })


def product_list(request, category_slug=None):
    category = None
    categories = models.Category.objects.all()
    products = models.Product.objects.active()
    if category_slug:
        category = get_object_or_404(models.Category, slug=category_slug)
        products = products.filter(category=category)
        paginator = Paginator(products, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {
        'category': category,
        'categories': categories,
        'page_obj': page_obj,
    })


def product_detail(request, id, slug):
    product = get_object_or_404(models.Product, id=id, slug=slug, active=True)

    return render(request, 'detail.html', {'product': product, })


class PdfDownloadView(generic.ListView):
    model = models.CatalogPdf
    fields = ['pdf']
    template_name = 'catolog.html'


def pdf_view(request, slug):
    pdf = get_object_or_404(models.CatalogPdf, slug=slug)
    data = open(pdf.pdf.path, "rb").read()
    return HttpResponse(data, content_type="application/pdf")


class SearchView(generic.ListView):
    model = models.Product
    template_name = 'search.html'
    context_object_name = 'search_result'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            result = models.Product.objects.filter(name=query)
        else:
            result = None
        return result
