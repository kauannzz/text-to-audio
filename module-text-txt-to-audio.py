from cgitb import text
from msilib.schema import Error
from multiprocessing.sharedctypes import Value
from gtts import gTTS

class textToVoice():
    def manualVoice():
        myText = input('Digite seu texto, meu amigo: ')
        archiveName = input('Digite o nome do arquivo a ser salvo: ')

        language = 'pt-BR'

        myObj = gTTS(text=myText, lang=language, slow=False)

        myObj.save(archiveName + '.mp3')
        print('O arquivo foi salvo com sucesso!')

    def txtToVoice():
        language = 'pt-BR'

        nameArchive = input('Digite o nome do seu arquivo .TXT: ')
        textArchive = open(nameArchive + '.txt', 'r', encoding="latin-1")
        
        myText = textArchive.read()
        
        myObj = gTTS(text=myText, lang=language, slow=False)

        myObj.save(nameArchive + '.mp3')
        print('O arquivo foi salvo com sucesso!')
            
        
select = input('Qual módulo você quer usar?\n(1) Manual\n(2) TXT para voz')
if select == 1:
    textToVoice.manualVoice()
elif select == 2:
   textToVoice.txtToVoice()
else:
   print('Você não digitou um número ou escolheu uma opção inválida!')