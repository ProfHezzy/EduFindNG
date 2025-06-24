from django.shortcuts import render
from .forms import SchoolSearchForm
from schools.models import SchoolProfile
from .models import SchoolComparison
from django.contrib.auth.decorators import login_required


def search_schools(request):
    form = SchoolSearchForm(request.GET or None)
    schools = SchoolProfile.objects.all()
    if form.is_valid():
        # Filtering logic (simplified)
        if form.cleaned_data.get('location'):
            schools = schools.filter(address__icontains=form.cleaned_data['location'])
        if form.cleaned_data.get('school_type'):
            schools = schools.filter(school_type__icontains=form.cleaned_data['school_type'])
        if form.cleaned_data.get('keywords'):
            schools = schools.filter(name__icontains=form.cleaned_data['keywords'])
        # Add more filters as needed
    return render(request, 'search/search_results.html', {'form': form, 'schools': schools})


@login_required
def compare_schools(request):
    if request.method == 'POST':
        school_ids = request.POST.getlist('school_ids')
        schools = SchoolProfile.objects.filter(id__in=school_ids)
        comparison = SchoolComparison.objects.create(user=request.user)
        comparison.schools.set(schools)
        return render(request, 'search/comparison.html', {'schools': schools})
    return render(request, 'search/comparison_select.html')
