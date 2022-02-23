if __name__ == '__main__':
    cnp = input("Introdu CNP-ul: ")
# oare este formatul de cnp corect, cifre sa fie exact 13 and so on
    if len(cnp) != 13:
        if cnp.isdigit() is False:
            print('Baga Numai Numere Dilaule')
        print('Format CNP invalid')
# Sa verifica asa cum erau in tabel
    else:
        sex = cnp[0]
        an = cnp[1:3]
        luna = cnp[3:5]
        zi = cnp[5:7]
        jj = cnp[7:9]
        nnn = cnp[9:12]
        c = cnp[-1]

        sex_ok = '1' <= sex <= '9'
        an_ok = '00' <= an <= '99'
        luna_ok = '01' <= luna <= '12'
        zi_ok = '01' <= zi <= '31'
        jj_ok = '01' <= jj <= '52'
        nnn_ok = '001' <= nnn <= '999'

        c_control = 0
        nr_control = '279146358279'
        for index, i in enumerate(cnp[:12]):
            c_control += int(i) * int(nr_control[index])
# sa fie cu rest de 11 imparteala de control
        c_control = c_control % 11

        if c_control == 10:
            c_control = 1

        c_ok = c_control == int(c)
# show pleb his result
        if sex_ok and an_ok and luna_ok and zi_ok and jj_ok and nnn_ok and c_ok:
            print("CNP Valid, esti safe")
        else:
            print("CNP INVALID")
