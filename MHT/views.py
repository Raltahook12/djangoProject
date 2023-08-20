from django.views.generic import ListView
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ToDoItem

from django_tables2 import SingleTableMixin,MultiTableMixin
from django_filters.views import FilterView

from .models import team,participant,membership,teamMentor
from .tables import teamTable,participantTable,membershipTable
from .filters import pacticFilter

class pacticHTMxTableView(SingleTableMixin, FilterView):
    table_class = membershipTable
    queryset = membership.objects.select_related('team','participant')
    filterset_class = pacticFilter
    paginate_by = 25

    def get_template_names(self):
        if self.request.htmx:
            template_name = "pactic_table_partial.html"
        else:
            template_name = "pactic_table_htmx.html"
        return template_name
class MyLoginView(LoginView):
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('tasks')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

def userLogout(request):
    logout(request)
    return HttpResponseRedirect("login/")

class AllToDos(ListView):
    model = ToDoItem
    template_name = "MHT/home.html"