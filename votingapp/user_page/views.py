from django.http import HttpResponse
from django.shortcuts import redirect, render
from collections import Counter
from user_page.models import Candidate

def page(request):
    return render(request,'page.html')
def vote(request):
    if request.method=='POST':
        nme=request.POST.get('candidate')
        if nme:
            Candidate.objects.create(name=nme)
            return redirect('page')
    return render(request,'vote.html')


def result(request):
    candidates = Candidate.objects.all()
    candidate_names = [candidate.name for candidate in candidates]

    
    name_counts = Counter(candidate_names)

    
    candidate_with_most_entries = max(name_counts, key=name_counts.get)

    if candidate_with_most_entries:
        response = HttpResponse(f"The candidate with the most votes is: {candidate_with_most_entries}")
    else:
        response = HttpResponse("No candidates found.")
    
    return response
    
    
    