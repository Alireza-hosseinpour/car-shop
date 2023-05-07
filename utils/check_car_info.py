def save_car(data):
    from car.models import Car, Category
    car = Car()
    car.category = Category.objects.get(id=data.validated_data.get("category_id", None))
    car.name = data.validated_data.get("name", None)
    car.brand = data.validated_data.get("brand", None)
    car.color = data.validated_data.get("color", None)
    car.price = data.validated_data.get("price", None)
    car.image = data.validated_data.get("image", None)
    car.save()
