from django.shortcuts import render, redirect
from review.forms import ReviewForm
from review.models import ReviewModel

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_review')
    else:
        form = ReviewForm()
    return render(request, 'review/review.html', {'form': form})

def show_review(request):
    data = ReviewModel.objects.all()
    return render(request, 'review/show_review.html', {'data':data})
