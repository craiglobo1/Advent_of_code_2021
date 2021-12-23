from copy import copy
from dataclasses import dataclass
from typing import *

if 0:
    filename = "d16_input.txt"
else:
    filename = "sample.txt"

with open(filename, "r") as rf:
    lines = rf.readlines()
    lines = [val.strip()for val in lines]

bits_packet = lines[0]
def hexaToBin(hexa):
    ans = ""
    toBin = {
        "0" : "0000",
        "1" : "0001",
        "2" : "0010",
        "3" : "0011",
        "4" : "0100",
        "5" : "0101",
        "6" : "0110",
        "7" : "0111",
        "8" : "1000",
        "9" : "1001",
        "A" : "1010",
        "B" : "1011",
        "C" : "1100",
        "D" : "1101",
        "E" : "1110",
        "F" : "1111"
    }
    for digit in hexa:
        ans += toBin[digit]
    return ans

def unpackAt(iterable, index):
    return iterable[:index], iterable[index:]

class Packet:
    def __init__(self, packetStr):

        self.packetBits = hexaToBin(packetStr)
        self.version, self.packetBits = unpackAt(self.packetBits, 3)
        self.typeID , self.packetBits = unpackAt(self.packetBits, 3)
        self.typeID = int(self.typeID, 2)
        self.version = int(self.version, 2)
        if self.typeID == 4:
            extra = (len(self.packetBits)%4)*[0]
            self.packetBits += extra



        

packet = Packet(bits_packet)




