from django.views.generic import TemplateView

from users.forms import UserCreationForm


class RegisterView(TemplateView):
    template_name = "auth/register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = UserCreationForm()
        return context