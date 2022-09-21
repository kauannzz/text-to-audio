from cgitb import text
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
            
        