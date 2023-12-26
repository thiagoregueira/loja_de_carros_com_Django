# from django.shortcuts import redirect, render
from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# from django.views import View
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)


# CLASS GENERICS VIEW
class CarsListView(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        cars = super().get_queryset().order_by("model")
        search = self.request.GET.get("search")

        if search:
            cars = cars.filter(model__icontains=search)

        return cars


# CLASS GENERICS VIEW
class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"


# CLASS GENERICS VIEW
@method_decorator(
    login_required(login_url="login"), name="dispatch"
)  # só para quem estiver logado
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = "new_car.html"
    success_url = "/cars/"


# CLASS GENERICS VIEW
@method_decorator(
    login_required(login_url="login"), name="dispatch"
)  # também para quem estiver logado
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = "car_update.html"

    def get_success_url(self):
        return reverse_lazy("car_detail", kwargs={"pk": self.object.pk})


# CLASS GENERICS VIEW
@method_decorator(
    login_required(login_url="login"), name="dispatch"
)  # também para quem estiver logado
class CarDeleteView(DeleteView):
    model = Car
    template_name = "car_delete.html"
    success_url = "/cars/"


# FUNCTION BASED VIEW
# def cars_view(request):
#     search = request.GET.get("search")

#     if search:
#         cars = Car.objects.filter(model__icontains=search).order_by("model")
#     else:
#         cars = Car.objects.all().order_by("model")

#     return render(request, "cars.html", {"cars": cars})


# CLASS BASED VIEW (herda de View)
# class CarsView(View):
#     def get(self, request):
#         search = request.GET.get("search")

#         if search:
#             cars = Car.objects.filter(model__icontains=search).order_by("model")
#         else:
#             cars = Car.objects.all().order_by("model")

#         return render(request, "cars.html", {"cars": cars})


# FUNCTION BASED VIEW
# def new_car_view(request):
#     if request.method == "POST":
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect("cars_list")
#     else:
#         new_car_form = CarModelForm()

#     return render(request, "new_car.html", {"new_car_form": new_car_form})


# CLASS BASED VIEW (herda de View)
# class NewCarView(View):
#     def get(self, request):
#         new_car_form = CarModelForm()
#         return render(request, "new_car.html", {"new_car_form": new_car_form})

#     def post(self, request):
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect("cars_list")
#         return render(request, "new_car.html", {"new_car_form": new_car_form})
