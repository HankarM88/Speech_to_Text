#import library

import speech_recognition as sr
import pyaudio

# define a funtion to get the transcript from the microphone
def getTranscript():
    # Initialize recognizer class (for recognizing the speech)

    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable

    with sr.Microphone() as source:
        print("Talk")
        audio = r.listen(source)
        print("we got your audio, thanks")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

        try:
            # using google speech recognition
            audio_text= r.recognize_google(audio,language='ar-MA')
        except:
             print("Sorry, must be an ERROR. try again!")
   # get the transcript
    return audio_text

# define a function to write dozn the text into q text file
def writeTranscript(text,filename):
    # save the text into a text file
    with open(filename, mode ="w",encoding='utf-8') as file:
        file.write("This text is extracted from the audio file :\n\n")
        file.write(text)
        print("your has been Transcipt is extracted!!")


## TESTING THE SCRIPT
if __name__ == "__main__":

    #get the text from the image
    text=getTranscript()
    #write the text in a file
    writeTranscript(text,"./text results/audio_3.txt")
    print('Process is DONE')
