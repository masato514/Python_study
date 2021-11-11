from django.shortcuts import render

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import InquiryForm, PlayCreateForm

from django.urls import reverse_lazy

from .models import Play

from django.contrib import messages

import logging

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('kadai_app:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class PlayListView(LoginRequiredMixin, generic.ListView):
    model = Play
    template_name = 'play_list.html'
    paginate_by = 2

    def get_queryset(self):
        plays = Play.objects.filter(user = self.request.user).order_by('-created_at')
        return plays

class PlayDetailView(LoginRequiredMixin,generic.DetailView):
    model = Play
    template_name = 'play_detail.html'



class PlayCreateView(LoginRequiredMixin, generic.CreateView):
    model = Play
    template_name = 'play_create.html'
    form_class = PlayCreateForm
    success_url = reverse_lazy('kadai_app:play_list')

    def form_valid(self, form):
        kadai_app = form.save(commit = False)
        kadai_app.user = self.request.user
        kadai_app.save()
        messages.success(self.request, 'リストを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "リストの作成に失敗しました。")
        return super().form_invalid(form)

class PlayUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Play
    template_name = 'play_update.html'
    form_class = PlayCreateForm

    def get_success_url(self):
        return reverse_lazy('kadai_app:play_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'リストを更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "リストの更新に失敗しました。")
        return super().form_invalid(form)

class PlayDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Play
    template_name = 'play_delete.html'
    success_url = reverse_lazy('kadai_app:play_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "リストを削除しました。")
        return super().delete(request, *args, **kwargs)