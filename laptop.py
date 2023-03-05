from interface import Interface


class HPLaptop(Interface):
    def screen(self):
        print("\nScreen: 13.3 inch Full HD display")

    def keyboard(self):
        print("\nKeyboard: has lightning")

    def touchpad(self):
        print("\nTouchpad: +")

    def webcam(self):
        print("\nWebcam: -")

    def ports(self):
        print("\nPorts: USB Type-c, HDMI 2x, Ethernet, USB 3.0")

    def dynamics(self):
        print("\nDynamics: harman/kardon Pro Stereo")


