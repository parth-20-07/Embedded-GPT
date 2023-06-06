import speech_recognition as sr
import time

# Important Paths
audio_in_save_location: str = "../../logs/audio_in/log"
audio_out_save_location: str = "../../logs/audio_out/log"

# Global Variables
time_stamp = 0.0


def listen_to_microphone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        time_stamp = time.time()
        audio_file_name = f"{audio_in_save_location}_{time_stamp}.flac"

        with open(audio_file_name, "wb") as f:  # write audio to a WAV file
            f.write(audio.get_flac_data())
            print("Audio File Saved")
    return audio_file_name
