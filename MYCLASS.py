# Base class
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def charge(self):
        print(f"{self.brand} {self.model} is charging.")

# Inheritance example — a Smartphone with a camera
class CameraPhone(Smartphone):
    def __init__(self, brand, model, battery_life, camera_megapixels):
        super().__init__(brand, model, battery_life)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"Taking a photo with {self.camera_megapixels} MP camera.")

# Creating an object
phone = CameraPhone("Samsung", "Galaxy S21", 24, 108)
phone.call("123-456-7890")
phone.take_photo()
phone.charge()
