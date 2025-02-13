import legalnosc
import szach


def move(biale_figury, czarne_figury, biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, tura, moves):

    legality = legalnosc.check_check(biale_figury, czarne_figury, biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, tura, moves)

    if legality:
        if szach.check_szach(biale_figury, czarne_figury, x, y, vec_x, vec_y, tura, moves) != 1:
            if tura % 2 == 0:
                figury = biale_figury.copy()
                kolor = 'biale'
                figury_orginal = biale_figury
                figura_dwa = czarne_figury
            else:
                figury = czarne_figury.copy()
                kolor = 'czarne'
                figury_orginal = czarne_figury
                figura_dwa = biale_figury

            move_logic(figury, legality, x, y, vec_x, vec_y, moves, figury_orginal, figura_dwa, kolor)

            return 1

def move_logic(figury, legality, x, y, vec_x, vec_y, moves, figury_orginal, figura_dwa, kolor):
    for i, figura in enumerate(figury):
        # Convert tuple to list
        figura_list = list(figura)
        # wybor figury
        if figura_list[2] == x and figura_list[3] == y and figura_list[1] == 1:
            if legality == 2:
                moves.append((kolor, 'Pe', x, y, x+vec_x, y+vec_y))
            elif legality == 3:
                moves.append((kolor, 'O-O', x, y, x+vec_x, y+vec_y))
            else:
                moves.append((kolor, figura[0], x, y, x+vec_x, y+vec_y))

            figura_list[2] += vec_x
            figura_list[3] += vec_y

            if legality == 3:
                for j, wieza in enumerate(figury_orginal):
                    if wieza[2] == figura_list[2] + 2 and wieza[3] == figura_list[3] and wieza[1] == 1:
                        wieza_list = list(wieza)
                        wieza_list[2] -= 3
                        figury_orginal[j] = tuple(wieza_list)
                        break
                    elif wieza[2] == figura_list[2] - 1 and wieza[3] == figura_list[3] and wieza[1] == 1:
                        wieza_list = list(wieza)
                        wieza_list[2] += 2
                        figury_orginal[j] = tuple(wieza_list)
                        break

            #promocja pionka
            if kolor == 'biale':
                if figura_list[3] == 7 and figura_list[0] == 'P':
                    figura_list[0] = 'D'
            elif kolor == 'czarne':
                if figura_list[3] == 0 and figura_list[0] == 'P':
                    figura_list[0] = 'D'

            # Convert list back to tuple
            figury_orginal[i] = tuple(figura_list)

            for j, figura_odwrotna in enumerate(figura_dwa):
                odwrotna_figura_list = list(figura_odwrotna)
                if legality == 2:
                    if odwrotna_figura_list[2] == x + vec_x and odwrotna_figura_list[3] == y and odwrotna_figura_list[1] == 1:
                        odwrotna_figura_list[1] = 0
                        figura_dwa[j] = tuple(odwrotna_figura_list)
                        break
                elif odwrotna_figura_list[2] == x + vec_x and odwrotna_figura_list[3] == y + vec_y and odwrotna_figura_list[1] == 1:
                    odwrotna_figura_list[1] = 0
                    figura_dwa[j] = tuple(odwrotna_figura_list)
                    break
