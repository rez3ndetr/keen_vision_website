from .forms import UserForm, RegistrationUser
from django.shortcuts import render, redirect
from .servise import send
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from Keenvision.keenvision import settings
from django.contrib.auth import login


@csrf_exempt
def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']

            message = f"Новая заявка с сайта:\nИмя: {name}\nТелефон: {phone}"

            import requests
            #было бы неплохо положить токен бота в какойнибудь файл с .gitignore но мне лень
            bot_token = '6488282721:AAGNmtv8Lbb6o1YHE_9mLCXf1U8p8JZGtRo'
            bot_chat_id = '5253412990'
            bot_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

            data = {'chat_id': bot_chat_id, 'text': message}
            requests.post(bot_url, data=data)

            return redirect("success")
        else:
            print(form.errors)

    else:
        form = UserForm()




    return render(request,"hey/index.html", {'form': form})


def success(request):
    return render(request,"hey/success.html")


def signup(request):
    if request.method == 'POST':
        form = RegistrationUser(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("success")
        else:
            print(form.errors)
    else:
        form = RegistrationUser()

    return render(request,"account/signup.html", {'form': form})

# def csrf_failure(request, reason=""):
#     ctx = {'message': 'some custom messages'}
#     return render_to_response(your_custom_template, ctx)




