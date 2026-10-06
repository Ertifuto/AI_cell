import random

TextObj = ["🙂", "😒", "😂", "😭"]

def Neoral(inputs,weigths,bias):
    soma = 0
    for i in range(len(inputs)):
        soma = ((soma+inputs[i])*weigths[i])###precepton
    soma = soma+bias
    if soma > 0:
        return 1
    else:
        return 0

def Forca(inputs,weigths,bias):
    soma = 0
    for i in range(len(inputs)):
        soma = ((soma+inputs[i])*weigths[i])###precepton
    soma = soma+bias
    return soma

feliz = [10, -1, 9, -8]
infeliz = [-1, 7, 1, 10]
sacarstico = [7, -10, 10, -7]
neutro = [5, -1, 5, -0.5]
biasA,biasB,biasC,biasD = 3,-4,4,1


print("como foi seu dia?--------\nfeliz\ninfeliz\nsacarstico\nneutro\n------------------")
def Camada(dia, hora):
    return [
        Neoral(dia,feliz,biasA),
        Neoral(dia,infeliz,biasB),
        Neoral(dia,sacarstico,biasC),
        Neoral(dia,neutro,biasD) 
    ]

SaidaPeso = {
     TextObj:[random.uniform(-0.1,0.1) for _ in range(4) for memoria in TextObj]
}
SaidaBias = {  
    TextObj:0.0 for memoria in TextObj
}
ValoresNaoConstantes = [4, 9]
def Chose(dia, hora):
    CamadasData = Camada(dia, hora)
    Forca = {
         TextObj:Forca(CamadasData, SaidaPeso[TextObj], SaidaBias[TextObj]) for memoria in TextObj  
         }
    return [max(Forca, key=Forca.get),CamadasData]