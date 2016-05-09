filePointer = open('input.txt','r')

totalPaper = 0
totalRibbon = 0
overallPaper = 0

def findSmallestSide(length, width, height):
    side1 = length * width
    side2 = length * height
    side3 = width * height
    smallest = "null"
    if side1 < side2:
        smallest = "side1"
        if side1 < side3:
            smallest = "side1"
        else:
            smallest = "side3"
    else:
        if side2 < side3:
            smallest = "side2"
        else:
            smallest = "side3"

    return smallest    

def findSmallestSide2(length, width, height):
    sides = [length, width, height]
    print (sides)
    sides.sort()
    print (sides)
    print (sides[0])
    print (sides[1])
    return sides[1]*sides[0]

def find2SmallestSides(length, width, height):
    sides = [length, width, height]
    print (sides)
    sides.sort()
    print (sides)
    print (sides[0])
    print (sides[1])
    return sides[0],sides[1]

def part2(length, width, height):
    side1, side2 = find2SmallestSides(length, width, height) 
    presentWrap = side1 * 2 + side2 * 2
    bow = length * width * height
    combined = presentWrap + bow
    return combined

for line in filePointer.readlines():
    print (line)
    length, width, height = line.split("x")
    length = int(length)
    width = int(width)
    height = int(height)
    print ("Length:", length)
    print ("Width:",width)
    print ("Height",height)

    side1 = length * width
    side2 = length * height
    side3 = width * height

    packageSurface = (side1 + side2 + side3)*2
    print ("Surface Area:",packageSurface)

    smallestSide = findSmallestSide2(length, width, height)
    totalPaper = packageSurface + smallestSide
    print ("Current totalPaper:",totalPaper)

    overallPaper = overallPaper + totalPaper
    print ("OverallPaper:",overallPaper)

    overallRibbon = part2(length, width, height)
    totalRibbon = overallRibbon + totalRibbon
    print ("Total Ribbon:",totalRibbon)



