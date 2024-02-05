import pyaudio
import wave
import os
import logging
# Configure logging
logging.basicConfig(filename='audio_player.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
folderPath = 'conversation'
CHUNK = 1024
deviceId = 6
# Initialize PyAudio
p = pyaudio.PyAudio()
device = p.get_device_info_by_index(deviceId)
def play_audio(file_name, stream):
    wf = wave.open(file_name, 'rb')
    chunk = wf.readframes(CHUNK)
    while chunk:
        stream.write(chunk)
        chunk = wf.readframes(CHUNK)
    wf.close()
# Open stream as Output mic 
stream_agent = p.open(format=pyaudio.paInt16,
                      channels=2,
                      rate=int(device['defaultSampleRate']),
                      output=True,
                      output_device_index=deviceId)
# Open stream as Output speaker
stream_customer = p.open(format=pyaudio.paInt16,
                         channels=2,
                         rate=44100,
                         output=True)
files = sorted([f for f in os.listdir(folderPath) if f.endswith('.wav')])
for filename in files:
    if 'agent' in filename.lower():
        logging.info(f"Playing on Agent stream: {filename}")
        play_audio(os.path.join(folderPath, filename), stream_agent)
    elif 'customer' in filename.lower():
        logging.info(f"Playing on Customer stream: {filename}")
        play_audio(os.path.join(folderPath, filename), stream_customer)
    else:
        logging.warning(f"Unknown file type: {filename}")
# Wait for the audio to finish playing
# time.sleep(wf.getnframes() / wf.getframerate())
stream_agent.stop_stream()
stream_agent.close()
stream_customer.stop_stream()
stream_customer.close()
p.terminate()









