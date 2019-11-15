from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.views import View  # Import the View parent class
from myclub_app.histogram import *
from django.template.loader import render_to_string
from django.template.loader import get_template
# Create your views here.


def home_page(request):
    current_time = datetime.now()
    view = """<hmtl>
        <head>
        <body>

        <p>Todays time {}</p>
        <form method = "GET" action = "/myclub_app">
        <button type = "submit">Main Page</button>
        </form>
        <form method = "GET" action = "/myclub_app/profile">
        <button type = "submit">Histogram</button>
        </form>
        </body>
        </head>
     </html>""".format(current_time)
    return HttpResponse(view)


def main_page(request):
    view = """<hmtl>
        <head>
        <body>
        <p>Click below to get you to the home page</p>
        <form  method = "GET" action = "home/">
        <button type = "submit">HOME PAGE</button>
        </form>
        </body>
        </head>
     </html>"""
    return HttpResponse(view)


class userHistogram(View):

    def get(self, request):
        words = histogram_Dictionary(getText())
        sentence = read_Sentence(sampler_Dictionary_sentence(words))
        return render(request, 'histogram.html', {'sentence': sentence})
