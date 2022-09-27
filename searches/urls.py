# articles/urls.py
from django.urls import path
from .views import (
    SearchListView,
    searchItemView,
    ProfileDetailView,
    profileDelete,
    profileStar,
    profileSkills,
    profileStarX,
    searchDelete,
    searchStar,
)

urlpatterns = [
    path("", SearchListView.as_view(), name="search_list"),
    path("<int:pk>/", searchItemView, name="search_item"),
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/delete/<int:pk>/", profileDelete, name="profile_delete"),
    path("profile/star/<int:pk>/", profileStar, name="profile_star"),
    path("profile/skill/<int:pk>/", profileSkills, name="profile_skill"),
    path("profile/star/<int:pid>/<int:sid>/", profileStarX, name="profile_starX"),
    path("delete/<int:sid>/", searchDelete, name="search_delete"),
    path("star/<int:sid>/", searchStar, name="search_star"),
]
