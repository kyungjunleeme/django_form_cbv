from django.urls import path
from django_filters import filterset
from monitoring.filters import PostFilter, ProductFilter, UserFilter, TagFilter
from monitoring import views
from django_filters.views import FilterView


app_name = "monitoring"  # URL Reverse에서 namespace역할을 하게 됨

urlpatterns = [
    path(
        "search/",
        FilterView.as_view(
            filterset_class=UserFilter, template_name="monitoring/user_list.html"
        ),
        name="search",
    ),
    path(
        "tag_search/",
        FilterView.as_view(
            filterset_class=TagFilter, template_name="monitoring/tag_list.html"
        ),
        name="tag_search",
    ),
    path(
        "post_search/",
        FilterView.as_view(
            filterset_class=PostFilter, template_name="monitoring/post_list.html"
        ),
        name="post_search",
    ),
    path("product_search/", views.product_search, name="product_search"),
]
