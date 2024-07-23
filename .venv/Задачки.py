
rubkop_mysh = float(input())
rubkop_shena = float(input())

print((rubkop_mysh+rubkop_shena)//100 *10)
print(((rubkop_mysh+rubkop_shena)%100 *10)/100) #последнее действие просто сведение рублевого эквивалента к копейкам

'''
otpysk = (rubkop_mysh+rubkop_shena)//100 *10 +((rubkop_mysh+rubkop_shena)%100 *10)/100
eda = (rubkop_mysh+rubkop_shena) //100 *30 + ((rubkop_mysh+rubkop_shena)%100 *30)/100
kommun = (rubkop_mysh+rubkop_shena) //100 *5 + ((rubkop_mysh+rubkop_shena)%100 *5)/100
dosyg = (rubkop_mysh+rubkop_shena) //100 * 15 + ((rubkop_mysh+rubkop_shena)%100 *15)/100
nakop = (rubkop_mysh+rubkop_shena) //100 *40 + ((rubkop_mysh+rubkop_shena)%100 *40)/100
'''
otpysk = ((rubkop_mysh+rubkop_shena)//100 *10 +((rubkop_mysh+rubkop_shena)%100 *10)/100)
otpysk_polykopeika = int((otpysk - int(otpysk)) * 1000 % 10) #ура третий порядок (это полукопейка)
otpysk2 = int( ((otpysk - int(otpysk)) * 1000 - float(otpysk - int(otpysk) * 1000))  % 10)
print(otpysk - otpysk2 / 1000)

'''
otpysk_itog = otpysk - otpysk_polykopeika / 1000 -

eda = ((rubkop_mysh+rubkop_shena) //100 *30 + ((rubkop_mysh+rubkop_shena)%100 *30)/100)
eda_polykopeika = int((eda - int(eda)) * 1000 % 10)
eda2 = int((eda - int(eda)) * 1000 % 10)
eda_itog = eda - eda2 / 1000

kommun = ((rubkop_mysh+rubkop_shena) //100 *5 + ((rubkop_mysh+rubkop_shena)%100 *5)/100)
kommun_polykopeika = int((kommun - int(kommun)) * 1000 % 10)
kommun_itog = kommun - kommun_polykopeika2 / 1000

dosyg = ((rubkop_mysh+rubkop_shena) //100 * 15 + ((rubkop_mysh+rubkop_shena)%100 *15)/100)
dosyg_polykopeika = int((dosyg - int(dosyg)) * 1000 % 10)
dosyg_itog = dosyg - dosyg_polykopeika2 / 1000

nakop = ((rubkop_mysh+rubkop_shena) //100 *40 + ((rubkop_mysh+rubkop_shena)%100 *40)/100)
#nakop_polykopeika = int((nakop - int(nakop)) * 1000 % 10)



print('Отпуск:',otpysk_itog)
print('Пропитание и еда:',eda_itog)
print('Коммунальные платежи:',kommun_itog)
print('Досуг:',dosyg_itog)
print('Накопления:',nakop)
print ('Results(Проверка):',otpysk+eda+dosyg+nakop+kommun)
'''
print()