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
        print(request)
        return render(request, self.html_file)

def result_upload(request): # Change this back
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
    print(to_tokenize)
    summarizer = pipeline("summarization")
    summarized = summarizer(to_tokenize, min_length=75, max_length=300)
    print(summarized)

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
    context={}
    TESTING=False
    if TESTING: 
        context={"result":[{'question': 'How do you approach creative challenges?', 'answer': 'One way to approach creative challenges is by following the five-step process of 1) gathering material, 2) intensely working over the material in your mind, 3) stepping away from the problem, 4) allowing the idea to come back to you naturally, and 5) testing your idea in the real world and adjusting it based on feedback.'}, {'question': 'What is the definition of creativity?', 'answer': 'More often, creativity is about connecting ideas.'}, {'question': 'What is the definition of creative thinking?', 'answer': "Being creative isn't about being the first (or only) person to think of an idea."}, {'question': 'What is the definition of creative thinking?', 'answer': 'Thus, we can say creative thinking is the task of recognizing relationships between concepts.'}, {'question': 'What is the definition of creative thinking?', 'answer': 'The creative process is the act of making new connections between old ideas.'}, {'question': 'Which is the most important part of being creative?', 'answer': [{'answer': '5', 'correct': False}, {'answer': '2', 'correct': False}, {'answer': 'One', 'correct': False}, {'answer': 'first', 'correct': True}]}, {'question': 'How do you approach creative challenges?', 'answer': [{'answer': 'One', 'correct': False}, {'answer': '3', 'correct': False}, {'answer': '1', 'correct': True}, {'answer': '5', 'correct': False}]}, {'question': 'How do you approach creative challenges?', 'answer': [{'answer': 'five', 'correct': False}, {'answer': '1', 'correct': False}, {'answer': 'One', 'correct': True}, {'answer': '3', 'correct': False}]}, {'question': 'How do you approach creative challenges?', 'answer': [{'answer': 'five', 'correct': False}, {'answer': '2', 'correct': False}, {'answer': '4', 'correct': False}, {'answer': '3', 'correct': True}]}, {'question': 'How do you approach creative challenges?', 'answer': [{'answer': '5', 'correct': False}, {'answer': '3', 'correct': False}, {'answer': '2', 'correct': False}, {'answer': '4', 'correct': True}]}]}
        return render(request, "question-result.html", context)
    else:
        if(request.method == 'POST'):
            file1 = request.FILES['fa']

        fs = OverwriteStorage()

        file1.name = fs._save(file1.name, file1)
        print(file1.name)
        # Open and read the article
        f = open(f'./media/{file1.name}', 'r', encoding="utf8")
        to_tokenize = f.read()

        qg = QuestionGenerator()
        qa_list = qg.generate(
            to_tokenize, 
            num_questions=10, 
            answer_style='all'
        )
        context["result"] = qa_list[0]["question"]
        print(qa_list)
        print_qa(qa_list)
        return render(request, "question-result.html", context)

class AboutView(View):
    html_file = "about.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.html_file)