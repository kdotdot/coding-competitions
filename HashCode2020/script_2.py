from operator import itemgetter
import sys
class Library:
    #numero de libros, dias para signup, libros por dia
    def __init__(self, id,nBooks, nSignup, nPerDays, books, bookscore):
        self.id = id
        self.nBooks = nBooks
        self.nSignup = nSignup
        self.nPerDays = nPerDays
        self.booksDict = {i : bookScores[i] for i in books}
        self.scanned = []
    def str(self):
        return self.nBooks, self.nSignup, self.nPerDays, self.booksDict
    def scan(self,bookId):
        if bookId not in self.scanned:
            self.scanned.append(bookId)

def takeSignup(e):
    return e.nSignup

def takeSomething(e):
    return e.nBooks/e.nSignup

f=open(sys.argv[1], "r")
line1 = f.readline().split()
nBooks = int(line1[0])
nLibraries = int(line1[1])
nDays = int(line1[2])

temp = list(map(int,f.readline().split()))
bookScores = { i : temp[i] for i in range(len(temp) ) }

libraries = []

for i in range(nLibraries):
    lineaPar = f.readline().split()
    libraries.append(Library(i,int(lineaPar[0]),int(lineaPar[1]),int(lineaPar[2]),list(map(int,f.readline().split())), bookScores))

# LIBRERIAS ORDENADAS POR EL MENOR TIEMPO DE SIGNUP
libraries.sort(reverse=False, key=takeSignup)

signedUpLibraries = [libraries[0]]
finishedLibs = [libraries[0]]
nDays -= libraries[0].nSignup
daysUntilSignUp = libraries[1].nSignup

alreadySigned = 1

for day in range(nDays):
    # print(day)
    if daysUntilSignUp == 0:
        # SIGN UP NEW LIBRARY
        signedUpLibraries.append(libraries[alreadySigned])
        finishedLibs.append(libraries[alreadySigned])
        alreadySigned += 1
        if len(libraries) > alreadySigned:
            daysUntilSignUp = libraries[alreadySigned].nSignup
    daysUntilSignUp -=1
    # PROCESS SIGNED UP LIBRARY
    # COJE LOS MAYORES QUE NO ESTEN YA REGISTRADOS

    for lib in signedUpLibraries:
        res = dict(sorted(lib.booksDict.items(), key = itemgetter(1), reverse = True))
        # i=0
        # for book in range(lib.nPerDays):
        #     max = 0
        #     if lib not in signedUpLibraries:
        #         break
        #     while(max==0):
        #         # print("LIBS: ", id(res.get(3)))
        #         # print("Scores: ", id(bookScores.get(3)))
        #         # print(res)
        #         # print(i)
        #         # print(res.keys())
        #         if(i > len(lib.booksDict)-1):
        #              signedUpLibraries.remove(lib)
        #              break
        #         bookIndex = list(res.keys())[i]
        #         if lib.booksDict[bookIndex] == 0:
        #             signedUpLibraries.remove(lib)
        #             break
        #         max = bookScores[bookIndex]
        #         if max == 0:
        #             lib.booksDict[bookIndex] = 0
        #         i=i+1
        #
        #     # SCAN THE BOOK
        #     if lib not in signedUpLibraries:
        #         break
        #     bookScores[bookIndex] = 0
        #     lib.scan(bookIndex)


f= open(sys.argv[1].split('.')[0]+'.out',"w+")

validLibraries = 0
for l in finishedLibs:
    if len(l.scanned) > 0:
        validLibraries+=1
f.write(str(validLibraries)+'\n')

for l in finishedLibs:
    if len(l.scanned) > 0:
        f.write("{} {}\n".format(str(l.id),str(len(l.scanned))))
        for b in l.scanned:
            f.write(str(b)+' ')
        f.write('\n')
f.close()
