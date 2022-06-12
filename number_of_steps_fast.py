def no_of_steps(posx, posy, desx, desy):

    x = 0
    y = 0
    count = 0
    grouped = False

    if (posx == desx) and (posy == desy):
        return count

    # reordering x and y where x < y and making their values positive
    if abs(posx-desx) > abs(posy-desy):
        x = abs(posy-desy)
        y = abs(posx-desx)
    else:
        x = abs(posx-desx)
        y = abs(posy-desy)

    if x == 2 and y == 2:
        count += 4
        return count

    if x == 0:
        if y == 1:
            count += 3
            return count
        elif y == 2:
            count += 2
            return count
        elif y == 3:
            count += 3
            return count
        else:
            x == 2

    xy = x + y  # sum

    if y == x*2:
        return x
    elif y > x*2:
        grouped = True
    else:
        grouped = False

    if grouped:
        temp = y - 2*x
        count = temp//4
        count = x + 2*count
        count = count + (temp % 4)
        return count
    else:
        if xy % 2 == 0:
            count = xy/2
            count = (count-1)//3
            count += 1
            count *= 2
            return int(count)
        else:
            count = (xy + 1)/2
            count = count//3
            count += 1
            count = (2*count - 1)
            return int(count)


print(no_of_steps(0, 0, 15, 15))
