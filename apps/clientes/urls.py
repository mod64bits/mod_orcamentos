from django.urls import path
from .views import ClienteCreateView, ClienteListeView, ClienteDetailView, ClienteUpdateView


app_name = 'cliente'

urlpatterns = [
    path("", ClienteListeView.as_view(), name="cliente-list"),
    path("novo/", ClienteCreateView.as_view(), name="create-update"),
    path("update/<slug:slug>/", ClienteUpdateView.as_view(), name="client-update"),
    path("detalhe/<slug:slug>/", ClienteDetailView.as_view(), name="cliente-detail"),
]
