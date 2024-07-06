from pocketsphinx import LiveSpeech

def test_engine():
    for phrase in LiveSpeech():
        print(phrase)
