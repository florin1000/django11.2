import random
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestaurantLocation


# Create your views here.
def restaurant_listview(request):
    template_name = 'restaurants/Restaurant_location.html'
    queryset = RestaurantLocation.objects.all()
    context = {"restaurants_list": queryset}
    return render(request, template_name, context)


class RestaurantListView(ListView):
    template_name = 'restaurants/Restaurant_location.html'

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        print(self.kwargs)
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact="tarte") |
                Q(category__icontains="tarte")
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    template_name = 'restaurants/Restaurant_details.html'
    queryset = RestaurantLocation.objects.all()

    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(RestaurantLocation,
                                category=rest_id)  # pk=rest_id, it can be used any field instead of category
        return obj


class HomeView(TemplateView):
    template_name = 'home.html'

    # maybe a new way to update the context
    # https://reinout.vanrees.org/weblog/2014/05/19/context.html
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        surnames = ["John", "Emil"]
        context.update({"surnames": surnames})
        print(context)
        return context
