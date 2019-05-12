from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from .forms import PaidForm
from .models import Profile


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            context['is_paid_access'] = profile.is_paid_access
            return self.render_to_response(context)


class PaidView(FormView):
    template_name = 'subscribe-paid.html'
    form_class = PaidForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        access = Profile.objects.get(user=self.request.user)
        access.is_paid_access = True
        access.save()
        return super().form_valid(form)


def show_articles(request):
    return render(
        request,
        'articles.html'
    )


def show_article(request, id):
    return render(
        request,
        'article.html'
    )
