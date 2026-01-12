import functions_framework
import functions_framework
from google.cloud import storage
import os
from dotenv import load_dotenv
import google.genai
from google.genai.types import HttpOptions, Part
from google.genai import types
import vertexai
import functions_framework
import vertexai
from vertexai.generative_models import GenerativeModel, Part
from google.cloud import storage


@functions_framework.cloud_event
def process_audio(cloud_event):
    load_dotenv()
    project_id = os.environ.get("PROJECT_ID")
    region = os.environ.get("REGION")

    vertexai.init(project=project_id, location=region)

    input_bucket_name = str(cloud_event.data["bucket"])
    output_bucket_name = f"{project_id}-output-bucket"

    mp3_file = str(cloud_event.data["name"])

    if not mp3_file.endswith(".mp3"):
        print(f"File {mp3_file} is not an mp3 file. Skipping.")
        return

    gcs_path = f"gs://{input_bucket_name}/{mp3_file}"
    print(f"Processing: {gcs_path}")

    model = GenerativeModel("gemini-2.5-flash")

    prompt = "Generate a transcript of the speech."

    response = model.generate_content(
        [
            Part.from_uri(uri=gcs_path, mime_type="audio/mp3"),
            prompt,
        ]
    )
    transcript = response.text
    storage_client = storage.Client()
    ouput_bucket = storage_client.bucket(output_bucket_name)
    blob = ouput_bucket.blob(mp3_file)
    blob.upload_from_string(transcript)
