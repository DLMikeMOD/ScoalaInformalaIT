# if __name__ == '__main__':
#     cnp = input("Introdu CNP-ul: ")
# # oare este formatul de cnp corect, cifre sa fie exact 13 and so on
#     if len(cnp) != 13:
#         if cnp.isdigit() is False:
#             print('Baga Numai Numere Dilaule')
#         print('Format CNP invalid')
# # Sa verifica asa cum erau in tabel
#     else:
#         sex = cnp[0]
#         an = cnp[1:3]
#         luna = cnp[3:5]
#         zi = cnp[5:7]
#         jj = cnp[7:9]
#         nnn = cnp[9:12]
#         c = cnp[-1]
#
#         sex_ok = '1' <= sex <= '9'
#         an_ok = '00' <= an <= '99'
#         luna_ok = '01' <= luna <= '12'
#         zi_ok = '01' <= zi <= '31'
#         jj_ok = '01' <= jj <= '52'
#         nnn_ok = '001' <= nnn <= '999'
#
#         c_control = 0
#         nr_control = '279146358279'
#         for index, i in enumerate(cnp[:12]):
#             c_control += int(i) * int(nr_control[index])
# # sa fie cu rest de 11 imparteala de control
#         c_control = c_control % 11
#
#         if c_control == 10:
#             c_control = 1
#
#         c_ok = c_control == int(c)
# # show pleb his result
#         if sex_ok and an_ok and luna_ok and zi_ok and jj_ok and nnn_ok and c_ok:
#             print("CNP Valid, esti safe")
#         else:
#             print("CNP INVALID")

import datetime


class Validator:
    def __init__(self, cnp):
        self.CNP = cnp

    def Lungime(self):
        if len(self.CNP) != 13:
            return False
        return True

    def Sex(self):
        s = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        if self.Sex in s:
            return False
        return True

    def Date(self):
        try:
            date = self.CNP[1:7]
            if datetime.datetime.strptime(date, "%y%m%d"):
                return True
        except ValueError:
            return False

    def Judet(self):
        jud = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
               '16',
               '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31',
               '32',
               '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '51',
               '52']
        if self.CNP[7:9] in jud:
            return True
        return False

    def NNN(self):
        n1 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        n2 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        n3 = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        if self.CNP[9] in n1 and self.CNP[10] in n2 and self.CNP[11] in n3:
            return True
        return False

    def cifcontrol(self):
        intcnp = int(self.CNP[-1])
        val = '279146358279'
        cnpc = 0
        for i, v in enumerate(val):
            cnpc += int(v) * int(self.CNP[i])
        rest = cnpc % 11
        if rest == 10:
            rest = 1
        else:
            rest = rest
        if intcnp == rest:
            return True
        return False

    def format(self):
        if self.CNP.isdigit():
            return True
        return False

    def __str__(self):
        if self.Lungime() and self.Sex() and self.Date() and self.Judet() and self.NNN() and self.cifcontrol() and self.format() is True:
            return f'CNP: {self.CNP} este valid.'
        return f'CNP: {self.CNP} nu este valid.'


cnp_input = input('Introdu CNP: ')
obiect_1 = Validator(cnp_input)
print(obiect_1)
