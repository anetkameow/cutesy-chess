def kolizja(x, y, vec_x, vec_y, biale_pozycje, czarne_pozycje, kolor):
    xx, yy = 0, 0
    if vec_x > 1 or vec_x < -1 or vec_y > 1 or vec_y < -1:
        while xx <= vec_x - 2 or xx >= vec_x + 2 or yy <= vec_y - 2 or yy >= vec_y + 2:
            if vec_x > 0 and vec_x > xx:
                xx += 1
            elif vec_x < 0 and vec_x < xx:
                xx -= 1
            if vec_y > 0 and vec_y > yy:
                yy += 1
            elif vec_y < 0 and vec_y < yy:
                yy -= 1

            if (x+xx, y+yy) in biale_pozycje or (x+xx, y+yy) in czarne_pozycje:
                return False
    if kolor == 'biale':
        if (x+vec_x, y+vec_y) not in biale_pozycje:
            return 1
    if kolor == 'czarne':
        if (x+vec_x, y+vec_y) not in czarne_pozycje:
            return 1


def check_check(biale_figury, czarne_figury, biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, tura, moves):
    nazwa = ''
    kolor = ''

    if tura % 2 == 0:
        kolor = 'biale'
        for figura in biale_figury:
            if figura[2] == x and figura[3] == y and figura[1] == 1:
                nazwa = figura[0]
                break
    else:
        kolor = 'czarne'
        for figura in czarne_figury:
            if figura[2] == x and figura[3] == y and figura[1] == 1:
                nazwa = figura[0]
                break

    if nazwa == 'P' and check_P(biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, kolor, moves) == 1:
        return 1
    elif nazwa == 'P' and check_P(biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, kolor, moves) == 2:
        return 2
    elif nazwa == 'W' and check_W(biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, kolor):
        return 1
    elif nazwa == 'S' and check_S(biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, kolor):
        return 1
    elif nazwa == 'G' and check_G(biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, kolor):
        return 1
    elif nazwa == 'K' and check_K(biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, kolor, moves) == 1:
        return 1
    elif nazwa == 'K' and check_K(biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, kolor, moves) == 3:
        return 3
    elif nazwa == 'D' and check_D(biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, kolor):
        return 1


def check_P(biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, kolor, moves):
    if kolor == 'biale':
        #en passant
        if y == 4 and vec_y == 1 and abs(vec_x) == 1:
            if moves[-1][0] == 'czarne' and moves[-1][1] == 'P' and moves[-1][2] == x+vec_x and moves[-1][3] == y+2 and moves[-1][4] == x+vec_x and moves[-1][5] == y:
                return 2
        #ruchy pionka o 2 pola
        if y == 1 and vec_y == 2 and vec_x == 0:
            if (x, y+1) not in biale_pozycje and (x, y+1) not in czarne_pozycje:
                if (x, y+2) not in biale_pozycje and (x, y+2) not in czarne_pozycje:
                    return 1
        #ruch o 1 pole
        if vec_y == 1 and vec_x == 0:
            if (x, y+1) not in biale_pozycje and (x, y+1) not in czarne_pozycje:
                return 1
        #bicie
        if vec_y == 1 and abs(vec_x) == 1:
            if (x+vec_x, y+1) in czarne_pozycje:
                return 1

    if kolor == 'czarne':
        #en passant
        if y == 3 and vec_y == -1 and abs(vec_x) == 1:
            if moves[-1][0] == 'biale' and moves[-1][1] == 'P' and moves[-1][2] == x+vec_x and moves[-1][3] == y-2 and moves[-1][4] == x+vec_x and moves[-1][5] == y:
                return 2
        #ruchy pionka o 2 pola
        if y == 6 and vec_y == -2 and vec_x == 0:
            if (x, y-1) not in biale_pozycje and (x, y-1) not in czarne_pozycje:
                if (x, y-2) not in biale_pozycje and (x, y-2) not in czarne_pozycje:
                    return 1
        #ruch o 1 pole
        if vec_y == -1 and vec_x == 0:
            if (x, y-1) not in biale_pozycje and (x, y-1) not in czarne_pozycje:
                return 1
        #bicie
        if vec_y == -1 and abs(vec_x) == 1:
            if (x+vec_x, y-1) in biale_pozycje:
                return 1


def check_W(biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, kolor):
    if vec_x == 0 or vec_y == 0:
        if kolizja(x, y, vec_x, vec_y, biale_pozycje, czarne_pozycje, kolor):
            return 1


def check_S(biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, kolor):
    if abs(vec_x) == 1 and abs(vec_y) == 2 or abs(vec_x) == 2 and abs(vec_y) == 1:
        if kolor == 'biale':
            if (x+vec_x, y+vec_y) not in biale_pozycje:
                return 1
        if kolor == 'czarne':
            if (x+vec_x, y+vec_y) not in czarne_pozycje:
                return 1


def check_G(biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, kolor):
    if abs(vec_x) == abs(vec_y):
        if kolizja(x, y, vec_x, vec_y, biale_pozycje, czarne_pozycje, kolor):
            return 1


def check_K(biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, kolor, moves):
    if kolor == 'biale':
        #ruchy krola
        if abs(vec_x) <= 1 and abs(vec_y) <= 1:
            if (x+vec_x, y+vec_y) not in biale_pozycje:
                return 1
        if not any(move[0] == 'biale' and move[1] == 'K' for move in moves):
            if vec_x == 2 and vec_y == 0:
                if not any(move[0] == 'biale' and move[1] == 'W' and move[2] == 7 for move in moves):
                    if (6, 0) not in biale_pozycje and (5, 0) not in biale_pozycje and (4, 0) not in biale_pozycje:
                        if (6, 0) not in czarne_pozycje and (5, 0) not in czarne_pozycje and (4, 0) not in czarne_pozycje:
                            return 3
            if vec_x == -2 and vec_y == 0:
                if not any(move[0] == 'biale' and move[1] == 'W' and move[2] == 0 for move in moves):
                    if (1, 0) not in biale_pozycje and (2, 0) not in biale_pozycje:
                        if (1, 0) not in czarne_pozycje and (2, 0) not in czarne_pozycje:
                            return 3
    if kolor == 'czarne':
        #ruchy krola
        if abs(vec_x) <= 1 and abs(vec_y) <= 1:
            if (x+vec_x, y+vec_y) not in czarne_pozycje:
                return 1
        if not any(move[0] == 'czarne' and move[1] == 'K' for move in moves):
            if vec_x == 2 and vec_y == 0:
                if not any(move[0] == 'czarne' and move[1] == 'W' and move[2] == 7 for move in moves):
                    if (6, 7) not in czarne_pozycje and (5, 7) not in czarne_pozycje and (4, 7) not in czarne_pozycje:
                        if (6, 7) not in biale_pozycje and (5, 7) not in biale_pozycje and (4, 7) not in biale_pozycje:
                            return 3
            if vec_x == -2 and vec_y == 0:
                if not any(move[0] == 'czarne' and move[1] == 'W' and move[2] == 0 for move in moves):
                    if (1, 7) not in czarne_pozycje and (2, 7) not in czarne_pozycje:
                        if (1, 7) not in biale_pozycje and (2, 7) not in biale_pozycje:
                            return 3


def check_D(biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, kolor):
    if abs(vec_x) == abs(vec_y) or vec_x == 0 or vec_y == 0:
        if kolizja(x, y, vec_x, vec_y, biale_pozycje, czarne_pozycje, kolor):
            return 1
