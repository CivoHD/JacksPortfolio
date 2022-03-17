
import pytube
import colorama
import youtube_dl
import time
from colorama import Fore, Style
colorama.init(autoreset=True)

print(Fore.RED + '''


 ██████╗██╗██╗   ██╗ ██████╗ ███████╗    ██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
██╔════╝██║██║   ██║██╔═══██╗██╔════╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
██║     ██║██║   ██║██║   ██║███████╗     ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗  
██║     ██║╚██╗ ██╔╝██║   ██║╚════██║      ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝  
╚██████╗██║ ╚████╔╝ ╚██████╔╝███████║       ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗
 ╚═════╝╚═╝  ╚═══╝   ╚═════╝ ╚══════╝       ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
                                                                                                      
 ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗███████╗██████╗                          
██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗                         
██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   █████╗  ██████╔╝                         
██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██╔══╝  ██╔══██╗                         
╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ███████╗██║  ██║                         
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ ''')



while True:

    print(Fore.GREEN + "[+] Choose (mp4 or mp3) ")
    fileType = input()

    print(Fore.BLUE + '[+] Paste a youtube link here')
    ytURL = input()

    if fileType == 'mp4':
        youtube = pytube.YouTube(ytURL)
        video = youtube.streams.get_highest_resolution()

        video.download('')
        break
    elif fileType == 'mp3':
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytURL])
            break
    else:
        print(Fore.RED + "Invalid file type retry!")

    try_again = input("[+] 'retry':  ")
    if try_again.lower() != "retry":
        break

print(Fore.GREEN + "Your download is complete!!")
       
            
            


