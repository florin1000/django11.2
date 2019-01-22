import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from .models import RestaurantLocation


# Create your views here.
def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {"restaurants_list": queryset}
    return render(request, template_name, context)


class HomeView(TemplateView):
    template_name = 'home.html'

    # maybe a new way to update the context
    # https://reinout.vanrees.org/weblog/2014/05/19/context.html

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        surnames = ["JOhn", "Emil"]
        context.update({"surnames": surnames})
        print(context)
        return context
