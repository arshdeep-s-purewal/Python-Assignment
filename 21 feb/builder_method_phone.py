class Screen:
    def __init__(self, type):
        self.type = type

class Camera:
    def __init__(self, megapixel):
        self.megapixel = megapixel

class Chipset:
    def __init__(self, chipset):
        self.chipset = chipset

class Phone:
    def __init__(self):
        self.screen = None
        self.camera = None
        self.chipset = None

    def specifications(self):
        print(f"Screen Type: {self.screen.type} \nCamera: {self.camera.megapixel}\nChipset: {self.chipset.chipset}")

iphoneX = Phone()
iphoneX.screen = Screen("HDR")
# print(iphoneX.screen.type)
iphoneX.camera = Camera("12 megapixel")
iphoneX.chipset = Chipset("A12")


class PhoneBuilder:
    def add_screen(self):
        pass

    def add_camera(self):
        pass
        
    def add_chipset(self):
        pass

class IphoneXbuild(PhoneBuilder):
    def __init__(self):
        self.phone = Phone()

    def add_screen(self):
        screen = Screen("HDR")
        self.phone.screen = screen
        return self

    def add_camera(self):
        camera = Camera("12mp")
        self.phone.camera = camera
        return self

    def add_chipset(self):
        chipset = Chipset("A13")
        self.phone.chipset = chipset
        return self

    def build(self):
        return self.phone

class Director:
    def __init__(self, phone_build):
        self.phone_build = phone_build

    def get_phone(self):
        return self.phone_build.add_screen().add_camera().add_chipset().build()

def main():
    iphoneXbuild = IphoneXbuild()
    director = Director(iphoneXbuild)
    phone = director.get_phone()
    # print("hiiiiiiiiiiiiiiii")
    phone.specifications()

if __name__=="main":
    main()