
import threading
import sys
import time
from turtle import width
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import wave
import speech_recognition as sr
from speech_recognition import AudioData


stop_event = threading.Event()

def wait_for_enter():
    input("\n🎤 Press Enter to stop recording...\n")
    stop_event.set()

def spinner():
    chars = '|/-\\'
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f'\r🔴 Recording... {chars[i % 4]}')
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    print("\r✅ Recording complete!          ")

def record_audio(label):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                    input=True, frames_per_buffer=1024)
    frames = []
    
    threading.Thread(target=wait_for_enter, daemon=True).start()
    threading.Thread(target=spinner, daemon=True).start()
    
    while not stop_event.is_set():
        frames.append(stream.read(1024))
    
    stream.stop_stream()
    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()
    return b''.join(frames), 16000, width

def analyze_audio(data, rate):

    samples = np.frombuffer(data, dtype=np.int16)

    return {
     'duration': len(samples) / rate,
     'avg_volume': np.mean(np.abs(samples)),
     'max_volume': np.max(np.abs(samples)),
     'samples': samples
    }

def display_stats(stats, text, label):

   print(f"\n{'─' * 40}")

   print(f"???? {label}")

   print(f"{'─' * 40}")

   print(f"⏱️  Duration:  {stats['duration']:.2f} seconds")

   print(f"???? Avg Amplitude: {stats['avg_volume']:.0f}")

   print(f"???? Max Amplitude: {stats['max_volume']:.0f}")

   print(f"???? Transcription: {text}")

def compare(stats1, stats2):

    print("\n" + "=" * 40)

    print("???? COMPARISON RESULTS")

    print("=" * 40)


    if stats1['duration'] > stats2['duration']:

        longer = "Recording 1"

        diff = ((stats1['duration'] - stats2['duration']) / stats2['duration']) * 100

    else:

        longer = "Recording 2"

        diff = ((stats2['duration'] - stats1['duration']) / stats1['duration']) * 100

    print(f"⏱️  {longer} is longer by {diff:.1f}%")

# Volume comparison

    if stats1['avg_volume'] > stats2['avg_volume']:

        louder = "Recording 1"

        diff = ((stats1['avg_volume'] - stats2['avg_volume']) / stats2['avg_volume']) * 100

    else:

       louder = "Recording 2"

       diff = ((stats2['avg_volume'] - stats1['avg_volume']) / stats1['avg_volume']) * 100

       print(f"???? {louder} is louder by {diff:.1f}%")


def save_audio(data, rate, width, filename="recording.wav"):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(data)
    print(f"💾 Saved: {filename}")

def transcribe(data, rate, width):
    recognizer = sr.Recognizer()
    audio = AudioData(data, rate, width)
    try:
        text = recognizer.recognize_google(audio)
        print(f"📝 Transcription: {text}")
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")

def plot_waveform(data, rate):
    samples = np.frombuffer(data, dtype=np.int16)
    time_axis = np.linspace(0, len(samples) / rate, len(samples))
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, samples, color='blue')
    plt.title("Your Voice Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_both(stats1, stats2, rate):

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))


# Plot Recording 1

    t1 = np.linspace(0, len(stats1['samples']) / rate, len(stats1['samples']))

    ax1.plot(t1, stats1['samples'], color='blue', linewidth=0.5)

    ax1.set_title(f"Recording 1 (Normal) - Duration: {stats1['duration']:.2f}s, Avg: {stats1['avg_volume']:.0f}")

    ax1.set_ylabel("Amplitude")

    ax1.grid(True, alpha=0.3)

    ax1.set_ylim(-35000, 35000)


    t2 = np.linspace(0, len(stats2['samples']) / rate, len(stats2['samples']))

    ax2.plot(t2, stats2['samples'], color='red', linewidth=0.5)

    ax2.set_title(f"Recording 2 (Modified) - Duration: {stats2['duration']:.2f}s, Avg: {stats2['avg_volume']:.0f}")

    ax2.set_xlabel("Time (seconds)")

    ax2.set_ylabel("Amplitude")

    ax2.grid(True, alpha=0.3)

    ax2.set_ylim(-35000, 35000)

    plt.tight_layout()

    plt.show()


#def main():
  # print("=" * 40)
   #print("🎙️  HELLO AI, CAN YOU HEAR ME?")
   #print("=" * 40)
   #print("\nSpeak into your microphone...")
    
    #audio_data, rate, width = record_audio()
    #save_audio(audio_data, rate, width)
    #transcribe(audio_data, rate, width)
    #plot_waveform(audio_data, rate)

def main():

    print("=" * 40)

    print("???? VOICE ANALYSIS LAB")

    print("=" * 40)

    print("Record twice and compare your voice!")



# Recording 1: Control

    audio1, rate, width = record_audio("Recording 1: Speak NORMALLY")

    stats1 = analyze_audio(audio1, rate)

    text1 = transcribe(audio1, rate, width)

    display_stats(stats1, text1, "Recording 1 Results")



# Prompt for Recording 2

    input("\n???? Press Enter, then speak LOUDER or FASTER...")



# Recording 2: Variable

    audio2, rate, width = record_audio("Recording 2: CHANGE your voice!")

    stats2 = analyze_audio(audio2, rate)

    text2 = transcribe(audio2, rate, width)

    display_stats(stats2, text2, "Recording 2 Results")



# Compare and visualize

    compare(stats1, stats2)

    plot_both(stats1, stats2, rate)

if __name__ == "__main__":
    main()