from django.shortcuts import redirect, render
from django.http import HttpResponse
from cards.models import Flashcard
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def home(request):
    flashcards = Flashcard.objects.all()
    contexts = {'flashcards':flashcards}
    return render(request, 'cards/home.html',contexts)

def create_flashcard(request):
    if request.method == 'POST':
        question = request.POST['question']
        answer = request.POST['answer']
        Flashcard.objects.create(question=question, answer=answer)
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


def quiz(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'cards/quiz.html', {'flashcards':flashcards})

def main(request):
    
    return render(request, 'cards/main.html')

def xo(request):
    
    return render(request, 'cards/xo.html')



def flashcard_list(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'cards/flashcard_list.html', {'flashcards': flashcards})



def tic_tac_toe_with_quiz(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'your_template.html', {'flashcards': flashcards})





