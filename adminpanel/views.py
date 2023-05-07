from django.contrib import messages

from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout

from car.models import Car, Purchase, Category
from django.contrib.auth.mixins import LoginRequiredMixin


class AdminPanelView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        from user.models import User
        users = User.objects.all()
        cars = Car.objects.all()
        purchases = Purchase.objects.all()
        query = request.GET.get('q') if request.GET.get('q') != None else ''
        queryset = users.filter(Q(first_name__icontains=query))

        context = {
            'queryset': queryset,
            'query': query,
            'cars': cars,
            'users': users,
            'purchases': purchases
        }
        return render(request, 'newtemplate/home/index.html', context)


class LoginView(TemplateView):

    def get(self, request, *args, **kwargs):
        page = 'login'
        return render(request, 'newtemplate/home/login.html', {'page': page})

    def post(self, request, *args, **kwargs):
        page = 'login'
        if request.user.is_authenticated:
            return redirect('admin')
        if request.method == 'POST':

            username = request.POST.get('username')
            password = request.POST.get('password')

            try:
                admin = User.objects.get(username=username)
            except:
                messages.error(request, 'user is not found')
                return redirect('login')

            admin = authenticate(request, username=username, password=password)
            if admin is not None:
                login(request, admin)
                return redirect('admin')
            else:
                messages.error(request, 'invalid username or password')
        context = {'page': page}
        return render(request, 'newtemplate/home/login.html', context=context)


def Logout(request):
    logout(request)
    return redirect('login')


class DeleteView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        from user.models import User
        user = User.objects.get(id=self.kwargs['user_id'])
        if user is None:
            messages.error(request, 'user Not exist')
            return redirect('admin')
        user.delete()
        messages.error(request, 'user deleted successfully')
        return redirect('admin')

    def post(self, request, *args, **kwargs):
        from user.models import User
        user = User.objects.get(id=self.kwargs['user_id'])
        if user is None:
            messages.error(request, 'user Not exist')
            return redirect('admin')
        user.delete()
        messages.error(request, 'user deleted successfully')
        return redirect('admin')


class DeleteCarView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        car = Car.objects.get(id=self.kwargs['car_id'])
        car.delete()
        messages.error(request, 'Car deleted successfully')
        return redirect('admin')

    def post(self, request, *args, **kwargs):
        car = Car.objects.get(id=self.kwargs['car_id'])
        if car is None:
            messages.error(request, 'car Not exist')
            return redirect('list-of-cars')
        car.delete()
        messages.error(request, 'Car deleted successfully')
        return redirect('admin')


class UpdateUserView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        from user.models import User
        user = User.objects.get(id=self.kwargs['user_id'])
        return render(request, 'update-user.html', {'user': user})

    def post(self, request, *args, **kwargs):
        from user.models import User
        user = User.objects.get(id=self.kwargs['user_id'])
        print(user)
        print(request.POST)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.address = request.POST.get('Address')
        user.save()
        messages.success(request, 'user info updated successfully')
        return redirect('list-of-users')


class ListOfUsers(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        from user.models import User
        query = request.GET.get('q') if request.GET.get('q') != None else ''
        queryset = User.objects.filter(Q(first_name__icontains=query) |
                                       Q(last_name__icontains=query) |
                                       Q(email__icontains=query)
                                       )

        context = {
            'users': queryset,

        }
        return render(request, 'user-list.html', context)


class ListOfCars(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q') if request.GET.get('q') != None else ''
        cars = Car.objects.filter(Q(name__icontains=query) |
                                  Q(brand__icontains=query) |
                                  Q(category__title__icontains=query)
                                  )

        context = {
            'cars': cars
        }
        return render(request, 'cars-list.html', context)


class UpdateCarView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        car = Car.objects.get(id=self.kwargs['car_id'])
        return render(request, 'car-update.html', {'car': car, 'categories': categories})

    def post(self, request, *args, **kwargs):
        category_title = request.POST.get('category_title')
        selected_category, created_category = Category.objects.get_or_create(title=category_title)
        car = Car.objects.get(id=self.kwargs['car_id'])
        car.category = selected_category or created_category
        car.name = request.POST.get('name')
        car.brand = request.POST.get('brand')
        car.price = request.POST.get('price')
        car.color = request.POST.get('color')
        car.save()
        messages.success(request, 'Car updated successfully')
        return redirect('list-of-cars')


class PurchaseList(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q') if request.GET.get('q') != None else ''
        purchases = Purchase.objects.filter(Q(car__name__icontains=query) |
                                            Q(user__first_name__icontains=query) |
                                            Q(user__last_name__icontains=query) |
                                            Q(created_at__icontains=query)
                                            )

        context = {
            'purchases': purchases
        }
        return render(request, 'purchase-list.html', context)


class PurchaseUpdateView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        purchase = Purchase.objects.get(id=self.kwargs['purchase_id'])
        return render(request, 'update-purchase.html', {'purchase': purchase})

    def post(self, request, *args, **kwargs):
        purchase = Purchase.objects.get(id=self.kwargs['purchase_id'])
        purchase.is_delivered = request.POST.get('is_delivered')
        purchase.is_paid = request.POST.get('is_paid')
        purchase.save()
        return redirect('purchase-list')


class AddCarView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'add-car.html', {'categories': categories})

    def post(self, request, *args, **kwargs):
        category_title = request.POST.get('category_title')
        selected_category, created_category = Category.objects.get_or_create(title=category_title)
        car = Car.objects.create(
            category=selected_category or created_category,
            name=request.POST.get('name'),
            brand=request.POST.get('brand'),
            color=request.POST.get('color'),
            price=request.POST.get('price'),
        )
        messages.success(request, 'car added successfully')
        return redirect('list-of-cars')


class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        from adminpanel.models import Admin
        categories = Category.objects.all()
        admins = Admin.objects.all()
        cars = Car.objects.all()

        return render(request, "homepage/homepage_view.html",
                      {'categories': categories, 'admins': admins, 'cars': cars})
