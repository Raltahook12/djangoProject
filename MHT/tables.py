import django_tables2 as tables
from .models import team,participant,membership,FullTable

class teamTable(tables.Table):
   class Meta():
       model = team
       template_name = "tables/bootstrap_htmx.html"

class participantTable(tables.Table):
    class Meta():
        model = participant
        template_name = "tables/bootstrap_htmx.html"

class membershipTable(tables.Table):
    class Meta():
        model = FullTable
        template_name = "tables/bootstrap_htmx.html"
