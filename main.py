import functions_framework
import os
import vertexai
from vertexai.generative_models import GenerativeModel, Part
from google.cloud import storage
from dotenv import load_dotenv


@functions_framework.cloud_event
def process_audio(cloud_event):
    load_dotenv()
    project_id = os.environ.get("PROJECT_ID")
    region = os.environ.get("REGION", "us-central1")
    output_file_name = "file.txt"

    if not project_id:
        print("Error: PROJECT_ID not defined")
        return
    vertexai.init(project=project_id, location=region)

    input_bucket_name = str(cloud_event.data["bucket"])
    output_bucket_name = f"{project_id}-output-bucket"

    mp3_file = str(cloud_event.data["name"])

    if not mp3_file.endswith(".mp3"):
        print(f"File {mp3_file} is not an mp3 file. Skipping.")
        return

    gcs_uri = f"gs://{input_bucket_name}/{mp3_file}"

    try:
        model = GenerativeModel("gemini-2.5-flash")
        prompt = "Generate a transcript of the speech."
        response = model.generate_content(
            [
                Part.from_uri(uri=gcs_uri, mime_type="audio/mp3"),
                prompt,
            ]
        )
        transcript = response.text
    except Exception as e:
        print("Error: something wrong happened")
        return
    storage_client = storage.Client()
    ouput_bucket = storage_client.bucket(output_bucket_name)
    blob = ouput_bucket.blob(output_file_name)
    blob.upload_from_string(transcript)
    print(
        f"Success! transcript is now at: gs://{output_bucket_name}/{output_file_name}"
    )
