from django.contrib.auth import get_user_model
from django.shortcuts import render
from monitoring.filters import ProductFilter, UserFilter, TagFilter, PostFilter
from monitoring.models import Post, Comment, Product, Tag

User = get_user_model()
# AttributeError: 'str' object has no attribute '_meta' (settings.AUTH_USER_MODEL)


# def search(request):
#     user_list = User.objects.all()
#     user_filter = UserFilter(request.GET, queryset=user_list)
#     return render(request, "monitoring/user_list.html", {"filter": user_filter})


# def tag_search(request):
#     tag_list = Tag.objects.all()
#     tag_filter = TagFilter(request.GET, queryset=tag_list)
#     return render(request, "monitoring/tag_list.html", {"filter": tag_filter})


def post_search(request):
    post_list = Post.objects.all()
    post_filter = TagFilter(request.GET, queryset=post_list)
    return render(request, "monitoring/post_list.html", {"filter": post_filter})


def product_search(request):
    product_list = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product_list)
    return render(request, "monitoring/product_list.html", {"filter": product_filter})
