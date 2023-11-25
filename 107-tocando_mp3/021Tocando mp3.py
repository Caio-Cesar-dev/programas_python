"""import playsound                   #outra forma de tocar a musica
playsound.playsound('021.bm.mp3')
print("Musica one love - bob marley")"""

# não consegui tocar com codigo do professor citado na aula
from pygame import mixer
mixer.init()
mixer.music.load('021.bm.mp3')
mixer.music.play()
input()
