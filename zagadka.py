# -*- coding: utf-8 -*-
print u"Перед вами две двери. ОдНА темная(1), друГАя сВетлАя(2). В какую ЗайДете?"
door=raw_input(">>>")

if door == "1":
    print u"ТАм сИдит БегЛый Зэк, и ТОчиТ БутеР. Что ты сДелаЕшь?"
    print u"1. ЗабЕРЕшь буТЕр."
    print u"2. УдаРИшь ЗэКА."

    zek = raw_input(">>>")

    if zek == "1":
        print u"Он сЬеСт тебя."
    elif zek == "2":
    	print u"ЗасТавИть Тебя ЗареЗаться."
    else:
    	print u"Он тебя признал."

elif door == "2":
	print u"Стоит сТол , нА стОле ЗВониТ теЛефон. Ваши действия?"
    print u"1. вОзьмешь трубку."
    print u"2. ОтМенишь вызоВ."
    print u"РазобьешЬ ТеЛефоН."
    trubka = raw_input(">>>")

    if trubka == "1" or trubka == "2":
    	print u"ТебЕ пОзвонил ЗэК из соседней двеРИ"
    else:
    	print u"ЗэК пРИшел За тоБОЙ"

else:
	print "Разбил телефон и ЗакРЫЛ дВЕРь. ТЫ ВыйГрал!!!"
