class Ip:
    def __init__(self, ip, maske=0):
        if maske==0:
            if "/" in ip:
                self.ip, self.cidr = ip.split("/")

    def getip(self):
        return self.ip
    
    def getInt(self):
        number = 0
        field = self.ip.split(".")
        for item in field:
            number = number * 256 + int(item)
        return number
    
    def getIpfromInt(self, number):
        ip = ""   
        for i in range(4):
            rest = number % 256
            ip = str(rest) + "." + ip
            number = number // 256
        return ip