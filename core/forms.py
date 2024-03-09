from django.forms import ModelForm
from .models import Rating, Restaurant

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ('user', 'restaurant', 'rating', )

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        # fields = ('name', 'restaurant_type', 'website', 'date_opened', 'latitude', 'longitude')
        fields = "__all__"