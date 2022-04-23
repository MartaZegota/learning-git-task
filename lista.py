shopping_dict = {
    "apteka": ['przeciwbolowy', 'przeciwgoraczkowy', 'przeciwwzdeciowy', 'przeciwkaszlowy'],
    "warzywniak": ['marchew', 'seler', 'rukola', 'pomidor']
}

shop_dict = dict(shopping_dict)
for shop, product in shop_dict.items():
  print(f"Idę do {shop} i kupuję następujące {product}")