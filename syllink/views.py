from django.shortcuts import redirect, render
from django.views import generic

from .forms import SyllabusUploaderForm


class IndexView(generic.ListView):
    template_name = "syllink/index.html"

    def get_queryset(self):
        """Return the last five published questions."""
        return None

def upload_file(request):
    if request.method == 'POST':
        form = SyllabusUploaderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = SyllabusUploaderForm()
    return render(request, 'syllink/upload_file.html', {
        'form': form
    })