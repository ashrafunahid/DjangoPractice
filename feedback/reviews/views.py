from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def reviews(request):
    if request.method == "POST":
        entered_username = request.POST['username']
        print(len(entered_username))
        if entered_username == "" or len(entered_username) < 5:
            return render(request, "reviews/review.html", {
                "has_error": True
            })
        return HttpResponseRedirect("thank-you")

    return render(request, "reviews/review.html", {
        "has_error": False
    })

def thank_you(request):
    return render(request, "reviews/thankyou.html")