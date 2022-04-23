shopping_dict = {
    "piekarnia": ['chleb', 'pączek', 'bułki'],
    "warzywniak": ['marchew', 'seler', 'rukola']
}

shop_dict = dict(shopping_dict)
for shop, product in shop_dict.items():
  print(f"Idę do {shop} i kupuję następujące {product}")