from PyQt5 import uic,QtWidgets

alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def descriptografa():
    linha = segunda_tela.lineEdit.text()
    soma = ""
    p = linha
    contar = len(p)
    for i in range (contar):
        x = p[i]
        procurar = alfabeto.index(x)
        soma += alfabeto[procurar - 3]
        segunda_tela.label_4.setText(soma)
def chama_segunda_tela():
    segunda_tela.show()

def funcao_principal():
    linha = formulario.lineEdit.text()
    soma = ""
    p = linha.lower().replace(" ", "")
    contar = len(p)
    for i in range(contar):
        x = p[i]
        procurar = alfabeto.index(x)
        soma += alfabeto[procurar + 3]
    formulario.label_4.setText(soma)

app = QtWidgets.QApplication([])
formulario=uic.loadUi("luisin.ui")
segunda_tela=uic.loadUi("segunda_tela.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(descriptografa)

formulario.show()
app.exec()