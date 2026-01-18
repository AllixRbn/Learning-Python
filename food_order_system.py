italian_food = ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"]
indian_food = ["Curry", "Chutney", "Samosa", "Naan"]

def find_meal(name, menu):
  if name in menu:
    return name
  else:
    return None

def select_meal(name, food_type):
  if food_type == "italian":
    return find_meal(name, italian_food)
  elif food_type == "indian":
    return find_meal(name, indian_food)
  else:
    return None

def display_available_meals(food_type):
  if food_type == "italian":
    print("Available Italian Meals:")
    for i in italian_food:
      print(i)
  elif food_type == "indian":
    print("Available Indian Meals:")
    for i in indian_food:
      print(i)
  else:
    print("Invalid food type")

def create_summary(name, amount, food_type):
  order = select_meal(name, food_type)
  if order:
    return f"You ordered {amount} {name}."
  else:
    return "Meal not found."

print("Welcome to the Food Order System!")
type_input = input("What type of food would you like? : ").lower()
display_available_meals(type_input)
name_input = input("What would you like to order? : ")
amount_input = int(input("How many would you want? : "))
result = create_summary(name_input, amount_input, type_input)
print(result)
