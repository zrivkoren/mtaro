from django.shortcuts import render_to_response
from mtaro.taro.models import TaroCard
import random
from django.http import HttpResponse


def home(request):
    all_cards_in_home = TaroCard.objects.all()[:2]
    return render_to_response('taro/home.html', {'all_cards_in_home': all_cards_in_home})	
	
def card(request):
    TaroCard_id = TaroCard.objects.get(id=1)
    return HttpResponse("You're view on card number %s." % TaroCard_id)
	
def all(request):
    all_cards = TaroCard.objects.all()[:]
    return render_to_response('taro/all.html', {'all_cards': all_cards})
	
def random_cards(request):
    random_card = random.choice(TaroCard.objects.all())
    return render_to_response('taro/random-card.html', {'random_card': random_card})
	
def random_cards_list(request):
    random_list = random.sample((TaroCard.objects.all()), 4)
    return render_to_response('taro/order.html', {'random_list': random_list})