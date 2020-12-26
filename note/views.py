from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

from note.forms import EmailPostForm
from note.models import Note


class AllNote(View):
    def get(self, request):
        context = {}
        all_notes = Note.objects.all()
        paginator = Paginator(all_notes, 30)
        page = request.GET.get('page')
        try:
            notes = paginator.page(page)
        except PageNotAnInteger:
            notes = paginator.page(1)
        except EmptyPage:
            notes = paginator.page(paginator.num_pages)
        context['all_notes'] = all_notes
        context['page'] = page
        context['notes'] = notes
        return render(request, "index.html", context)

def note_detail(request, slug):
    note = get_object_or_404(Note, slug=slug)
    return render(request, 'detail.html', {'note': note})

def note_share(request, slug):
    note = get_object_or_404(Note, slug=slug)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            note_url = request.build_absolute_uri(note.get_absolute_url())
            subject = f"Вам направлено напоминание от {cd['name']} - {note.title} ({note.text})"
            message = f"Ознакомиться с заметкой можно по ссылке {note_url}"
            send_mail(subject, message, 'e.orechovich92@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'share.html', {'note': note, 'form': form, 'sent': sent})