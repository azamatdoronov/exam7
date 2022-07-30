from django.shortcuts import redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic import ListView

from webapp.forms import PollForm
from webapp.models import Poll


class IndexView(ListView):
    model = Poll
    template_name = "polls/index.html"
    context_object_name = "polls"
    ordering = "-created_p"
    paginate_by = 5


class PollView(DetailView):
    template_name = "polls/poll_view.html"
    model = Poll


class CreatePoll(CreateView):
    form_class = PollForm
    template_name = "polls/create.html"

    def form_valid(self, form):
        poll = form.save(commit=False)
        poll.save()
        return redirect("PollView", pk=poll.pk)


class UpdatePoll(UpdateView):
    model = Poll
    template_name = 'polls/update.html'
    form_class = PollForm
    context_object_name = 'poll'


class DeletePoll(DeleteView):
    model = Poll
    template_name = "polls/delete.html"
    success_url = reverse_lazy('index')
