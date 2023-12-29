while True: 
    asmens_kodas = input("Iveskite asmens koda arba exit:")
    if asmens_kodas == 'exit':
        print("viso gero")
        break
    if not asmens_kodas.isnumeric() or len(asmens_kodas) != 11:
        print("Iveskite 11 skaitmenu")
        continue
    menuo = int(asmens_kodas[3:5])
    print('menuo:',menuo)
    if menuo < 1 or menuo > 12:
        print('Neteisingas, menuo negali but daugiau uz 12 arba lygus 0')
        continue
    diena = int(asmens_kodas[5:7] )
    print('diena:', diena)
    if diena < 1 or diena > 31:
        print('Neteisingai, diena negali  but didesne nei 31 arbas lygus 0')
        continue
    kontrolinis = 0
    daugikliai = '1234567891'
    kiti_daugikliai = '3456789123'
    for daugiklio_nr, skaitmuo in enumerate(asmens_kodas[:10]):
        kontrolinis += int(skaitmuo) * int(daugikliai[daugiklio_nr])
    print('kontrolinis:', kontrolinis, kontrolinis % 11)
    if kontrolinis % 11 == 10:
        for daugiklio_nr, skaitmuo in enumerate(asmens_kodas[:10]):
            kontrolinis += int(skaitmuo) * int(kiti_daugikliai[daugiklio_nr])
        tikrininamas = kontrolinis % 11
    print('sekantis kontrolinis:', kontrolinis, kontrolinis % 11)
    tikrininamas = kontrolinis % 11
    if tikrininamas == 10:
        tikrininamas = 0
    paskutinis = int(asmens_kodas[10])
    if paskutinis != tikrininamas:
        print('Neteisingas: paskutinis skaicius klaidingas')
        continue
    print('Tesingas')