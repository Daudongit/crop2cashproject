from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import (views, status, permissions)

from .serializers import (
    UserSerializer, ItemSerializer, ItemDetailSerializer,
    ItemListSerializer, BuyerSerializer
)
from .models import Item, Buyer, BuyerInterest

# Create your views here.


class SignUpView(views.APIView):
    # Seller signup and login
    def post(self,request):
        data = request.data.copy()
        data['username'] = request.data['email']
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            data = {'token':token.key, **serializer.data}
            return Response(
                {'success':True,'data':data},
                status.HTTP_200_OK
            )
        return Response(
            {'success':False,'error':serializer.errors}
        )

class LoginView(views.APIView):
    #Login seller
    def post(self,request):
        user = authenticate(
            email=request.data['email'], 
            password=request.data['password']
        )

        if user is not None:
            if user.is_active:
                login(request, user)
                serialized = UserSerializer(user)
                token, _ = Token.objects.get_or_create(user=user)
                data = {'token':token.key, **serialized.data}
                return Response(
                    {'success':True,'data':data},
                    status.HTTP_200_OK
                )
            else:
                return Response({
                    'success': False,
                    'error': 'This account has been disabled.'
                    }, status=status.HTTP_401_UNAUTHORIZED
                )
        else:
            return Response({
               'success': False,
               'error': 'Invalid email/password combination.'
                }, status=status.HTTP_401_UNAUTHORIZED
            )


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    #Logout seller
    def post(self, request, format=None):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class ItemView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    parser_class = (FileUploadParser,)

    # Get items for login seller
    def get(self,request):
        items = Item.objects.filter(
            user=request.user,mark_delete=False
        )
        serialized = ItemSerializer(items,many=True)
        return Response(
            {'success':True,'data':serialized.data},
            status.HTTP_200_OK
        )

    # Create new item for login seller
    def post(self,request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = ItemSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'success':True,'data':serializer.data},
                status.HTTP_200_OK
            )
        return Response({'status':False,'error':serializer.errors})

    # Mark login seller item as sold to a buyer
    def put(self,request,pk):
        item = get_object_or_404(Item.objects.all(), pk=pk)
        if item.user == request.user:
            serializer = ItemSerializer(
                item, data={'sold_status':True}, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                buyer_interest_qs = BuyerInterest.objects.filter(
                    item=item,buyer_id=request.data['buyer_id']
                )
                buyer_interest_qs.update(is_new_owner=True)
                return Response(
                    {'success':True,'data':serializer.data},
                    status=status.HTTP_202_ACCEPTED
                )

        return Response({
            'success': False,
            'error': 'Non authorize item'
            }, status=status.HTTP_401_UNAUTHORIZED
        )

    # Mark login seller item as delete
    def delete(self,request,pk):
        item = get_object_or_404(Item.objects.all(), pk=pk)
        if item.user == request.user:
            item.mark_delete = True
            item.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response({
            'success': False,
            'error': 'Non authorize item'
            }, status=status.HTTP_401_UNAUTHORIZED
        )



class ItemDetailView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    # Get login seller item detail with interested buyers
    def get(self,request):
        item = Item.objects.get(pk=request.query_params.get('item_id'))
        if request.user == item.user:
            serialized = ItemDetailSerializer(item)
            return Response(
                {'success':True,'data':serialized.data},
                status.HTTP_200_OK
            )
        return Response({
            'success': False,
            'error': 'Non authorize item'
            }, status=status.HTTP_401_UNAUTHORIZED
        )

class HomePageView(views.APIView):

    # Get all unsold items for buyers
    def get(self,request):
        items = Item.objects.filter(sold_status=False,mark_delete=False)
        serialized = ItemListSerializer(items,many=True)
        return Response(
            {'success':True,'data':serialized.data},
            status.HTTP_200_OK
        )

    # Note buyer interest in a seller item
    def post(self,request):
        item_id = request.data['item_id']
        data = request.data.copy()
        data.pop('item_id')
        serializer = BuyerSerializer(data=data)
        
        if serializer.is_valid():
            buyer = serializer.save()
            seller_item = Item.objects.get(pk=item_id)
            BuyerInterest.objects.get_or_create(buyer=buyer,item=seller_item)
            # seller_item.buyers.add(buyer,through_defaults={}) 
            return Response(
                {'success':True,'data':{'message':'your interest is noted'}},
                status.HTTP_200_OK
            )
        return Response({'status':False,'error':serializer.errors})


def index(request):
    return render(request, 'jijiclone/index.html')


