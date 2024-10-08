from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Athlete
from django.core.cache import cache

def athlete_list(request):
    athletes = Athlete.objects.all().order_by('id')

    # Paginate the results (10 athletes per page)
    paginator = Paginator(athletes, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    
    cache_keys = {f'athlete_{obj.id}': obj for obj in page_obj.object_list}
    cache_timeout = 30
    
    # Set the cache values with the specified timeout if not set
    if not cache.get_many(cache_keys.keys()):
        cache.set_many(cache_keys, timeout=cache_timeout) 
    
    cached_athletes = cache.get_many(cache_keys.keys())
    athletes_list = [cached_athletes[key] for key in cache_keys.keys()]
    return render(request, 'Athletes/athletesDetails.html', {'athletes': athletes_list, 'page_obj': page_obj})


def athlete_list_country(request, country=None):
    # Get the search query from the GET parameter
    search_query = request.GET.get('country')

    # If no search query is provided, default to 'China'
    selected_country = search_query if search_query else 'China'
    selected_country_lower = selected_country.lower()

    # Filter athletes by the selected country (case-insensitive)
    athletes = Athlete.objects.filter(country__iexact=selected_country_lower).order_by('id')
    distinct_countries = Athlete.objects.values_list('country', flat=True).distinct()

    # Paginate the results (10 athletes per page)
    paginator = Paginator(athletes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    cache_keys = {f'athlete_{obj.id}': obj for obj in page_obj.object_list}
    cache_timeout = 30
    
    # Set the cache values with the specified timeout if not set
    if not cache.get_many(cache_keys.keys()):
        cache.set_many(cache_keys, timeout=cache_timeout) 
    
    cached_athletes = cache.get_many(cache_keys.keys())
    athletes_list = [cached_athletes[key] for key in cache_keys.keys()]

    return render(request, 'Athletes/countryDetails.html', {
        'athletes': athletes_list,
        'page_obj': page_obj,
        'distinct_countries': distinct_countries,
    })
        
def home(request):
    return render(request, 'Athletes/index.html', {"Country":"China"})