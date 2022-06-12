from math import sqrt


def KnightMovement(posx, posy):  # gives all the possible moves of the knight from a point
    posx1 = posx + 1
    posy1 = posy + 2

    posx2 = posx1
    posy2 = posy - 2

    posx3 = posx - 1
    posy3 = posy1

    posx4 = posx3
    posy4 = posy2

    posx5 = posx + 2
    posy5 = posy + 1

    posx6 = posx - 2
    posy6 = posy5

    posx7 = posx5
    posy7 = posy - 1

    posx8 = posx6
    posy8 = posy7

    # retuns all the 8 possible moves
    return (posx1, posy1), (posx2, posy2), (posx3, posy3), (posx4, posy4), (posx5, posy5), (posx6, posy6), (posx7, posy7), (posx8, posy8)


def MinKnightMovement(posx, posy, desx, desy):
    count = 1  # defining a variable that keeps count of the number of moves we need to make
    # making a list of the values that we get back
    listcount = list(KnightMovement(posx, posy))
    if (desx, desy) in listcount:  # we check if we can reach the des x and y in one move
        return count  # return 1
    else:  # if we cant reach it in one move
        while (desx, desy) not in listcount:  # make an infinte loop untill we get back the destination
            # we make a loop that give us all the possible second solutions
            for i in range(len(listcount)):
                listcount.extend(list(KnightMovement(
                    listcount[i][0], listcount[i][1])))  # we extend the list by adding the other possibilities
            count += 1  # increases the count ( we made an extra move)
        return count  # returns the number of moves needed to reach the destination


print(MinKnightMovement(0, 0, 3, 0))
