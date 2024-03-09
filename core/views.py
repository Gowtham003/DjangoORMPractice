from django.shortcuts import render
from .forms import RatingForm, RestaurantForm
from .models import Rating, Restaurant, Sale
from django.db.models import Sum, Avg, Prefetch
from django.utils import timezone
from datetime import timedelta

def index(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'index.html', {'form': form})
    context = {'form': RestaurantForm()}
    return render(request, 'index.html', context)

def test(request):
    month_ago = timezone.now() - timedelta(days=1)
    last_month_sales = Prefetch('sales', queryset=Sale.objects.filter(datetime__gte=month_ago))
    restaurants = Restaurant.objects.prefetch_related('ratings', last_month_sales)
    restaurants = restaurants.annotate(total_income=Sum('sales__income'))
    context = {'restaurants': restaurants}
    # ratings = Rating.objects.only('rating', 'user__username', 'restaurant__name').filter(rating__gte=3).select_related('restaurant', 'user')
    # context = {'ratings': ratings}
    return render(request, 'test.html', context)