import json
import copy

def main():
    firstMatriz = []
    matrizAssigned = False
    matriz = []
    language = chooceLanguage()

    nApiary = int(input(language["nApiary"] + "\n"))
    r1Total, r2Total, r3Total = 0, 0, 0

    for i in range(nApiary):
        row = []
        print("\n" + language["infoApiary"] + str(i + 1) + ":")
        
        r1 = int(input(language["value1"] + "\n"))
        r2 = int(input(language["value2"] + "\n"))
        r3 = int(input(language["value3"] + "\n"))

        r1Total += r1
        r2Total += r2
        r3Total += r3

        row.extend([r1, r2, r3])
        row.extend([addOnes(i, j) for j in range(nApiary)])
        row.append(float(input(language["rightSide"] + "\n")))

        matriz.append(row)

    #Comprobar que el software funciona si se agrega los valores de la fila z (descomentar todos los comentarios relacionados a z )
    #print("\nIngrese los valores de Z:")
    #zValues = [int(input(f"Z{i+1}: ")) for i in range(3)]
    #matriz.append(addZ(nApiary, zValues))
    matriz.append(addZ(nApiary, r1Total, r2Total, r3Total))
    
    if not matrizAssigned:
        firstMatriz = copy.deepcopy(matriz) 
        matrizAssigned = True
    
    beautyMatriz(firstMatriz, nApiary)
    print("\n")
    analyzeAndTransform(matriz, nApiary)
    print("\n " + language["answere"] + str(matriz[-1][-1]))

def analyzeAndTransform(matriz, nApiary):
    while any(z < 0 for z in matriz[-1][:-1]):
        columPivot = findPivotColum(matriz[-1])
        rowPivot, pivot = findPivot(matriz, columPivot)
        transformRowPivot(matriz, rowPivot, pivot)
        transformColumns(matriz, rowPivot, columPivot)
        beautyMatriz(matriz, nApiary)
        print("\n")

def beautyMatriz(matriz, nApiary):
    beauty = []
    beauty.append(addHeaderRow(nApiary))
    for i in range(nApiary):
        row = ["X" + str(i + 4)] + matriz[i][:]
        beauty.append(row)
    row = ["Z"] + matriz[-1][:]
    beauty.append(row)

    for fila in beauty:
        print(" | ".join(map(str, fila)))

def addHeaderRow(nApiary):
    auxRow = ["VB", "X1", "X2", "X3"]
    auxRow.extend(["X" + str(i + 4) for i in range(nApiary)])
    auxRow.append("RS")
    return auxRow

def addOnes(i, j):
    return 1 if i == j else 0

def addZ(nApiary, r1Total, r2Total, r3Total):
    row = [-r1Total, -r2Total, -r3Total]
    row.extend([0] * (nApiary + 1))
    return row

#def addZ(nApiary, zValues):
#    row = [-z for z in zValues]
#    row.extend([0] * (nApiary + 1))
#    return row

def findPivotColum(row):
    min_value = min(row[:-1])
    return row.index(min_value)

def findPivot(matriz, columPivot):
    aux = float('inf')
    rowPivot, pivot = None, None

    for i, row in enumerate(matriz[:-1]):
        if row[columPivot] > 0:
            result = row[-1] / row[columPivot]
            if result < aux:
                rowPivot = i
                pivot = row[columPivot]
                aux = result

    print("La columna pivote es:", columPivot)
    print("El número pivote es:", pivot)
    return rowPivot, pivot

def transformRowPivot(matriz, rowPivot, pivot):
    matriz[rowPivot] = [x / pivot for x in matriz[rowPivot]]

def transformColumns(matriz, rowPivot, columPivot):
    for i in range(len(matriz)):
        if i != rowPivot:
            factor = matriz[i][columPivot]
            matriz[i] = [matriz[i][j] - factor * matriz[rowPivot][j] for j in range(len(matriz[i]))]

def chooceLanguage():
    with open('data.json') as json_file:
        lang = json.load(json_file)

    while True:
        aux = int(input("1) Español \n2) English\n"))
        if aux in [1, 2]:
            langCode = "es" if aux == 1 else "en"
            return lang.get(langCode, {})
        else:
            print("Por favor, ingrese una opción válida (1 o 2) \nPlease, select a valid option (1 or 2)")

if __name__ == "__main__":
    main()
