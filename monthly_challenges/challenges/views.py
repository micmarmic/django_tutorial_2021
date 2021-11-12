from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Jan challenge",
    "february": "feb challenge",
    "march": "march challenge",
    "april": "april challenge",
    "may": "may challenge",
    "june": "june challenge",
    "july": "july challenge",
    "august": "august challenge",
    "september": "september challenge",
    "october": "october challenge",
    "november": "november challenge",
    "december": None,
}


# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", { 
        "months": months
    })


# noinspection PyBroadException
def monthly_challenge(request, month):
    # error_text = "Unknown month"
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "challenge_text": challenge_text
        })
    except Exception as e:
        raise Http404()  # auto finds the 404.html file


def monthly_challenge_by_number(request, month):
    if month < 1 or month > 12:
        return HttpResponseNotFound("Invalid month")

    months = list(monthly_challenges.keys())
    month_string = months[month - 1]
    redirect_path = reverse("month-challenge", args=[month_string])
    return HttpResponseRedirect(redirect_path)
