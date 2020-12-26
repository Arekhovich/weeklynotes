from django.contrib import admin
from django.urls import path, include
from note.views import AllNote, note_share, note_detail

urlpatterns = [

    path("note_detail/<str:slug>/", note_detail, name="note-detail"),
    path('share/<str:slug>/', note_share, name='note-share'),
    path("", AllNote.as_view(), name="the-main-page"),
]