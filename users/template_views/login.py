from django.views.generic import TemplateView

from users.forms import LoginForm


class LoginView(TemplateView):
    template_name = "auth/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LoginForm()
        return context