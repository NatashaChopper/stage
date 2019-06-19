import numpy
with open ("dic.txt", "w", encoding="utf-8") as dic:

    for x in range(5, 790, 1):
        if 92 < x <= 113:
            dic.write('"'+str(x)+'"'+":"+ '"'+'1'+'",')
        elif 113 < x <= 133:
            dic.write('"'+str(x)+'"'+":"+ '"'+'2'+'",')
        elif 133 < x <= 153:
            dic.write('"'+str(x)+'"'+":"+ '"'+'3'+'",')
        elif 153 < x <= 173:
            dic.write('"'+str(x)+'"'+":"+ '"'+'4'+'",')
        elif 173 < x <= 193:
            dic.write('"'+str(x)+'"'+":"+ '"'+'5'+'",')
        elif 193 < x <= 213:
            dic.write('"'+str(x)+'"'+":"+ '"'+'6'+'",')
        elif 213 < x <= 233:
            dic.write('"'+str(x)+'"'+":"+ '"'+'7'+'",')
        elif 233 < x <= 253:
            dic.write('"'+str(x)+'"'+":"+ '"'+'8'+'",')
        elif 253 < x <= 273:
            dic.write('"'+str(x)+'"'+":"+ '"'+'9'+'",')
        elif 273 < x <= 293:
            dic.write('"'+str(x)+'"'+":"+ '"'+'10'+'",')
        elif 293 < x <= 313:
            dic.write('"'+str(x)+'"'+":"+ '"'+'11'+'",')
        elif 313 < x <= 333:
            dic.write('"'+str(x)+'"'+":"+ '"'+'12'+'",')
        elif 333 < x <= 353:
            dic.write('"'+str(x)+'"'+":"+ '"'+'13'+'",')
        elif 353 < x <= 373:
            dic.write('"'+str(x)+'"'+":"+ '"'+'14'+'",')
        elif 373 < x <= 393:
            dic.write('"'+str(x)+'"'+":"+ '"'+'15'+'",')
        elif 393 < x <= 413:
            dic.write('"'+str(x)+'"'+":"+ '"'+'16'+'",')
        elif 413 < x <= 433:
            dic.write('"'+str(x)+'"'+":"+ '"'+'17'+'",')
        elif 433 < x <= 453:
            dic.write('"'+str(x)+'"'+":"+ '"'+'18'+'",')
        elif 453 < x <= 473:
            dic.write('"'+str(x)+'"'+":"+ '"'+'19'+'",')
        elif 473 < x <= 493:
            dic.write('"'+str(x)+'"'+":"+ '"'+'20'+'",')
        elif 493 < x <= 513:
            dic.write('"'+str(x)+'"'+":"+ '"'+'21'+'",')
        elif 513 < x <= 533:
            dic.write('"'+str(x)+'"'+":"+ '"'+'22'+'",')
        elif 533 < x <= 553:
            dic.write('"'+str(x)+'"'+":"+ '"'+'23'+'",')
        elif 553 < x <= 573:
            dic.write('"'+str(x)+'"'+":"+ '"'+'24'+'",')
        elif 573 < x <= 593:
            dic.write('"'+str(x)+'"'+":"+ '"'+'25'+'",')
        elif 593 < x <= 613:
            dic.write('"'+str(x)+'"'+":"+ '"'+'26'+'",')
        elif 613 < x <= 633:
            dic.write('"'+str(x)+'"'+":"+ '"'+'27'+'",')
        elif 633 < x <= 653:
            dic.write('"'+str(x)+'"'+":"+ '"'+'28'+'",')
        elif 653 < x <= 673:
            dic.write('"'+str(x)+'"'+":"+ '"'+'29'+'",')
        elif 673 < x <= 693:
            dic.write('"'+str(x)+'"'+":"+ '"'+'30'+'",')
        elif 693 < x <= 713:
            dic.write('"'+str(x)+'"'+":"+ '"'+'31'+'",')
        elif 713 < x <= 733:
            dic.write('"'+str(x)+'"'+":"+ '"'+'32'+'",')
        elif 733 < x <= 753:
            dic.write('"'+str(x)+'"'+":"+ '"'+'33'+'",')
        elif 753 < x <= 773:
            dic.write('"'+str(x)+'"'+":"+ '"'+'34'+'",')
        elif 773 < x <= 793:
            dic.write('"'+str(x)+'"'+":"+ '"'+'35'+'",')
        elif 4 < x <= 15:
            dic.write('"'+str(x)+'"'+":"+ '"'+'36'+'",')
        elif 15 < x <= 25:
            dic.write('"'+str(x)+'"'+":"+ '"'+'37'+'",')
        elif 25 < x <= 35:
            dic.write('"'+str(x)+'"'+":"+ '"'+'38'+'",')
        elif 35 < x <= 45:
            dic.write('"'+str(x)+'"'+":"+ '"'+'39'+'",')
        elif 45 < x <= 55:
            dic.write('"'+str(x)+'"'+":"+ '"'+'40'+'",')
        elif 55 < x <= 65:
            dic.write('"'+str(x)+'"'+":"+ '"'+'41'+'",')
        elif 65 < x <= 75:
            dic.write('"'+str(x)+'"'+":"+ '"'+'42'+'",')
        elif 75 < x <= 85:
            dic.write('"'+str(x)+'"'+":"+ '"'+'43'+'",')
        elif 85 < x <= 92:
            dic.write('"'+str(x)+'"'+":"+ '"'+'44'+'",')
        
with open ("time.txt", "w", encoding="utf-8") as duree:
    for y in numpy.arange(0, 1.7, 0.01):
        if 0 < y <= 0.1:
            duree.write('"'+str(y)+'"'+":"+ '"'+'80'+'",')
        elif 0.1 < y <= 0.2:
            duree.write('"'+str(y)+'"'+":"+ '"'+'81'+'",')
        elif 0.2 < y <= 0.3:
            duree.write('"'+str(y)+'"'+":"+ '"'+'82'+'",')
        elif 0.3 < y <= 0.4:
            duree.write('"'+str(y)+'"'+":"+ '"'+'83'+'",')
        elif 0.4 < y <= 0.5:
            duree.write('"'+str(y)+'"'+":"+ '"'+'84'+'",')
        elif 0.5 < y <= 0.6:
            duree.write('"'+str(y)+'"'+":"+ '"'+'85'+'",')
        elif 0.6 < y <= 0.7:
            duree.write('"'+str(y)+'"'+":"+ '"'+'86'+'",')
        elif 0.7 < y <= 0.8:
            duree.write('"'+str(y)+'"'+":"+ '"'+'87'+'",')
        elif 0.8 < y <= 0.9:
            duree.write('"'+str(y)+'"'+":"+ '"'+'88'+'",')
        elif 0.9 < y <= 1:
            duree.write('"'+str(y)+'"'+":"+ '"'+'89'+'",')
        elif 1 < y <= 1.1:
            duree.write('"'+str(y)+'"'+":"+ '"'+'90'+'",')
        elif 1.1 < y <= 1.2:
            duree.write('"'+str(y)+'"'+":"+ '"'+'91'+'",')
        elif 1.2 < y <= 1.3:
            duree.write('"'+str(y)+'"'+":"+ '"'+'92'+'",')
        elif 1.3 < y <= 1.4:
            duree.write('"'+str(y)+'"'+":"+ '"'+'93'+'",')
        elif 1.4 < y <= 1.5:
            duree.write('"'+str(y)+'"'+":"+ '"'+'94'+'",')
        elif 1.5 < y <= 1.6:
            duree.write('"'+str(y)+'"'+":"+ '"'+'95'+'",')
        elif 1.6 < y <= 1.7:
            duree.write('"'+str(y)+'"'+":"+ '"'+'96'+'",')