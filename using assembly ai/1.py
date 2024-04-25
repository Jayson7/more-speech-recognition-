
import assemblyai as aai
import os

from dotenv import load_dotenv
load_dotenv()

aai.settings.api_key = os.getenv("assem_api")
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)