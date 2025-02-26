from gtts import gTTS

text = """
Namaste Mathangi! My name is Anika, and I’m here to guide you through managing your credit card dues.
Mathangi, as of today, your credit card bill shows an amount due of INR 5,053 which needs to be paid by 31st December 2024.
"""

tts = gTTS(text, lang='en', tld='co.in')  # Indian accent
tts.save("inputs/input_audio.mp3")
print("Audio saved to inputs/input_audio.mp3")

