class TollRoad:
    __lv = 0; __hv = 0; __gv = 0
    __lv_tax = 0; __hv_tax = 0
    __tax = 0

    def getinfo(self):
        self.__vid = int(input("Enter Vehicle ID:  "))
        self.__vname = input("Enter Vehicle Name: ")
        while True:
            self.__vtype = input("Enter Vehicle Type (LV,HV,GV): ")
            if self.__vtype.upper() in ["LV", "HV", "GV"]:
                print()
                return self.__vid
            else:
                print("\nInvelid Vehicle Type\n")

    @classmethod
    def calculatetax(cls, vehicle):
        tax = 0
        if vehicle.__vtype.upper() == "LV":
            cls.__lv += 1
            tax += 400
            cls.__lv_tax += tax
        elif vehicle.__vtype.upper() == "HV":
            cls.__hv += 1
            tax += 600
            cls.__hv_tax += tax
        elif vehicle.__vtype.upper() == "GV":
            cls.__gv += 1

        cls.__tax += tax

    @classmethod
    def showinfo(cls):
        print("Total number of Light Vehicles: {}\nTotal number of Heavy Vehicles: {}\nTotal number of Government Vehicles: {}\n\nTotal Tax from Light Vehicles: {}\nTotal Tax from Heavy Vehicles: {}\n\nTotal Tax: {}".format(cls.__lv, cls.__hv, cls.__gv, cls.__lv_tax, cls.__hv_tax, cls.__tax))


vehicles = dict()
n = int(input("Enter number of Vehicles: "))
print()

for i in range(n):
    vehicle = TollRoad()
    vehicle_id = vehicle.getinfo()
    vehicles.setdefault(vehicle_id, vehicle)
    TollRoad.calculatetax(vehicle)

TollRoad.showinfo()