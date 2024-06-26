def calc_points(points):

    result = 0

    score = {
        "1":0,
        "2":0,
        "3":0,
        "4":0,
        "5":0,
        "6":0,
    }

    for p in points:
        score[str(p)] += 1

    a = score["1"]
    b = score["2"]
    c = score["3"]
    d = score["4"]
    e = score["5"]
    f = score["6"]

    if a and b and c and d and e and f == 1:
        result += 1500
        
    elif a and b and c and d and e >= 1:

        if a == 2:
            result += 100
        elif e == 2:
            result += 50
        
        result += 500
    
    elif b and c and d and e and f >= 1:

        if a == 2:
            result += 100
        elif e == 2:
            result += 50
        
        result += 750

    for k in score:
        if score[k] < 3:

            if int(k) == 1:
                result += 100 * score[k]
            elif int(k) == 5:
                result += 50 * score[k]

        if score[k] == 3:
            if int(k) == 1:
                result += 1000
            else:
                result += int(k) * 100

        elif score[k] == 4:
            if int(k) == 1:
                result += 2000
            else:
                result += int(k) * 100 * 2

        elif score[k] == 5:
            if int(k) == 1:
                result += 4000
            else:
                result += int(k) * 100 * 4

        elif score[k] == 6:
            if int(k) == 1:
                result += 8000
            else:
                result += int(k) * 100 * 8

    return result