from gtts import gTTS

myText = input('Digite seu texto, meu amigo: ')
archiveName = input('Digite o nome do arquivo a ser salvo: ')

language = 'pt-BR'

myObj = gTTS(text=myText, lang=language, slow=False)

myObj.save(archiveName + '.mp3')
print('O arquivo foi salvo com sucesso!')
