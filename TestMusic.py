from kivy.core.audio import SoundLoader
sound = SoundLoader.load('Hey Ya!.mp3')
if sound:
    print("Sound found at %s" % sound.source)
    print("Sound is %.3f seconds" % sound.length)
    while True:
        sound.play()