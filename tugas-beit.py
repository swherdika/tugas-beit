import requests
from datetime import date
from datetime import datetime
response = requests.get(
    'http://ecocim-backend-theone.beit.co.id/api/ManualConfig/TestBEIT')

# Data Fetch
if response.status_code == 200:
    data = response.json()

# Helper Functions


def findCO(name):
    foundC = name.find('C')
    foundO = name.find('O')
    if (foundC > -1 and foundO > -1):
        return True
    else:
        return False


def isPrime(num):
    if num > 1:
        for i in range(2, int(float(num)/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def isDividedBySeven(num):
    if num % 7 == 0:
        return True
    else:
        return False


def determineNearestMonth(month):
    dt1 = datetime(date.today().year, month, date.today().day)
    dt2 = datetime(date.today().year, date.today().month, date.today().day)
    if dt1 < dt2:
        return datetime(date.today().year+1, month, date.today().day)
    else:
        return dt1


# Main Function
listNama = data['listNama']
listNilai = data['listNilai']
tabelNilai = {}

tempKelas = [[], [], [], [], [], [], [], [], [], []]
kelasSpesial = []

willBeMarried = []
cursedDead = []
for i in range(0, len(listNama)):
    if (findCO(listNama[i])):
        kelasSpesial.append({listNama[i]: listNilai[i]})
        if (isDividedBySeven(listNilai[i])):
            willBeMarried.append({listNama[i]: listNilai[i]})
    else:
        tempKelas[listNilai[i]//10].append({listNama[i]: listNilai[i]})
    if (isPrime(listNilai[i])):
        cursedDead.append({listNama[i]: listNilai[i]})
    tabelNilai[listNama[i]] = listNilai[i]

kelas = {}
tempKelasIdx = 0
kelasIdx = 0
while (tempKelasIdx < len(tempKelas)):
    if len(tempKelas[tempKelasIdx]) > 0:
        title = 'Kelas ke-' + str(kelasIdx+1) + \
            '(' + str(tempKelasIdx) + '0+)'
        kelas[title] = tempKelas[tempKelasIdx]
        kelasIdx += 1
    tempKelasIdx += 1
title = 'Kelas ke-' + str(kelasIdx+1) + \
    '(Spesial)'
kelas[title] = kelasSpesial

# Report
print("     Data Setiap Kelas")
print("=========================================")
for key in kelas:
    print(key + " : " + str(kelas[key]))
    print("Jumlah siswa : " + str(len(kelas[key])))
    print()

print("     Data Siswa Menikah Tahun Depan")
print("=========================================")
for i in willBeMarried:
    print(i)
print("Jumlah siswa akan menikah tahun depan : " + str(len(willBeMarried)))
print()

print("     Data Siswa Terkutuk Mati")
print("=========================================")
cursedThisMonth = []
for i in cursedDead:
    for j in i:
        deathTime = determineNearestMonth(i[j] % 10)
        if (i[j] % 10 == date.today().month):
            cursedThisMonth.append(i)
    print(str(i) + " Terkutuk pada tanggal : " + str(deathTime.date()))
print("Jumlah siswa terkutuk : " + str(len(cursedDead)))
print("Jumlah siswa terkutuk bulan ini : " + str(len(cursedThisMonth)))
print("Jumlah siswa terkutuk selain bulan ini : " +
      str(len(cursedDead) - len(cursedThisMonth)))
print()
