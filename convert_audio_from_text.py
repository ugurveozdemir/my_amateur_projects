from gtts import gTTS
import shutil
print("Welcome to converter to audio from text app")

while True:
    app_lang = input("Please enter the language (en/tr/quit) -->")
    app_lang = app_lang.lower()
    lang_options = ("en","tr","quit")
    if app_lang not in lang_options:
        print("Please type a proper option")
        continue
    elif app_lang == "quit":
        print("It's quiting...")
        quit()
    elif app_lang == "en":
        text = input("Please enter text what you want to convert audio -->")
        name = input("Type a name for the file -->")
        tts = gTTS(text, lang = 'en')
        tts.save(f"{name}-to-audio.mp3")
        print("It is successfully done.")
    elif app_lang == "tr":
        text = input("Lütfen sese çevirmek istediğiniz metni girin. -->")
        isim = input("Dosyaya bir isim verin -->")
        tts = gTTS(text, lang = 'tr')
        tts.save(f"{isim}-to-audio.mp3")
        print("İşlem başarıyla tamamlandı!")