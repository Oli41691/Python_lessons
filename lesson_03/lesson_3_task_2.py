from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "SLK", "+79854862357"),
    Smartphone("ZTE", "OL483", "+79226582185"),
    Smartphone("Poco", "M5", "+75476321575")
]
for Smartphone in catalog:
    print(f"{Smartphone.mark} - {Smartphone.model} - {Smartphone.number}")
