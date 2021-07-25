from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from transformers import pipeline
import torch
from scripts.questiongenerator import QuestionGenerator
from scripts.questiongenerator import print_qa
# Create your views here.

all = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '\n']
all_caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

class OverwriteStorage(FileSystemStorage):
    def _save(self, name, content):
        available_name = name
        if self.exists(name):
            available_name = self.get_available_name(name)

        super(OverwriteStorage, self)._save(available_name, content)
        return available_name

class IndexView(View):
    html_file = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.html_file)

def result_upload(request):
    context = {}

    if(request.method == 'POST'):
        file1 = request.FILES['fa']

    fs = OverwriteStorage()

    file1.name = fs._save(file1.name, file1)
    print(file1.name)
    # Open and read the article
    f = open(f'./media/{file1.name}', 'r', encoding="utf8")
    to_tokenize = f.read()

    # Initialize the HuggingFace summarization pipeline
    summarizer = pipeline("summarization")
    summarized = summarizer(to_tokenize, min_length=75, max_length=300)

    t1 = ""

    for i in summarized:
        if i in all or i in all_caps:
            t1 += i

    context["result"] = summarized[0]["summary_text"]
    print(summarized[0]["summary_text"])
    # return summarized text
    return render(request, "result.html", context)

class QuestionView(View):
    html_file = "question.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.html_file)

def question_upload(request):
    device = torch.device('cuda')
    # assert device == torch.device('cuda'), "Not using CUDA. Set: Runtime > Change runtime type > Hardware Accelerator: GPU"

    qg = QuestionGenerator()
    with open('test_data/indian_matchmaking.txt', 'r') as a:
        article = a.read()

    qa_list = qg.generate(
        article, 
        num_questions=10, 
        answer_style='all'
    )
    print_qa(qa_list)