# DATA TİME MODÜLÜ
from datetime import datetime
from datetime import timedelta

""" burda içinde ayrı datatime da var eğer içindeki modülleri tektek çalıştımak istiyorsak 
from datatime import date gibi"""
print(datetime.now())
suan=datetime.now().year
suan=datetime.now().day
suan=datetime.now().second
print(suan)
simdi=datetime.today()
print(simdi.ctime())
sonuc=datetime.strftime(simdi,"%B")
"""
%Y yerine %X yazıp saati %d yazıp ayın kaçıncı günü %A hangi gün %B hangi ay olduğunu bulabiliriz
"""
print(sonuc)
zaman=" 30 haziran 2001"
gun,ay, yıl=zaman.split()
print(gun)
print(ay)
print(yıl)
Now="29 May  1453 hour 08:22:45"
dnow= datetime.strptime(Now,"%d %B %Y hour %H:%M:%S")
print(dnow)
birthday=datetime(2001,6,30,11,30,56)
print(birthday)
result=simdi-birthday
print(result.seconds)
a=simdi+timedelta(days=14)
print(a)
# ÖRNEKLER ÇEŞİTLENDİRELEBİLİR BUNLARA W3SCHOOL VB. DEN BULABİLİRSİN

