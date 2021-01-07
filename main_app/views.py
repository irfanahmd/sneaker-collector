from django.shortcuts import render
from .models import Sneaker

from django.http import HttpResponse


# Add the Cat class & list and view function below the imports


# class Sneaker:  # Note that parens are optional if not inheriting from another class
#     def __init__(self, name, brand, description, link, image):
#         self.name = name
#         self.brand = brand
#         self.description = description
#         self.link = link
#         self.image = image


# sneakers = [
#     Sneaker('New Balance 327 White Gum Sole', 'New Balance', "Once the pinnacle of athletic footwear, the running shoes of the '70s have become the casual go-to's of the modern age. This is readily apparent with these New Balance 327 sneakers. Their vintage aesthetic is given a modern boost with an oversized N logo, while a nylon and suede upper provides durability and the signature gum rubber outsole provides both traction and contrast with the predominantly white upper.",
#             "https://uncrate.com/new-balance-327-white-gum-sole-sneakers/", 'https://uncrate.com/p/2021/01/New-Balance-327-white-1.jpg'),
#     Sneaker('New Balance 327 Black Castlerock', 'New Balance', "The New Balance N logo is featured prominently on the sides of its sneakers, but nowhere more prominently than on these 327s. A reinterpretation of the Boston, MA company's 1970s runners, they have an oversized N logo and a black/gray upper made from a mix of pigskin and nylon. Designed for casual wear, they're finished with a knobby gum rubber outsole.",
#             'https://uncrate.com/new-balance-327-black-castlerock-sneakers/', 'https://uncrate.com/p/2021/01/New-Balance-327-2.jpg')
# ]


# Create your views here.

def home(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'sneakers/index.html', {'sneakers': sneakers})


def about(request):
    return render(request, 'about.html')


def sneakers_index(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'sneakers/index.html', {'sneakers': sneakers})


def sneakers_detail(request, sneaker_id):
    sneaker = Sneaker.objects.get(id=sneaker_id)
    return render(request, 'sneakers/detail.html', {'sneaker': sneaker})
