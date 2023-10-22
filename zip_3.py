# English Version
print('''---------- English Version ----------''')
goods_en = ['Laptop', 'Smartphone', 'TV', 'PS5', 'PC']
on_sale_en = ['for sale', 'Sales', 'Sales', 'for sale', 'Sale']
goods_on_sale_en = list(zip(goods_en, on_sale_en))
print(f"Goods in stock: {goods_on_sale_en}")

# Russian Version
print('''---------- Русская версия ----------''')
goods_ru = ['Ноутбук', 'Смартфон', 'Телевизор', 'Плейстейшн 5', 'Компьютер']
on_sale_ru = ['Продается', 'Продано', 'Продано', 'Продается', 'Продано']
goods_on_sale_ru = list(zip(goods_ru, on_sale_ru))
print(f"Товары на складе: {goods_on_sale_ru}")



