import os
import PyPDF2

#caminho para os arquivos que quer renomear
path = 'Certificados1'

i = 0

#listdir lê todos os arquivos de forma aleatória 
arquivos = os.listdir(path)


for filename in arquivos:

    pdf_file = open(os.path.join(path,filename), 'rb')
    read_pdf = PyPDF2.PdfReader(pdf_file)
    page = read_pdf.pages[0]
    page_content = page.extract_text()
    #lê e junta os caracteres de texto com quebra de linha
    parsed = ''.join(page_content)
    #fechar arquivo pdf antes de renomear
    pdf_file.close()

    os.rename(os.path.join(path,filename), os.path.join(path,str(str(parsed) +'.pdf')))
    i = i + 1