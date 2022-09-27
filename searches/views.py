from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from .search import search, get_skills
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, FormView
from searches.models import Search, Profile

# Create your views here.


class SearchGet(LoginRequiredMixin, ListView):
    model = Search
    template_name = "search_list.html"


def SearchPost(request):
    data = request.POST
    q = data.get("q")
    s = Search(title=q, author=request.user)
    s.save()
    data = search(q)
    for item in data:
        s.profile_set.create(
            name=item["login"],
            avatar_url=item["avatar_url"],
            html_url=item["html_url"],
            url=item["url"],
            repos_url=item["repos_url"],
            skills="",
        )
    response = redirect(reverse("search_item", kwargs={"pk": s.id}))
    return response


class SearchListView(LoginRequiredMixin, ListView):
    def get(self, request, *args, **kwargs):
        view = SearchGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = SearchPost
        return view(request, *args, **kwargs)


def searchItemView(request, pk):
    s = Search.objects.get(id=pk)
    return render(
        request,
        "search_detail.html",
        {"profiles": s.profile_set.all(), "search": s, "star": False},
    )


class ProfileGet(DetailView):
    model = Profile
    template_name = "profile_detail.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["skills"] = str(self.get_object().skills).split(" ")
        return context


def profilePost(request, pk):
    data = request.POST
    p = Profile.objects.get(id=pk)
    p.comment_set.create(comment=data.get("c"))
    return redirect(reverse("profile_detail", kwargs={"pk": pk}))


class ProfileDetailView(LoginRequiredMixin, DetailView):  # new
    def get(self, request, *args, **kwargs):
        view = ProfileGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = profilePost
        return view(request, *args, **kwargs)


def profileDelete(request, pk):
    p = Profile.objects.get(id=pk)
    p.delete()
    return redirect(reverse("home"))


def profileStar(request, pk):
    p = Profile.objects.get(id=pk)
    p.star = not (p.star)
    p.save()
    return redirect(reverse("profile_detail", kwargs={"pk": pk}))


def profileSkills(request, pk):
    p = Profile.objects.get(id=pk)
    p.skills = get_skills(p.repos_url)
    p.got_skills = True
    p.save()
    return redirect(reverse("profile_detail", kwargs={"pk": pk}))


def profileStarX(request, pid, sid):
    p = Profile.objects.get(id=pid)
    p.star = not (p.star)
    p.save()
    return redirect(reverse("search_item", kwargs={"pk": sid}))


def searchDelete(request, sid):
    s = Search.objects.get(id=sid)
    s.delete()
    return redirect(reverse("home"))


def searchStar(request, sid):
    s = Search.objects.get(id=sid)
    return render(
        request,
        "search_detail.html",
        {"profiles": s.profile_set.all(), "search": s, "star": True},
    )
