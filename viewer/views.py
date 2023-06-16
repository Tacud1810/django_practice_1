'''
modul with view functions for viewer app
'''

from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView

from viewer.models import MyUser


# Create your views here.
def home(request):
    """ render for home page"""
    return render(request, template_name="home.html")


# def users(request):
# 	users_list = MyUser.objects.all()
# 	context = {"users": users_list}
# 	return render(request, template_name='users.html', context=context)


class UsersView(TemplateView):
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = MyUser.objects.all()
        return context


def user(request, pk):
    person = MyUser.objects.get(id=pk)
    # email = MyUser.objects.get(user=email)
    context = {"person": person}
    return render(request, template_name="user.html", context=context)


class PersonForm(ModelForm):
    class Meta:
        model = MyUser
        fields = "__all__"


class PersonCreateView(CreateView):
    template_name = "add_user.html"
    form_class = PersonForm
    success_url = reverse_lazy("users")

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.get_success_url())


class PersonUpdateView(UpdateView):
    template_name = "update_user.html"
    model = MyUser
    form_class = PersonForm
    success_url = reverse_lazy("users")

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.get_success_url())
