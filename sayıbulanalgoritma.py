dizi=[25,35,15,20,45,50,125,78,456,7]
toplam=50
kontrol=False
for i in range(len(dizi)):
    if kontrol==True:
        break
    else:
        ilkeleman=dizi[i]
        for j in range(len(dizi)):
            if j==i:
                pass
            else:
                sonuc =ilkeleman+dizi[j]
                if sonuc==toplam:
                    kontrol=True
                    print("ilk sayı=",ilkeleman," indis=",i,"\n","ikinci sayı=",dizi[j]," indis=",j)
                    break
