from django.contrib import admin
from .models import Clientes


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('documento', 'whatsApp', 'tipo_cliente', 'usuario', 'created', 'bloqueado')
    list_filter = ('bloqueado', 'created', 'tipo_cliente',)
    search_fields = ('whatsApp', 'documento',)
    list_per_page = 50
    date_hierarchy = 'created'
    actions = ('set_bloqueado',)

    fieldsets = [
        (
            "Usuario Cadastrado",
            {
                "fields": ["usuario"],
                "description": "Selecione ou cadastre um usuario para ser proprietario desse cliente"
            },
        ),
        (
            None,
            {
                "fields": ["tipo_cliente", "documento", "whatsApp"],
            },
        ),
        (
            "Bloquear Cliente",
            {
                "classes": ["collapse"],
                "fields": ["bloqueado"],
            }
        ),
    ]

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ('-created', 'bloqueado',)
        return ('-created',)

    def set_bloqueado(self, request, queryset):
        cont = queryset.update(bloqueado=True)
        self.message_user(request, "{} Clientes Bloqueados com sucesso!".format(cont))

    set_bloqueado.short_description = "Marque os clientes para bloquear"


admin.site.register(Clientes, ClienteAdmin)
