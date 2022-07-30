from django.shortcuts import redirect
from django.views.generic import CreateView

from webapp.forms import AnswerForm, Answer
from webapp.models import Poll


class CreateAnswers(CreateView):
    form_class = AnswerForm
    template_name = "answers/answers.html"
    model = Answer

    def form_valid(self, form):
        self.pk = form.save()
        return super().form_valid(form)

    def get_redirect_url(self):
        return redirect("PollView", pk=self.poll.pk)
