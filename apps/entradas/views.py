from django.shortcuts import render
from django.views.generic import (ListView, CreateView, DeleteView,
                                    UpdateView, DetailView)
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Records, Comments
from .forms import CreateRecordForm, CommentsForm

# Create your views here.

class index_views(ListView):
    model = Records
    paginate_by = 2
    context_object_name = 'record_users'
    template_name = 'entradas/index.html'

class up_Record_views(LoginRequiredMixin, CreateView):
    model = Records
    form_class = CreateRecordForm
    template_name = 'entradas/up_record.html'
    success_url = reverse_lazy('entradas:index')

    #Receive file and asigned user
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            Record = form.save(commit=False)
            Record.author = User.objects.get(username=request.user)
            Record.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class Record_views(DetailView):
    model = Records
    template_name = 'entradas/view_record.html'
    form_class = CommentsForm

    def get_context_data(self, **kwargs):
        context =super(Record_views, self).get_context_data(**kwargs)
        sumaVistas = context['object']
        sumaVistas.views += 1
        sumaVistas.save()
        if 'form' not in context:
            context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            slug = kwargs['slug']
            comentario = form.save(commit=False)
            comentario.author = User.objects.get(username=request.user)
            comentario.recordOwn = self.model.objects.get(slug=slug)
            comentario.save()
        return HttpResponseRedirect(comentario.recordOwn.get_absolute_url())

class Record_edit_views(LoginRequiredMixin, UpdateView):
    model = Records
    form_class = CreateRecordForm
    template_name = 'entradas/edit_record.html'

    def get_success_url(self):
    # if you are passing 'pk' from 'urls'
    # capture that 'pk' and pass it to 'reverse_lazy()' function
    #send this slug because edit the title else send slug = self.kwargs['slug']
        slug=self.object.slug
        return reverse_lazy('entradas:record_view', kwargs={'slug': slug })
