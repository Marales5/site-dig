from random import randint

from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy

from .utils import *
from .forms import *
from django.core.paginator import Paginator
from django.db.models import Q


def goods_list(request):
    ################ For searching ########################
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()
    ##############################################
    paginator = Paginator(posts, 5)

    page_num = request.GET.get('page', 1)
    page = paginator.get_page(page_num)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    context = {
        'posts': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    # return render(request, 'digital_site/index.html', context={'posts': posts})
    return render(request, 'digital_site/index.html', context=context)


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'digital_site/tags_list.html', context={'tags': tags})


def digital_list(request):
    goods = Digital.objects.all()
    unit_digital = randint(1, 5)
    obj = Digital.objects.get(id=unit_digital)
    return render(request, 'digital_site/index2.html',
                  context={'goods': goods, 'unit_digital': unit_digital, 'obj': obj})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'digital_site/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'digital_site/post_create_form.html'


class PostUpdate(ObjectUpdateMixit, View):
    model = Post
    model_form = PostForm
    template = 'digital_site/post_update_form.html'


class PostDelete(ObjDeleteMixin, View):
    model = Post
    template = 'digital_site/post_delete_form.html'
    redirect_url = 'post_list_url'


# def tags_list(request):
#     tags = Tag.objects.all()
#     return render(request, 'digital_site/tags_list.html', context={'tags': tags})

class TagUpdate(ObjectUpdateMixit, View):
    model = Tag
    model_form = TagForm
    template = 'digital_site/tag_update_form.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'digital_site/tag_create.html'


class TagDelete(ObjDeleteMixin, View):
    model = Tag
    template = 'digital_site/tag_delete_form.html'
    redirect_url = 'tags_list_url'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'digital_site/tag_detail.html'


def advertisement(request):
    n = "my thinks"
    return render(request, 'digital_site/advertisement.html', context={'post': n})


################ Any Model #####################################

class GoodsView(View):
    def get(self, request):
        goods = Digital.objects.all()
        unit_digital = randint(1, 5)
        obj = Digital.objects.get(id=unit_digital)
        return render(request, "digital_site/index2.html", {"goods_list": goods, 'obj': obj})


class GoodsDetail(ObjectDetailMixin, View):
    model = Digital
    template = 'digital_site/single_product.html'

class MyLoginUserView(LoginView):
    template_name = 'digital_site/login.html'
    form_class = AuthentificateForm
    success_url = reverse_lazy('goods_list_url')

    def get_success_url(self):
        return self.success_url