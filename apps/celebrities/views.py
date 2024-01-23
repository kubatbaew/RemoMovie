from django.views import generic

from apps.celebrities.models import Celebrity, Director


class CelebrityListView(generic.ListView):
    model = Celebrity
    template_name = 'pages/celebrities/celebritylist.html'

    def get_queryset(self):
        queryset = super().get_queryset()

        full_name = self.request.GET.get('full_name')
        if full_name:
            queryset = queryset.filter(full_name__icontains=full_name)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['directors'] = Director.objects.all()[:4]

        return context


class CelebrityDetailView(generic.DetailView):
    model = Celebrity
    pk_url_kwarg = 'pk'
    template_name = "pages/celebrities/celebritysingle.html"


class DirectorDetailView(generic.DetailView):
    model = Director
    template_name = 'pages/celebrities/directorsingle.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'celebrity'
