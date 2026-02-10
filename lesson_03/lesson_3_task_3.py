from address import Address
from mailing import Mailing

to_add = Address(123456, 'Москва', 'Ленинский проспект', 10, 5)
from_add = Address(654321, 'Санкт-Петербург', 'Невский проспект', 20, 15)

shipment = Mailing(to_add, from_add, 10000, "Sheeps")

print(f"Отправление {shipment.track} из {shipment.from_add}"
      f"в {shipment.to_add}."
      f"Стоимость {shipment.cost} рублей")
