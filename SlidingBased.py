width = input("Width: ")
height = input("Height: ")
parts = input("Parts of Window: ")
SashNum = input("Number of Sashes: ")

width = float(width)
height = float(height)
parts = int(parts)
SashNum = int(SashNum)

debug = 1
# .....................................................
# Sum all 4 sides of Frames
FrameSum = ((width*2)+(height*2))*85000
if debug == 1:
    print("Frame:", FrameSum)
# Mullions
Mullions = ((parts-1)*(height))*75000
if debug == 1:
    print("Mullions:", Mullions)
# Sash
Sashes = SashNum*(((width/parts)*2)+(height*2))*75000
if debug == 1:
    print("Sashes:", Sashes)
# Interlock
Interlock = SashNum*((height)*15000)
if debug == 1:
    print("InterLock:", Interlock)
# Overlapping Cover
OCover = SashNum*((((width/parts)*2)+(height*2))*15000)
if debug == 1:
    print("Overlapping Cover:", OCover)
# Alminuim Rail
Arail = width * 10000
if debug == 1:
    print("Alminuim Rail:", Arail)
# Tape
Tape = (SashNum*(((width/parts)*2)+height))*1200
if debug == 1:
    print("Tape:", Tape)
# Equipment
Equipment = SashNum*200000
if debug == 1:
    print("Equipment:", Equipment)
# Glass
Glass = ((width*height)*0.7)*77000
if debug == 1:
    print("Glass:", Glass)
# Installation Equipment
Iequip = SashNum*40000
if debug == 1:
    print("Installation Material:", Iequip)

FinalPrice = FrameSum+Mullions+Sashes+Interlock+OCover+Arail+Tape+Tape+Equipment+Glass+Iequip
FinalPrice += (FinalPrice*10)/100
if debug == 1:
    print("Installation Price: 10 Percent", (FinalPrice*10)/100)
print("Total price of Sliding Door and window:", FinalPrice)