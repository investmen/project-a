from django.urls import path

from project_b.users.views import (
    user_list_view,
    user_redirect_view,
    user_update_view,
    cuser_update_view,
    euser_update_view,
    buser_update_view,
    user_detail_view,
)

app_name = "users"
urlpatterns = [
    path("", view=user_list_view, name="list"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("~cupdate/", view=cuser_update_view, name="cupdate"),
    path("~eupdate/", view=euser_update_view, name="eupdate"),
    path("~bupdate/", view=buser_update_view, name="bupdate"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
