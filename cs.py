import gtts
from pygame import mixer
from tempfile import TemporaryFile
from win10toast import ToastNotifier
import pyperclip, time, threading, pyautogui, langid


def play_clip(text):
    ''' Play the text params passed as audio
        Speaks up the message   '''
    language = langid.classify(text)[0]

    speak = gtts.gTTS(text, lang=language, slow=False)

    print(f"Language: {language}\tText: {clip}")
    f = TemporaryFile()
    speak.write_to_fp(f)
    
    f.seek(0)
    mixer.music.load(f)
    mixer.music.play()



def toast_notif(text):
    '''Toast a notification in Windows10'''
    notif = ToastNotifier()
    notif.show_toast("Clipboard Speaker", text)



def hello_prompt():
    title = "Please Read through this before continuing!"
    text =  "After this screen, wait for a toast notification for initializing\n"\
            "Select text and copy to your clipboard, the program will automatically start playing it!"

    return pyautogui.confirm(text, title, buttons=["OK, continue", "Exit"])
    
    
    
    
'''main function lies here:'''
reply = ""
reply = hello_prompt()

if(reply != "Exit"):
    clip_hist = ""
    mixer.init()
    toast_notif("Ready to work!\nYou can minimize the application now!")

    while True:
        temp = pyperclip.paste()
        if temp != clip_hist:
            clip_hist = temp
            clip = pyperclip.paste()

            # threading the clip playing and notification in a parallel thread
            t1 = threading.Thread(target=play_clip, args=(clip,))
            t2 = threading.Thread(target=toast_notif, args=(clip,))

            t1.start()
            t2.start()