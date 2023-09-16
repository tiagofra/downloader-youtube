from pytube import YouTube
from moviepy.editor import *
import os
import urllib.request
import urllib.parse
import re

repetir_formato = True
repetir_linkOuNome = True

print("Downloader do youtube em áudio ou vídeo!")
while repetir_linkOuNome:
    linkOuNome = input("Você deseja inserir um link (Digite 'l') ou colocar o nome (Digite 'n')? ")
    if linkOuNome == 'n':   
        nome_video = input("Digite o nome da música ou vídeo que você deseja baixar: ")
        nome_video_codificado = urllib.parse.quote(nome_video)
        link_padrao = "https://youtube.com/results?search_query="
        html = urllib.request.urlopen(link_padrao + nome_video_codificado)
        pagina = html.read().decode()
        resultado = re.findall(r"watch\?v=(\S{11})", pagina)
        repetir_linkOuNome = False
        if resultado:
            link_final = ("https://www.youtube.com/watch?v=" + resultado[0])
        else:
            print("Nenhum video encontrado com esse nome")
    elif linkOuNome == 'l':
        link_final = input("Insira o link do vídeo: ")
        repetir_linkOuNome = False
    else:
        print("Você não inseriu 'l' ou 'n'")

while repetir_formato:
    try:
        formato = input("Você deseja baixar em vídeo (MP4 - Digite 'v') ou em música (MP3 - Digite 'm')? ").strip().lower()
        if formato not in ['v', 'm']:
            print("Escolha de formato inválida. Use 'v' ou 'm'. ")
    except:
        continue

    if formato == "v":
        print("Baixando em formato MP4, aguarde...")
        yt=YouTube(link_final)
        video=yt.streams.filter(res="720p").first()
        video.download()
        repetir_formato = False
    elif formato == "m":
        yt=YouTube(link_final) 
        print("Baixando, aguarde...")
        video=yt.streams.filter(res="144p").first()
        download_video=video.download()
        base, ext=os.path.splitext(download_video)
        mp3=base + ".mp3"
        mp4_without_frames = AudioFileClip(download_video)     
        mp4_without_frames.write_audiofile(mp3)    
        mp4_without_frames.close()
        if os.path.exists(download_video):
            os.remove(download_video)
        repetir_formato = False

print("Download concluído.")