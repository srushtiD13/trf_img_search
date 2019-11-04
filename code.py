import cv2
oimgb=cv2.imread('bch2.jpeg')#query img
oimgb=cv2.resize(oimgb,(200,200))
a=29 #number of bins
b=0.5 #threshold
reslist=[]

#dataset
oimgt1=cv2.imread('bch1.jpeg')
oimgt1=cv2.resize(oimgt1,(200,200))
oimgt2=cv2.imread('bch2.jpeg')
oimgt2=cv2.resize(oimgt2,(200,200))
oimgt3=cv2.imread('bch3.jpeg')
oimgt3=cv2.resize(oimgt3,(200,200))
oimgt4=cv2.imread('bch4.jpeg')
oimgt4=cv2.resize(oimgt4,(200,200))
oimgt5=cv2.imread('bch5.jpeg')
oimgt5=cv2.resize(oimgt5,(200,200))
oimgt6=cv2.imread('forest1.jpeg')
oimgt6=cv2.resize(oimgt6,(200,200))
oimgt7=cv2.imread('forest2.jpeg')
oimgt7=cv2.resize(oimgt7,(200,200))
oimgt8=cv2.imread('forest3.jpeg')
oimgt8=cv2.resize(oimgt8,(200,200))
oimgt9=cv2.imread('forest4.jpeg')
oimgt9=cv2.resize(oimgt9,(200,200))
oimgt10=cv2.imread('ros1.jpeg')
oimgt10=cv2.resize(oimgt10,(200,200))
oimgt11=cv2.imread('ros2.jpeg')
oimgt11=cv2.resize(oimgt11,(200,200))
oimgt12=cv2.imread('ros3.jpeg')
oimgt12=cv2.resize(oimgt12,(200,200))
oimgt13=cv2.imread('ros4.jpeg')
oimgt13=cv2.resize(oimgt13,(200,200))
oimgt14=cv2.imread('man1.jpeg')
oimgt14=cv2.resize(oimgt14,(200,200))
oimgt15=cv2.imread('man2.jpeg')
oimgt15=cv2.resize(oimgt15,(200,200))
oimgt16=cv2.imread('man3.jpeg')
oimgt16=cv2.resize(oimgt16,(200,200))
oimgt17=cv2.imread('man4.jpg')
oimgt17=cv2.resize(oimgt17,(200,200))
oimgt18=cv2.imread('man5.jpeg')
oimgt18=cv2.resize(oimgt18,(200,200))
oimgt19=cv2.imread('tgr1.jpeg')
oimgt19=cv2.resize(oimgt19,(200,200))
oimgt20=cv2.imread('tgr2.jpeg')
oimgt20=cv2.resize(oimgt20,(200,200))
oimgt21=cv2.imread('tgr3.jpeg')
oimgt21=cv2.resize(oimgt21,(200,200))
oimgt22=cv2.imread('tgr4.jpeg')
oimgt22=cv2.resize(oimgt22,(200,200))
oimgt23=cv2.imread('tgr5.jpeg')
oimgt23=cv2.resize(oimgt23,(200,200))

#conversion to HSV
imgb=cv2.cvtColor(oimgb,cv2.COLOR_BGR2HSV)
imgt1=cv2.cvtColor(oimgt1,cv2.COLOR_BGR2HSV)
imgt2=cv2.cvtColor(oimgt2,cv2.COLOR_BGR2HSV)
imgt3=cv2.cvtColor(oimgt3,cv2.COLOR_BGR2HSV)
imgt4=cv2.cvtColor(oimgt4,cv2.COLOR_BGR2HSV)
imgt5=cv2.cvtColor(oimgt5,cv2.COLOR_BGR2HSV)
imgt6=cv2.cvtColor(oimgt6,cv2.COLOR_BGR2HSV)
imgt7=cv2.cvtColor(oimgt7,cv2.COLOR_BGR2HSV)
imgt8=cv2.cvtColor(oimgt8,cv2.COLOR_BGR2HSV)
imgt9=cv2.cvtColor(oimgt9,cv2.COLOR_BGR2HSV)
imgt10=cv2.cvtColor(oimgt10,cv2.COLOR_BGR2HSV)
imgt11=cv2.cvtColor(oimgt11,cv2.COLOR_BGR2HSV)
imgt12=cv2.cvtColor(oimgt12,cv2.COLOR_BGR2HSV)
imgt13=cv2.cvtColor(oimgt13,cv2.COLOR_BGR2HSV)
imgt14=cv2.cvtColor(oimgt14,cv2.COLOR_BGR2HSV)
imgt15=cv2.cvtColor(oimgt15,cv2.COLOR_BGR2HSV)
imgt16=cv2.cvtColor(oimgt16,cv2.COLOR_BGR2HSV)
imgt17=cv2.cvtColor(oimgt17,cv2.COLOR_BGR2HSV)
imgt18=cv2.cvtColor(oimgt18,cv2.COLOR_BGR2HSV)
imgt19=cv2.cvtColor(oimgt19,cv2.COLOR_BGR2HSV)
imgt20=cv2.cvtColor(oimgt20,cv2.COLOR_BGR2HSV)
imgt21=cv2.cvtColor(oimgt21,cv2.COLOR_BGR2HSV)
imgt22=cv2.cvtColor(oimgt22,cv2.COLOR_BGR2HSV)
imgt23=cv2.cvtColor(oimgt23,cv2.COLOR_BGR2HSV)


#calculating histogram and normalize
histb=cv2.calcHist([imgb],[0],None,[a],[0,256])
cv2.normalize(histb,histb,0,400,cv2.NORM_MINMAX)

hist1=cv2.calcHist([imgt1],[0],None,[a],[0,256])
cv2.normalize(hist1,hist1,0,400,cv2.NORM_MINMAX)

hist2=cv2.calcHist([imgt2],[0],None,[a],[0,256])
cv2.normalize(hist2,hist2,0,400,cv2.NORM_MINMAX)

hist3=cv2.calcHist([imgt3],[0],None,[a],[0,256])
cv2.normalize(hist3,hist3,0,400,cv2.NORM_MINMAX)

hist4=cv2.calcHist([imgt4],[0],None,[a],[0,256])
cv2.normalize(hist4,hist4,0,400,cv2.NORM_MINMAX)

hist5=cv2.calcHist([imgt5],[0],None,[a],[0,256])
cv2.normalize(hist5,hist5,0,400,cv2.NORM_MINMAX)

hist6=cv2.calcHist([imgt6],[0],None,[a],[0,256])
cv2.normalize(hist6,hist6,0,400,cv2.NORM_MINMAX)

hist7=cv2.calcHist([imgt7],[0],None,[a],[0,256])
cv2.normalize(hist7,hist7,0,400,cv2.NORM_MINMAX)

hist8=cv2.calcHist([imgt8],[0],None,[a],[0,256])
cv2.normalize(hist8,hist8,0,400,cv2.NORM_MINMAX)

hist9=cv2.calcHist([imgt9],[0],None,[a],[0,256])
cv2.normalize(hist9,hist9,0,400,cv2.NORM_MINMAX)

hist10=cv2.calcHist([imgt10],[0],None,[a],[0,256])
cv2.normalize(hist10,hist10,0,400,cv2.NORM_MINMAX)

hist11=cv2.calcHist([imgt11],[0],None,[a],[0,256])
cv2.normalize(hist11,hist11,0,400,cv2.NORM_MINMAX)

hist12=cv2.calcHist([imgt12],[0],None,[a],[0,256])
cv2.normalize(hist12,hist12,0,400,cv2.NORM_MINMAX)

hist13=cv2.calcHist([imgt13],[0],None,[a],[0,256])
cv2.normalize(hist13,hist13,0,400,cv2.NORM_MINMAX)

hist14=cv2.calcHist([imgt14],[0],None,[a],[0,256])
cv2.normalize(hist14,hist14,0,400,cv2.NORM_MINMAX)

hist15=cv2.calcHist([imgt15],[0],None,[a],[0,256])
cv2.normalize(hist15,hist15,0,400,cv2.NORM_MINMAX)

hist16=cv2.calcHist([imgt16],[0],None,[a],[0,256])
cv2.normalize(hist16,hist16,0,400,cv2.NORM_MINMAX)

hist17=cv2.calcHist([imgt17],[0],None,[a],[0,256])
cv2.normalize(hist17,hist17,0,400,cv2.NORM_MINMAX)

hist18=cv2.calcHist([imgt18],[0],None,[a],[0,256])
cv2.normalize(hist18,hist18,0,400,cv2.NORM_MINMAX)

hist19=cv2.calcHist([imgt19],[0],None,[a],[0,256])
cv2.normalize(hist19,hist19,0,400,cv2.NORM_MINMAX)

hist20=cv2.calcHist([imgt20],[0],None,[a],[0,256])
cv2.normalize(hist20,hist20,0,400,cv2.NORM_MINMAX)

hist21=cv2.calcHist([imgt21],[0],None,[a],[0,256])
cv2.normalize(hist21,hist21,0,400,cv2.NORM_MINMAX)

hist22=cv2.calcHist([imgt22],[0],None,[a],[0,256])
cv2.normalize(hist22,hist22,0,400,cv2.NORM_MINMAX)

hist23=cv2.calcHist([imgt23],[0],None,[a],[0,256])
cv2.normalize(hist23,hist23,0,400,cv2.NORM_MINMAX)

#comparing histogram values
res=cv2.compareHist(histb,hist1,cv2.HISTCMP_CORREL)
reslist.append(res)
res1=cv2.compareHist(histb,hist2,cv2.HISTCMP_CORREL)
reslist.append(res1)
res2=cv2.compareHist(histb,hist3,cv2.HISTCMP_CORREL)
reslist.append(res2)
res3=cv2.compareHist(histb,hist4,cv2.HISTCMP_CORREL)
reslist.append(res3)
res4=cv2.compareHist(histb,hist5,cv2.HISTCMP_CORREL)
reslist.append(res4)
res5=cv2.compareHist(histb,hist6,cv2.HISTCMP_CORREL)
reslist.append(res5)
res6=cv2.compareHist(histb,hist7,cv2.HISTCMP_CORREL)
reslist.append(res6)
res7=cv2.compareHist(histb,hist8,cv2.HISTCMP_CORREL)
reslist.append(res7)
res8=cv2.compareHist(histb,hist9,cv2.HISTCMP_CORREL)
reslist.append(res8)
res9=cv2.compareHist(histb,hist10,cv2.HISTCMP_CORREL)
reslist.append(res9)
res10=cv2.compareHist(histb,hist11,cv2.HISTCMP_CORREL)
reslist.append(res10)
res11=cv2.compareHist(histb,hist12,cv2.HISTCMP_CORREL)
reslist.append(res11)
res12=cv2.compareHist(histb,hist13,cv2.HISTCMP_CORREL)
reslist.append(res12)
res13=cv2.compareHist(histb,hist14,cv2.HISTCMP_CORREL)
reslist.append(res13)
res14=cv2.compareHist(histb,hist15,cv2.HISTCMP_CORREL)
reslist.append(res14)
res15=cv2.compareHist(histb,hist16,cv2.HISTCMP_CORREL)
reslist.append(res15)
res16=cv2.compareHist(histb,hist17,cv2.HISTCMP_CORREL)
reslist.append(res16)
res17=cv2.compareHist(histb,hist18,cv2.HISTCMP_CORREL)
reslist.append(res17)
res18=cv2.compareHist(histb,hist19,cv2.HISTCMP_CORREL)
reslist.append(res18)
res19=cv2.compareHist(histb,hist20,cv2.HISTCMP_CORREL)
reslist.append(res19)
res20=cv2.compareHist(histb,hist21,cv2.HISTCMP_CORREL)
reslist.append(res20)
res21=cv2.compareHist(histb,hist22,cv2.HISTCMP_CORREL)
reslist.append(res21)
res22=cv2.compareHist(histb,hist23,cv2.HISTCMP_CORREL)
reslist.append(res22)
    #comparing histogram and calculating threshold "b"
b=reslist[0]
if b==1.0:
    b=reslist[1]
for i in reslist:
    if b<i and i!=1.0:
        b=i

b=b-0.3
print(b)


if (res>b):
    cv2.imshow('1st',oimgt1)
if res1>b:
    cv2.imshow('2nd',oimgt2)
if res2>b:
    cv2.imshow('3rd',oimgt3)
if res3>b:
    cv2.imshow('4th',oimgt4)
if res4>b:
    cv2.imshow('5th',oimgt5)
if res5>b:
    cv2.imshow('6th',oimgt6)
if res6>b:
    cv2.imshow('7th',oimgt7)
if res7>b:
    cv2.imshow('8th',oimgt8)
if res8>b:
    cv2.imshow('9th',oimgt9)
if res9>b:
    cv2.imshow('10th',oimgt10)
if res10>b:
    cv2.imshow('11th',oimgt11)
if res11>b:
    cv2.imshow('12th',oimgt12)
if res12>b:
    cv2.imshow('13th',oimgt13)
if res13>b:
    cv2.imshow('14th',oimgt14)
if res14>b:
    cv2.imshow('15th',oimgt15)
if res15>b:
    cv2.imshow('16th',oimgt16)
if res16>b:
    cv2.imshow('17th',oimgt17)
if res17>b:
    cv2.imshow('18th',oimgt18)
if res18>b:
    cv2.imshow('19th',oimgt19)
if res19>b:
    cv2.imshow('20th',oimgt20)
if res20>b:
    cv2.imshow('21st',oimgt21)
if res21>b:
    cv2.imshow('22nd',oimgt22)
if res22>b:
    cv2.imshow('23rd',oimgt23)

print(reslist)
cv2.imshow('query',oimgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
