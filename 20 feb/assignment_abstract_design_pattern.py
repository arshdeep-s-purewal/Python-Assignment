class Iphone:
    def __init__(self, phone = None):
        self.phone = phone
    
    def show_phone(self):
        phone = self.phone()
        print("we have {phone} and its release date is {phone.release_date()}")

class Iphone10:
    def __init__(self, rlease_date, memory, camera_in_px, battery_in_mAh, bionic_chipset, color):
        self.rlease_date = rlease_date
        self.memory = memory
        self.camera_in_px = camera_in_px
        self.battery_in_mAh = battery_in_mAh
        self.bionic_chipset = bionic_chipset
        self.color = color

    def release_date(self):
        return self.rlease_date

    def ram(self):
        return self.memory

    def camera(self):
        return self.camera_in_px

    def battery(self):
        return self.battery_in_mAh
    
    def chipset(self):
        return self.bionic_chipset
    
    def colors(self):
        return self.color

# x = Iphone10(rlease_date = "03/09/2017", memory = "3 GB", camera_in_px = "12 px", battery_in_mAh = "2716mAh", bionic_chipset = "A11", color = ["space gray", "silver", "White", "Black"])
# a = x.colors()
# print("Release date of Iphone X was ",a)

class Iphone11:
    def __init__(self, rlease_date, memory, camera_in_px, battery_in_mAh, bionic_chipset, color):
        self.rlease_date = rlease_date
        self.memory = memory
        self.camera_in_px = camera_in_px
        self.battery_in_mAh = battery_in_mAh
        self.bionic_chipset = bionic_chipset
        self.color = color

    def release_date(self):
        return self.rlease_date

    def ram(self):
        return self.memory

    def camera(self):
        return self.camera_in_px

    def battery(self):
        return self.battery_in_mAh
    
    def chipset(self):
        return self.bionic_chipset
    
    def colors(self):
        return self.color

# eleven = Iphone11(rlease_date = "20/09/2019", memory = "4 GB", camera_in_px = "12 px", battery_in_mAh = "3110mAh", bionic_chipset = "A13", color = ['Black', 'Green', 'Yellow', 'Purple', 'Red', 'White'])
# e = eleven.ram()
# print(e)


class Iphone12:
    def __init__(self, rlease_date, memory, camera_in_px, battery_in_mAh, bionic_chipset, color):
        self.rlease_date = rlease_date
        self.memory = memory
        self.camera_in_px = camera_in_px
        self.battery_in_mAh = battery_in_mAh
        self.bionic_chipset = bionic_chipset
        self.color = color

    def release_date(self):
        return self.rlease_date

    def ram(self):
        return self.memory

    def camera(self):
        return self.camera_in_px

    def battery(self):
        return self.battery_in_mAh
    
    def chipset(self):
        return self.bionic_chipset
    
    def colors(self):
        return self.color

# twelve = Iphone12(rlease_date = "23/10/2020", memory = "4 GB", camera_in_px = "12 px", battery_in_mAh = "2815mAh", bionic_chipset = "A14", color = ['Black', 'Green', 'Blue', 'Red', 'White'])
# tw = twelve.release_date()
# print(tw)

class Iphone13:
    def __init__(self, rlease_date, memory, camera_in_px, battery_in_mAh, bionic_chipset, color):
        self.rlease_date = rlease_date
        self.memory = memory
        self.camera_in_px = camera_in_px
        self.battery_in_mAh = battery_in_mAh
        self.bionic_chipset = bionic_chipset
        self.color = color

    def release_date(self):
        return self.rlease_date

    def ram(self):
        return self.memory

    def camera(self):
        return self.camera_in_px

    def battery(self):
        return self.battery_in_mAh
    
    def chipset(self):
        return self.bionic_chipset
    
    def colors(self):
        return self.color

# thirteen = Iphone13(rlease_date = "24/09/2021", memory = "4 GB", camera_in_px = "12 px", battery_in_mAh = "3240mAh", bionic_chipset = "A15", color = ['Starlight', 'Midnight', 'Blue', 'Pink', 'Green'])
# tt = thirteen.ram()
# print(tt)

class Iphone14:
    def __init__(self, rlease_date, memory, camera_in_px, battery_in_mAh, bionic_chipset, color):
        self.rlease_date = rlease_date
        self.memory = memory
        self.camera_in_px = camera_in_px
        self.battery_in_mAh = battery_in_mAh
        self.bionic_chipset = bionic_chipset
        self.color = color

    def release_date(self):
        return self.rlease_date

    def ram(self):
        return self.memory

    def camera(self):
        return self.camera_in_px

    def battery(self):
        return self.battery_in_mAh
    
    def chipset(self):
        return self.bionic_chipset
    
    def colors(self):
        return self.color

# fourteen = Iphone14(rlease_date = "16/09/2022", memory = "6 GB", camera_in_px = "12 px", battery_in_mAh = "3279mAh", bionic_chipset = "A15", color = ['Midnight', 'Purple', 'Starlight', 'Blue', 'Red'])
# f = fourteen.ram()
# print(f)


ph = Iphone(Iphone14)
 