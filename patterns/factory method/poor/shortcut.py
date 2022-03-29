import factory_method_poor as factory_method_poor

# funny python shortcut
desired_class = getattr(factory_method_poor, "Square")(3.4)
print(desired_class.calculate_area())
