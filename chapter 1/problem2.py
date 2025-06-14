import pyttsx3
engine = pyttsx3.init()
engine.say('''
        Twinkle Twinkle, Little Star
        How I wonder what you are
        Up above the world so high
        Like a diamond in the sky
        Twinkle Twinkle Little Star
        How I wonder what you are!
        Twinkle Twinkle, Little Star
        How I wonder what you are
        Up above the world so high
        Like a diamond in the sky
        Twinkle Twinkle Little Star
        How I wonder what you are!
    ''')
engine.runAndWait()
# This code uses the pyttsx3 library to convert text to speech.
# It initializes the text-to-speech engine, then uses the `say` method to speak the lyrics of "Twinkle Twinkle, Little Star". 
# Finally, it calls `runAndWait` to process the speech commands and wait until the speech is finished.
# Make sure to install the pyttsx3 library if you haven't already:
# pip install pyttsx3
# Note: The output will be spoken aloud, so ensure your audio is enabled.
# The code is a simple demonstration of text-to-speech functionality in Python.

 