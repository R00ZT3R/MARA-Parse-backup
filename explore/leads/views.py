from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from transformers import pipeline
# Create your views here.

class IndexView(View):
    html_file = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.html_file)

def result(request):

    context = {}

    if(request.method == 'POST'):
        file1 = request.FILES('fa')

    # Open and read the article
    f = open("article.txt", "r", encoding="utf8")
    to_tokenize = f.read()

    # Initialize the HuggingFace summarization pipeline
    summarizer = pipeline("summarization")
    summarized = summarizer(to_tokenize, min_length=75, max_length=300)

    # return summarized text
    print(summarized)
    return summarized

class ResultView(View):
    html_file = "result.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.html_file)

def quiz_view(*args, **kwargs):
    return HttpResponse("<h1>Quizzes</h1>")

def summarization_view(*args, **kwargs):
    return HttpResponse("<h1>Summarization of content</h1>")