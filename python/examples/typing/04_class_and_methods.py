# python -m mypy .\04_class_and_methods.py
from active_worker import ActiveWorker


claus = ActiveWorker(name="Claus", age=29, city="Berlin")

# uncomment and see the suggestions from the IDE:
# worker.

report_message = claus.report_for_duty()
print(report_message)
claus.carry_item("shampoo")
claus.carry_items(["lasagna", "his own cross"])

items = claus.unload_items()

for item in items:
    # uncomment and see the suggestions from the IDE:
    # item.
    print(item.upper())


# ooops

bertrand = ActiveWorker(name="Bertrand", age="39", city="Paris")


arguments = {"name": "Sally", "age": "21", "city": "New York"}
sally = ActiveWorker(**arguments)


# python -m mypy .\04_class_and_methods.py
