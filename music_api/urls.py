from django.urls import path
from .views import MusicList, MusicDetail, index, SongCreate, add_song_form,\
    register_request, login_request, logout_request

urlpatterns = [
    path("", index, name="index"),
    path("api/v1/music/", MusicList.as_view(), name="music_list_api"),
    path("api/v1/music/<int:pk>/", MusicDetail.as_view(), name="music_detail"),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name="logout"),
    path("add-song-form", SongCreate.as_view(), name="add_song_form"),
]
