import os
import PyPDF2
import random

#caminho para os arquivos que quer renomear
path = 'C:\\Users\\ana.kindinger\\Documents\\2 VIA CERTIFICADOS\\primeiro-semestre-2019'

#listdir lê todos os arquivos de forma aleatória 
arquivos = os.listdir(path)

for filename in arquivos:

    pdf_file = open(os.path.join(path,filename), 'rb')
    read_pdf = PyPDF2.PdfReader(pdf_file)
    page = read_pdf.pages[0]
    page_content = []
    i=1
    def visitor_body(text, cm, tm, fontDict, fontSize):
        y = tm[5]
        if y > 300 and y < 325:
            page_content.append(text)
            print(page_content)

    page.extract_text(visitor_text=visitor_body)
    #lê e junta os caracteres de texto com quebra de linha
    parsed = ''.join(page_content)
    #fechar arquivo pdf antes de renomear
    pdf_file.close()
    try:
        os.rename(os.path.join(path,filename), os.path.join(path,str(str(parsed) +'.pdf')))
    except FileExistsError:
        os.rename(os.path.join(path,filename), os.path.join(path,str(str(parsed) +str(random.randrange(100))+'.pdf')))
        
         