import os, sys, openpyxl, requests, pydub
from gtts import gTTS

def saveTts(text, filePath, type = "api"): # type = api/gtts
    try:
        if type == "api":
            response = requests.get("https://translate.google.com/translate_tts", params = {
                "ie": "UTF-8",
                "q": text,
                "tl": "bn-BD",
                "client": "tw-ob",
            })
            open(filePath, "wb").write(response.content)
        else:
            tts = gTTS(text, lang = "bn")
            tts.save(filePath)
    except:
        pass

excelPath = str(input("Enter EXCEL directory path or press Enter for default: ") or "files/xlsx/")
mp3Path = str(input("Enter MP3 directory path or press Enter for default: ") or "files/mp3/")
wavPath = str(input("Enter WAV directory path or press Enter for default: ") or "files/wav/")

if not os.path.exists(excelPath) or not os.path.exists(mp3Path) or not os.path.exists(wavPath):
    print('Directory not found or incorrect!')
    sys.exit()

index = 0
activeSheet = "Sheet1"
for file in os.listdir(excelPath):
    if file.endswith(".xlsx"):
        data = openpyxl.load_workbook(excelPath + file, data_only = True)
        sheet = data[activeSheet]
        
        rowIndex = index
        for col in sheet['C']:
            if col.value is not None:
                rowIndex += 1
                try:
                    saveTts(col.value, f'{mp3Path}{rowIndex}.mp3')
                except:
                    pass
        index = rowIndex
                
index = 0
for file in os.listdir(mp3Path):
    if file.endswith(".mp3"):
        index += 1
        print(f'(#{index}) Converting {file} ...')
        sound = pydub.AudioSegment.from_mp3(mp3Path + file)
        sound.export(wavPath + file.replace('.mp3', '.wav'), format = "wav")
        print("Success!")
        # os.remove(wavPath + file.replace('.mp3', '.wav'))