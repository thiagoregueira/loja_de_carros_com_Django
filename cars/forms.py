from django import forms
from cars.models import Car

# Modo Manual
# class CarForm(forms.Form):
#     model = forms.CharField(max_length=200)
#     brand = forms.ModelChoiceField(Brand.objects.all().order_by("name"))
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     value = forms.FloatField()
#     photo = forms.ImageField()

#     def save(self):
#         car = Car(
#             model=self.cleaned_data["model"],
#             brand=self.cleaned_data["brand"],
#             factory_year=self.cleaned_data["factory_year"],
#             model_year=self.cleaned_data["model_year"],
#             plate=self.cleaned_data["plate"],
#             value=self.cleaned_data["value"],
#             photo=self.cleaned_data["photo"],
#         )
#         car.save()
#         return car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    def clean_value(self):
        value = self.cleaned_data["value"]
        if value < 10000:
            self.add_error(
                "value", "Não aceitamos carros com valores abaixo de R$ 10.000."
            )
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data["factory_year"]
        if factory_year < 1970:
            self.add_error(
                "factory_year", "Só aceitamos carros com fabricação a partir de 1970."
            )
        return factory_year
