from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string


get_month_name = {
    "january": "You Selected January!",
    "february": "You Selected February!",
    "march": "You Selected March!",
    "april": "You Selected April!",
    "may": "You Selected May!",
    "june": "You Selected June!",
    "july": "You Selected July!",
    "august": "You Selected August!",
    "september": "You Selected September!",
    "october": "You Selected October!",
    "november": "You Selected November!",
    "december": None,
}


def index(request):
    months = list(get_month_name.keys())
    return render(request, "challanges/index.html", {
        "months": months
    })



def month_number_view(request, month_name):
    months = list(get_month_name.keys())

    if month_name > len(months):
        return HttpResponseNotFound("Invalid Month Number!")

    redirect_month = months[month_name - 1]
    redirect_path = reverse("month-path", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def month_name_view(request, month_name):
    try:
        response_text = get_month_name[month_name]
        return render(request, "challanges/challanges.html", {
            "title": month_name,
            "response": response_text
        })
    except:
        # response_text = render_to_string("404.html")
        # return HttpResponseNotFound(response_text)
        raise Http404()
