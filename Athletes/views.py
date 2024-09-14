from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Athlete

def athlete_list(request):
    athletes = Athlete.objects.all()
    paginator = Paginator(athletes, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Athletes/athletesDetails.html', {'athletes': page_obj.object_list, 'page_obj': page_obj})

def athlete_list_country(request, country=None):
    # If no country is passed, default to 'China'
    selected_country = country if country else 'China'

    # Filter athletes by the selected country
    athletes = Athlete.objects.filter(country=selected_country).order_by('id')

    # Retrieve distinct countries for the dropdown
    distinct_countries = Athlete.objects.values_list('country', flat=True).distinct()

    # Paginate the results (10 athletes per page)
    paginator = Paginator(athletes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Render the template with the filtered athletes and distinct countries
    return render(request, 'Athletes/countryDetails.html', {
        'athletes': page_obj.object_list,
        'page_obj': page_obj,
        'distinct_countries': distinct_countries,
    })
    
def home(request):
    return render(request, 'Athletes/index.html')