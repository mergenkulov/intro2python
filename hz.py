# -*- coding: utf-8 -*-
from random import randint
print u"тебе надо угадать число которое я загадаю. АХАХАХАХА"
print u"Введи предел чисел"
n = int(raw_input(">>>"))
x=randint(0,n)
logic = 0
popitka = 1
while (logic !=1):
    print u"ВЕдите ЧИсло"
    inp=int(raw_input(">>>"))
    if x == inp:
	    print u"Ты красавчик"
	    logic=1
    else:
	    print u"Вы приграли"
	    popitka +=1