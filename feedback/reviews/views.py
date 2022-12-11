from django.http import HttpResponseRedirect
from django.shortcuts import render
from . forms import ReviewForm
from . models import Review
from django.views import View
# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            # "has_error": False,
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()  # if using ModelForm
            return HttpResponseRedirect("thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        })


# def reviews(request):
#     # if request.method == "POST":
#     #     entered_username = request.POST['username']
#     #     print(len(entered_username))
#     #     if entered_username == "" or len(entered_username) < 5:
#     #         return render(request, "reviews/review.html", {
#     #             "has_error": True
#     #         })
#     #     return HttpResponseRedirect("thank-you")

#     if request.method == "POST":
#         form = ReviewForm(request.POST)

#         # # For Updating Data
#         # existing_data = Review.objects.get(pk=1)
#         # form = ReviewForm(request.POST, instance=existing_data)

#         if form.is_valid():
#             # print(form.cleaned_data)
#             # review = Review(
#             #     user_name=form.cleaned_data["user_name"],
#             #     review_text=form.cleaned_data["review_text"],
#             #     rating=form.cleaned_data["rating"])
#             # review.save()
#             form.save()  # if using ModelForm
#             return HttpResponseRedirect("thank-you")
#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {
#         # "has_error": False,
#         "form": form
#     })


def thank_you(request):
    return render(request, "reviews/thankyou.html")
