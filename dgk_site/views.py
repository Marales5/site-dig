from django.shortcuts import render, redirect


def redirect_blog(request):
    return redirect('goods_list_url', permanent=True)

# Create your views here.
