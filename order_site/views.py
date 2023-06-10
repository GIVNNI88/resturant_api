from django.http import JsonResponse
from rest_framework.views import APIView

from order_site.models import Cart, Category, Dish, Items, User, Delivery

class UsertAll(APIView):
    def get(self, request):
        users = User.objects.all()
        return JsonResponse([user.serialize() for user in users], safe=False)


class CategoryAll(APIView):
    def get(self, request):
        categories = Category.objects.all()
        return JsonResponse([category.serialize() for category in categories], safe=False)
    
class CategoryByID(APIView):
    def get(self, request, id):
        categories = Category.filterby(id=id).all()
        return JsonResponse([category.serialize() for category in categories], safe=False)



class DishAll(APIView):
    def get(self, request):
        dishes = Dish.objects.all()
        return JsonResponse([dish.serialize() for dish in dishes], safe=False)


class ItemAll(APIView):
    def get(self, request):
        items = Items.objects.all()
        return JsonResponse([item.serialize() for item in items], safe=False)


class CartAll(APIView):
    def get(self, request):
        carts = Cart.objects.all()
        return JsonResponse([cart.serialize() for cart in carts], safe=False)
    
class DeliveryAll(APIView):
     def get(self, request):
        deliveries = Delivery.objects.all()
        return JsonResponse([delivery.serialize() for delivery in deliveries], safe=False)
    
