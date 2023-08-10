from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
# Create your views here.


def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'reviews/create_review.html', {'form': form})



def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})


def edit_review(request, id):
    review = Review.objects.get(id=id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_detail_view', review.id)  # Use review.id here
    else:
        form = ReviewForm(instance=review)
    return render(request, "reviews/edit_review.html", {"form": form, "review": review})



def review_details(request, id):
    review = Review.objects.get(id=id)
    return render(request, "reviews/review_detail.html",{"review": review
    })