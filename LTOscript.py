import csv
import os

#Lista z podanymi sciezkami do plikow, ktore chcemy polaczyc w calosc
PathsList = []
IloscPlikow = int(input("enter the number of csv files that you want to combine:"))


for i in range(IloscPlikow):
    print("podaj sciezke do",i+1,"pliku:")
    path = str(input())
    PathsList.append(path)

#print(PathsList)

#lista z nieuporzadkowanymi numerami tasm, do dalszej obrobki i zapisu do pliku koncowego
ListToSet = []
#petla dodajaca pierwsze kolumny plikow csv do listy
for path in PathsList:
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ',')
        for row in readCSV:
            ListToSet.append(row[0])

#print(ListToSet)
changeToSet = set(ListToSet) # zamiana listy na zbiór > usuwa duplikaty
ListToSaveFile = list(changeToSet)

#print(ListToSaveFile)

filepath = input("enter the path to the folder that should contain the target file:")
filename = input("Enter the name of the destination file:")

finalpath = os.path.join(filepath,filename) #sciezka do folderu w ktorym beda znajdowac sie pliki docelowe, a folder bedzie mial nazwe pliku docelowego
os.mkdir(finalpath)


L5 = ['List of L5 LTO:']  # narazie mi sie nie chce tego poprawic i to jest na koncu listy (powinno byc na poczatku zeby ladnie wygladalo)
L6 = ['List of L6 LTO:']



for id in ListToSaveFile:    #petla dzieli na plili z L5 i L6 > w zalozeniu ze nie ma np. L4 bo juz nie uzywamy, ale beda L7 wiec przerobie pozniej
    if id.endswith('L5'):
        L5.append(id)
    else:
        L6.append(id)

#sortowanie list > zeby latwiej bylo odszukac te tasmy w sejfie bo mam je ulozone numerkami

L5sort = sorted(L5)
L6sort = sorted(L6)
ListToSaveFilesort = sorted(ListToSaveFile)

file = open(os.path.join(finalpath,filename), 'w')
fileL5 = open(os.path.join(finalpath,filename+'L5'), 'w')
fileL6 = open(os.path.join(finalpath,filename+'L6'), 'w')


#petle tworzace 3 pliki w folderze "filename"

for i in ListToSaveFilesort:
    file.write(i+'\n')

file.close()

for i in L5sort:
    fileL5.write(i+'\n')

fileL5.close()

for i in L6sort:
    fileL6.write(i+'\n')

fileL6.close()



#print(L5)
#print(L6)
#test GIT
print("File:",filename,"was successfully created in:",filepath,"!")
