from PyPDF2 import PdfFileWriter, PdfFileReader

edital = PdfFileReader("edital.pdf")
arquivo_reduzido = PdfFileWriter()

inicio = 28
final = 35


# Função que reduz o edital somente para as páginas
# que contém o conteúdo programático.


def reduzir_edital(pagina_inicial, pagina_final):
    for i in range(pagina_inicial - 1, pagina_final - 1):
        arquivo_reduzido.addPage(edital.getPage(i))
        with open("conteudo_programatico.pdf", "wb") as arquivo_de_saida:
            arquivo_reduzido.write(arquivo_de_saida)


reduzir_edital(inicio, final)


# Nesta etapa, será feita a conversão do arquivo .pdf para
# o formato de texto puro (raw text)
# https://www.askpython.com/python/examples/convert-pdf-to-txt

pdffileobj=open('conteudo_programatico.pdf','rb')

# # create reader variable that will read the pdffileobj
pdfreader = PdfFileReader(pdffileobj)
#
# # This will store the number of pages of this pdf file
x = pdfreader.numPages

# create a variable that will select the selected number of pages
pageobj = pdfreader.getPage(x-1)
#
# # (x+1) because python indentation starts with 0.
# # create text variable which will store all text datafrom pdf file
#
texto = pageobj.extractText()
file1=open(r"conteudo_programatico.txt","w", encoding='UTF-8')
file1.writelines(texto)
print(texto)


#
# arquivo_texto = open(r'conteudo_programatico.txt')
# arquivo_texto.writelines(texto)


