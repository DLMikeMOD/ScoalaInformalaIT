from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app1.models import Location

class LocationsView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'app1/locations_index.html'
    paginate_by = 5
    queryset = model.objects.filter(active=1)
    context_object_name = 'locations'

    def get_context_data(self, *args, **kwargs):
        data = super(LocationsView, self).get_context_data(*args, **kwargs)
        # data['locations'] = self.model.objects.filter(active=1)
        return data

class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Location
    # fields = '__all__'
    fields = ['city', 'country']
    template_name = 'app1/location_form.html'

    def get_success_url(self):
        return reverse('locations:lista_locati')

class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'app1/location_form.html'

    def get_success_url(self):
        return reverse('app1/location:lista_locati')

@login_required
def delete_location(request, pk):
    Location.objects.filter(id=pk).update(active=0)
    return redirect('locations:lista_locati')


class LocationInactiveView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'app1/locations_index.html'
    paginate_by = 5
    queryset = model.objects.filter(active=0)
    context_object_name = 'locations'

    def get_context_data(self, *args, **kwargs):
        data = super(LocationInactiveView, self).get_context_data(*args, **kwargs)
        # data['locations'] = self.model.objects.filter(active=0)
        return data

@login_required
def activate_location(request, pk):
    Location.objects.filter(id=pk).update(active=1)
    return redirect('locations:lista_locatii')