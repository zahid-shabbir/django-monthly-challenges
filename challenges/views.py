from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

_monthly_challenges = {
    "January": "Build a text-based adventure game",
    "February": "Create a simple web server",
    "March": "Write a script to automate a task on your computer",
    "April": "Build a machine learning model to predict something",
    "May": "Develop a simple GUI application",
    "June": "Create a data visualization using Matplotlib or Seaborn",
    "July": "Write a web scraper to extract data from a website",
    "August": "Build a chatbot",
    "September": "Create a simple game using Pygame",
    "October": "Develop a neural network using TensorFlow or PyTorch",
    "November": "Build a web application using Django",
    "December": None  # "Create a command-line tool to automate a task"
}


def index(request):
    # list_items = ""
    months = list(_monthly_challenges.keys())

    return render(request, 'challenges/index.html', {'months': months})
    # for month in months:
    #     list_items += f"<li><a href='{reverse('monthly_challenge', args=[month])}'>{month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"

    # return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(_monthly_challenges.keys())

    if month > len(months) or month < 1:
        response_data = render_to_string('404.html')
        return HttpResponseNotFound(response_data)

    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):

    month = month.title()
    try:
        challenge_text = _monthly_challenges[month]

        return render(request, 'challenges/challenge.html', {'text': challenge_text, 'month_name': month})
    except :
        raise Http404()