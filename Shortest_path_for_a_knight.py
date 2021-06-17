from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)


def Minimum_Knight_Movement(posx, posy, desx, desy):
    count = 0
    quadrant = 0

    if (posx == desx) and (posy == desy):
        return count

    while distance(posx, posy, desx, desy) != 0:

        if (posx > desx) and (posy > desy):
            quadrant = 3
        elif (posx > desx) and (posy < desy):
            quadrant = 2
        elif (posx < desx) and (posy > desy):
            quadrant = 4
        elif (posx < desx) and (posy < desy):
            quadrant = 1
        else:
            quadrant = 0  # the endpoint is on x-axis or on the y-axis

        if quadrant == 0:

            if (((posy-desy) % 2 == 0) and (abs(posy-desy) >= 3)) or (((posx-desx) % 2 == 0) and (abs(posx-desx) >= 3)):
                if (posy == desy) and (desx-posx >= 3):
                    posx += 2
                    posy += 1
                    count += 1
                    print(f"({posx},{posy})")
                elif (posy == desy) and (desx-posx <= -3):
                    posx -= 2
                    posy += 1
                    count += 1
                    print(f"({posx},{posy})")
                elif (posx == desx) and (desy-posy <= -3):
                    posx += 1
                    posy -= 2
                    count += 1
                    print(f"({posx},{posy})")
                elif (posx == desx) and (desy-posy >= 3):
                    posx += 1
                    posy += 2
                    count += 1
                    print(f"({posx},{posy})")
            elif (((posy-desy) % 2 != 0) and (abs(posy-desy) >= 3)) or (((posx-desx) % 2 != 0) and (abs(posx-desx) >= 3)):
                if (posy == desy) and (desx-posx >= 3):
                    posx += 1
                    posy += 2
                    count += 1
                    print(f"({posx},{posy})")
                elif (posy == desy) and (desx-posx <= -3):
                    posx -= 1
                    posy += 2
                    count += 1
                    print(f"({posx},{posy})")
                elif (posx == desx) and (desy-posy <= -3):
                    posx += 2
                    posy -= 1
                    count += 1
                    print(f"({posx},{posy})")
                elif (posx == desx) and (desy-posy >= 3):
                    posx += 2
                    posy += 1
                    count += 1
                    print(f"({posx},{posy})")
            elif (posy == desy) and (desx-posx == 2):
                posx += 1
                posy -= 2
                print(f"({posx},{posy})")
                posx += 1
                posy += 2
                print(f"({posx},{posy})")
                count += 2
            elif (posy == desy) and (posx-desx == 2):
                posx -= 1
                posy -= 2
                print(f"({posx},{posy})")
                posx -= 1
                posy += 2
                print(f"({posx},{posy})")
                count += 2
            elif (posx == desx) and (posy-desy == 2):
                posx += 2
                posy -= 1
                print(f"({posx},{posy})")
                posx -= 2
                posy -= 1
                print(f"({posx},{posy})")
                count += 2
            elif (posx == desx) and (desy-posy == 2):
                posx += 2
                posy += 1
                print(f"({posx},{posy})")
                posx -= 2
                posy += 1
                print(f"({posx},{posy})")
                count += 2
            elif (posy == desy) and (desx-posx == 1):
                posx += 1
                posy += 2
                print(f"({posx},{posy})")
                count += 1
            elif (posy == desy) and (posx-desx == 1):
                posx -= 1
                posy += 2
                print(f"({posx},{posy})")
                count += 1
            elif (posx == desx) and (posy-desy == 1):
                posx -= 2
                posy -= 1
                print(f"({posx},{posy})")
                count += 1
            elif (posx == desx) and (desy-posy == 1):
                posx -= 2
                posy += 1
                print(f"({posx},{posy})")
                count += 1
        elif quadrant == 1:

            if distance(posx, posy, desx, desy) == sqrt(2):  # if y-y1 = 1 and x-x1 = 1
                posx -= 1
                posy += 2
                print(f"({posx},{posy})")
                posx += 2
                posy -= 1
                print(f"({posx},{posy})")
                count += 2
                return count
            elif (desx-posx == 3) and (desy-posy == 4):
                posx += 2
                posy += 1
                count += 1
                print(f"({posx},{posy})")
                posx += 2
                posy += 1
                count += 1
                print(f"({posx},{posy})")
            elif (desx-posx == 4) and (desy-posy == 3):
                posx += 1
                posy += 2
                count += 1
                print(f"({posx},{posy})")
                posx += 1
                posy += 2
                count += 1
                print(f"({posx},{posy})")
            elif distance(posx+2, posy+1, desx, desy) < distance(posx+1, posy+2, desx, desy):
                posx += 2
                posy += 1
                count += 1
                print(f"({posx},{posy})")
            else:
                posx += 1
                posy += 2
                count += 1
                print(f"({posx},{posy})")
        elif quadrant == 2:

            if distance(posx, posy, desx, desy) == sqrt(2):
                posx += 1
                posy += 2
                print(f"({posx},{posy})")
                posx -= 2
                posy -= 1
                print(f"({posx},{posy})")
                count += 2
                return count
            elif (desx-posx == -3) and (desy-posy == 4):
                posx -= 2
                posy += 1
                count += 1
                print(f"({posx},{posy})")
                posx -= 2
                posy += 1
                count += 1
                print(f"({posx},{posy})")
            elif (desx-posx == -4) and (desy-posy == 3):
                posx -= 1
                posy += 2
                count += 1
                print(f"({posx},{posy})")
                posx -= 1
                posy += 2
                count += 1
                print(f"({posx},{posy})")
            elif distance(posx-2, posy+1, desx, desy) < distance(posx-1, posy+2, desx, desy):
                posx -= 2
                posy += 1
                count += 1
                print(f"({posx},{posy})")
            else:
                posx -= 1
                posy += 2
                count += 1
                print(f"({posx},{posy})")
        elif quadrant == 3:

            if distance(posx, posy, desx, desy) == sqrt(2):
                posx += 1
                posy -= 2
                print(f"({posx},{posy})")
                posx -= 2
                posy += 1
                print(f"({posx},{posy})")
                count += 2
                return count
            elif (desx-posx == -3) and (desy-posy == -4):
                posx -= 2
                posy -= 1
                count += 1
                print(f"({posx},{posy})")
                posx -= 2
                posy -= 1
                count += 1
                print(f"({posx},{posy})")
            elif (desx-posx == -4) and (desy-posy == -3):
                posx -= 1
                posy -= 2
                count += 1
                print(f"({posx},{posy})")
                posx -= 1
                posy -= 2
                count += 1
                print(f"({posx},{posy})")
            elif distance(posx-2, posy-1, desx, desy) < distance(posx-1, posy-2, desx, desy):
                posx -= 2
                posy -= 1
                count += 1
                print(f"({posx},{posy})")
            else:
                posx -= 1
                posy -= 2
                count += 1
                print(f"({posx},{posy})")
        elif quadrant == 4:

            if distance(posx, posy, desx, desy) == sqrt(2):
                posx -= 1
                posy -= 2
                print(f"({posx},{posy})")
                posx += 2
                posy += 1
                print(f"({posx},{posy})")
                count += 2
                return count
            elif (desx-posx == 3) and (desy-posy == -4):
                posx += 2
                posy -= 1
                count += 1
                print(f"({posx},{posy})")
                posx += 2
                posy -= 1
                count += 1
                print(f"({posx},{posy})")
            elif (desx-posx == 4) and (desy-posy == -3):
                posx += 1
                posy -= 2
                count += 1
                print(f"({posx},{posy})")
                posx += 1
                posy -= 2
                count += 1
                print(f"({posx},{posy})")
            elif distance(posx+2, posy-1, desx, desy) < distance(posx+1, posy-2, desx, desy):
                posx += 2
                posy -= 1
                count += 1
                print(f"({posx},{posy})")
            else:
                posx += 1
                posy -= 2
                count += 1
                print(f"({posx},{posy})")

    return count  # returns the number of moves needed to reach the destination


print(Minimum_Knight_Movement(0, 0, 15, 15))
