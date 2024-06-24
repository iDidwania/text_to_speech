# prereq: must install Google Text to Speech
# terminal: pip install gTTS
from gtts import gTTS

# ask user for text 
mytext = input("Enter your text: \n")
print("\n")

# ask user which language text is in
print("What language is the text in?")
print("English (en), French (fr), Portuguese (pt), Spanish (es)")
language = input()
  
print("\n")

# series of if-elif-else statements to present the possible accents
if (language == "en"):
  print("Please select an accent:")
  print("Australia (com.au), UK (co.uk), US (us), Canada (ca), India (co.in), Ireland (ie), South Africa (co.za), Nigeria (com.ng)")
  accent = input()
  print("\n")
elif (language == "fr"):
  print("Please select an accent:")
  print("Canada (ca), France (fr)")
  accent = input()
  print("\n")
elif (language == "pt"):
  print("Please select an accent:")
  print("Brazil (com.br), Portugal (pt)")
  accent = input()
  print("\n")
elif (language == "es"):
  print("Please select an accent:")
  print("Mexico (com.mx), Spain (es), US (us)")
  accent = input()
  print("\n")
else:
  accent = 'en'
  print("\n")

# create the audio file with the parameters established above
audio = gTTS(text = mytext, lang = language, tld = accent)

# save audio file 
audio.save("audio.mp3")


