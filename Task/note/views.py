from django.shortcuts import render
from rest_framework import generics
from .models import Note
from django.core.paginator import Paginator
from .serializers import NoteSerializer

class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note
    serializer_class = NoteSerializer


def listing(request):
    Note_list = Note.objects.all()
    paginator = Paginator(Note_list ) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "list.html", {"page_obj": page_obj})