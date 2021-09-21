from django.contrib.auth import get_user_model
from django.conf import settings
from monitoring.models import Post, Tag, Product, Manufacturer, Comment
import django_filters
from django import forms


User = get_user_model()
# User = settings.AUTH_USER_MODEL


class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr="icontains")
    year_joined = django_filters.NumberFilter(
        field_name="date_joined", lookup_expr="year"
    )
    year_joined__gt = django_filters.NumberFilter(
        field_name="date_joined", lookup_expr="year__gt"
    )
    year_joined__lt = django_filters.NumberFilter(
        field_name="date_joined", lookup_expr="year__lt"
    )

    class Meta:
        model = User
        fields = [
            "username",
            "last_name",
        ]


class TagFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Tag
        fields = ["name"]


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")  # 이거 설정하면 '/' 검색도 가능
    content = django_filters.CharFilter(lookup_expr="icontains")  #
    tag_set = django_filters.ModelChoiceFilter(queryset=Tag.objects.all())
    # tag_set = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple))

    class Meta:
        model = Post
        fields = ["tag_set"]


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            "price": ["lt", "gt"],
            "release_date": ["exact", "year__gt"],
        }
