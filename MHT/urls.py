from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.AllToDos.as_view(), name='home'),
    path('login/', views.LoginView.as_view(),name='login'),
    path('pactic_table_htmlx/',views.pacticHTMxTableView.as_view(),name = 'pacticTable'),
]
