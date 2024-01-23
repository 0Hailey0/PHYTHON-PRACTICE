# class Point():
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2

# p = Point(2,8)
# print(p.x)
# print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity=capacity
        self.passengers = [] #startout empty
    
    def add_passenger(self, name): #add passenger by name
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity-len(self.passengers)

flight = Flight(3) 

people = ["harry","ron","hermione","ginny"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"added {person} to flight successfully")
    else:
        print(f"no available seats for {person}")
    