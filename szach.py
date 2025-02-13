import legalnosc
import game_model


def check_szach(biale_figury, czarne_figury, x, y, vec_x, vec_y, tura, moves):
    if tura % 2 == 0:
        figura_1 = biale_figury.copy()
        figura_2 = czarne_figury.copy()
    else:
        figura_1 = czarne_figury.copy()
        figura_2 = biale_figury.copy()
    if szach_logic(figura_1, figura_2, x, y, vec_x, vec_y, tura, moves):
        return 1


def szach_logic(figura_1, figura_2, x, y, vec_x, vec_y, tura, moves):
    attack = []
    for i, figura in enumerate(figura_1):
        if figura[2] == x and figura[3] == y and figura[1] == 1:
            figura_list = list(figura)
            figura_list[2] += vec_x
            figura_list[3] += vec_y
            figura_1[i] = tuple(figura_list)
            break
    for i, figura in enumerate(figura_2):
        if figura[2] == x + vec_x and figura[3] == y + vec_y and figura[1] == 1:
            figura_list = list(figura)
            figura_list[1] = 0
            figura_2[i] = tuple(figura_list)
            break
    if tura % 2 == 0:
        figura_1_check, figura_2_check = game_model.pozycje(figura_1, figura_2)
    else:
        figura_2_check, figura_1_check = game_model.pozycje(figura_2, figura_1)
    for figura in figura_2:
        if figura[1] == 1:
            for xx in range(-7, 8):
                for yy in range(-7, 8):
                    if figura[2] + xx >= 0 and figura[2] + xx <= 7 and figura[3] + yy >= 0 and figura[3] + yy <= 7:
                        if tura % 2 == 0:
                            if legalnosc.check_check(figura_1, figura_2, figura_1_check, figura_2_check, figura[2], figura[3], xx, yy, tura+1, moves):
                                attack.append((figura[2]+xx, figura[3]+yy))
                        else:
                            if legalnosc.check_check(figura_2, figura_1, figura_2_check, figura_1_check, figura[2], figura[3], xx, yy, tura+1, moves):
                                attack.append((figura[2]+xx, figura[3]+yy))
    for figura in figura_1:
        if figura[0] == 'K':
            if (figura[2], figura[3]) in attack:
                print('Szach')
                return 1


def check_mat(biale_figury, czarne_figury, biale_pozycje, czarne_pozycje, tura, moves):
    biale_check = biale_figury.copy()
    czarne_check = czarne_figury.copy()
    if tura % 2 == 0:
        for figura in biale_check:
            if sprawdzenie_szach_mat(biale_figury, czarne_figury, biale_pozycje, czarne_pozycje, biale_check, czarne_check, tura, moves, figura) == 0:
                return 0
    else:
        for figura in czarne_check:
            if sprawdzenie_szach_mat(biale_figury, czarne_figury, biale_pozycje, czarne_pozycje, biale_check, czarne_check, tura, moves, figura) == 0:
                return 0
    return 1


def sprawdzenie_szach_mat(biale_figury, czarne_figury, biale_pozycje, czarne_pozycje, biale_check, czarne_check, tura, moves, figura):
    if figura[1] == 1:
        for xx in range(-7, 8):
            for yy in range(-7, 8):
                if figura[2] + xx >= 0 and figura[2] + xx <= 7 and figura[3] + yy >= 0 and figura[3] + yy <= 7:
                    if legalnosc.check_check(biale_check, czarne_check, biale_pozycje, czarne_pozycje, figura[2], figura[3], xx, yy, tura, moves) in {1, 2, 3}:
                        if check_szach(biale_figury, czarne_figury, figura[2], figura[3], xx, yy, tura, moves) != 1:
                            print(figura[2], figura[3])
                            print(xx, yy)
                            return 0
