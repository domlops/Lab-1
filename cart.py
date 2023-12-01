class ShoppingCart:
  def __init__(self):
      self.items = []

  def add_item(self, item):
      self.items.append(item)
      self.items = sorted(self.items, key=lambda x: x.price)


  def del_item(self, item):
      self.items.remove(item)

  def calculate_total(self):
      total = sum(item.price for item in self.items)
      return total
