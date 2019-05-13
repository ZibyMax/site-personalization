from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView, TemplateView
# from django.views.generic.base import TemplateView
from .forms import PaidForm
from .models import Profile, Article


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            context['user_is_paid_access'] = profile.is_paid_access
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


# def show_articles(request):
#     return render(
#         request,
#         'articles.html'
#     )


class ArticleListView(ListView):
    template_name = 'articles.html'
    model = Article
    ordering = ['title']

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data()
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user=self.request.user)
            context['is_paid_access'] = profile.is_paid_access
        else:
            context['is_paid_access'] = False
        return context


# def show_article(request, id):
#     return render(
#         request,
#         'article.html'
#     )


class ArticleView(DetailView):
    template_name = 'article.html'
    model = Article

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleView, self).get_context_data()
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user=self.request.user)
            context['user_is_paid_access'] = profile.is_paid_access
        else:
            context['user_is_paid_access'] = False
        return context
