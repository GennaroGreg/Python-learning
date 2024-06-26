class Vehicle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def moves(self):
        print('Drives on the highway')

    def get_make_model(self):
        print(f"I'm a {self.color} {self.make} {self.model}")

my_car = Vehicle('Honda', 'Civic', 'White')

my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Ferrari', '296', 'Red')
your_car.get_make_model()
your_car.moves()

class Airplane(Vehicle):
    def __init__(self, make, model, color, faa_id):
        super().__init__(make, model, color)
        self.faa_id = faa_id

    def identify(self):
        print(f'ID: {self.faa_id}')
    
    def moves(self):
        print('Flies through the air.')

class Truck(Vehicle):
    def moves(self):
        print('Rumbles down the dirt road.')

class Golfcart(Vehicle):
    pass

cessna = Airplane('Cessna', 'Skyhawk', 'Yellow', 'ABC456')
mack = Truck('Mack', 'Dumptruck', 'Brown')
golfwagon = Golfcart('Yamaha', 'XYZ123', 'White')

cessna.get_make_model()
cessna.moves()
cessna.identify()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()


# Polymorphism
print('\n\n')

for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()

