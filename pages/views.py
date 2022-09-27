from django.shortcuts import render
from searches.models import Search, Profile
from django.views.generic import TemplateView, ListView

# Create your views here.


class HomePageView(ListView):
    model = Search
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["search_list"] = Search.objects.filter(
                author=self.request.user
            ).order_by("-date")
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"
