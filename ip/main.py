from ip_class import Ip

addr1 = Ip("192.168.0.1/24")

print(addr1.ip, addr1.cidr, addr1.getInt())

print(addr1.getIpfromInt(addr1.getInt()+512))