from datetime import datetime


def get_car_if_exist(car_id):
    from car.models import Car
    try:
        car = Car.objects.get(id=car_id)
        return car
    except Exception as e:
        print(e)
        return None


def save_purchase(user, car):
    from car.models import Purchase
    purchase = Purchase()
    purchase.car = car
    purchase.user = user
    purchase.purchase_date = datetime.now()
    purchase.created_at = datetime.now()
    purchase.updated_at = datetime.now()
    purchase.save()
    return purchase
