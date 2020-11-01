#import library
import speech_recognition as sr

def getTranscript(filepath):
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Audio file as source
    # listening the audio file and store in audio_text variable

    with sr.AudioFile(filepath) as source:

        audio_text = r.listen(source)

    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:

            # using google speech recognition
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')

        except:
             print('Must Be an ERROR... run again...')
    return text

# define a function to write dozn the text into q text file
def writeTranscript(text,filename):
    # save the text into a text file
    with open(filename, mode ="w") as file:
        file.write("This text is extracted from the audio file :\n\n")
        file.write(text)
        print("your Transcipt is extracted. check it out!")

## TESTING THE SCRIPT
if __name__ == "__main__":
    # put the image  file path here !
    path = './audio files/audio_2.wav'
    #get the text from the image
    text=getTranscript(path)
    #write the text in a file
    writeTranscript(text,"./text results/audio_2.txt")
    print('Process is DONE')
