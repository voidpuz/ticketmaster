from django.views.generic import DetailView

from users.models import User


class ProfileView(DetailView):
    queryset = User.objects.filter(is_active=True, is_confirmed=True)
    template_name = "auth/profile.html"
    context_object_name = "user"