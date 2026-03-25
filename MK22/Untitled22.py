import string

tekst = "Kvsyt$sj$Evq}w$H$Exxego$Iriq}$ex${{ss$sr$wigxsv$KYPS"
klucz = int(4)


def szyfr_cezara(tekst, klucz):
    ostateczne=""
    for _ in tekst:
#        print(_)
        numer = ord(_)
        dodanie = numer - klucz
        zaszyfrowany = chr(dodanie)
        ostateczne += zaszyfrowany
    return(ostateczne)

print(szyfr_cezara(tekst, klucz))
        

#def rozszyfr_cezara(tekst, klucz):
#    ostateczne=""
#    for _ in tekst:
#        print(_)
#        numer = ord(_)
#        dodanie = numer - klucz
#        zaszyfrowany = chr(dodanie)
#        ostateczne += zaszyfrowany
#    return(ostateczne)

#print(szyfr_cezara(tekst, klucz))        

# ymene kcattA
#Attack enemy