
class Computer:

    def __init__(self, name="", ip="", os=""):
        self.name = name
        self._ip = ip if ip != "" else "127.0.0.1"
        self.os = os if os != "" else "Windows Server 2016"

    def __str__(self):
        return f"Computer: {self.name} - {self.ip}"

    # Method - A function tied to a class/object
    def ping(self):
        print(f"pinging {self.name} at {self.ip}")
        return True  # faking that we found it

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        if Computer._validIp(value):
            self._ip = value
        else:
            raise ValueError("Not a valid IP 4 Address")

    @staticmethod
    def _validIp(value):
        octets = value.split(".")
        if len(octets) != 4:
            return False

        try:
            for octet in octets:
                o = int(octet)
                if not (0 <= o <= 255):
                    return False
        except:
            return False
        else:
            return True


if __name__ == "__main__":
    # creating an instance, Instantiation
    c1 = Computer(name="web-server-1", ip="192.16.200.12")
    c2 = Computer(name="client321", os="Windows 10")

    c1.ip = "100.100.200.0"

    print(c1)
    print(c2)
    if c1.ping():
        print("The first machine is on the network")
