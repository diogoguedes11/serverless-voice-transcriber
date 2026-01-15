# Serverless Voice Transcriber

This project provides a serverless solution for transcribing audio files (MP3) uploaded to Google Cloud Storage (GCS) using Google Cloud Functions and Vertex AI. When an audio file is uploaded to a designated GCS bucket, a Cloud Function is triggered to transcribe the audio and save the resulting text file back to a GCS bucket.

## Features

- **Serverless**: Uses Google Cloud Functions for automatic, event-driven execution.
- **Scalable**: Handles audio transcription at scale with minimal infrastructure management.
- **Modular Infrastructure**: Managed with Terraform for reproducibility and easy deployment.
- **Secure**: Buckets are private by default, and permissions are managed via service accounts.

## Architecture

```
┌────────────┐        ┌────────────────────┐        ┌──────────────┐
│  User/API  │  ──▶  │  GCS Input Bucket  │  ──▶   │ Cloud Function│
└────────────┘        └────────────────────┘        └──────┬───────┘
                                                           │
                                                           ▼
                                            ┌────────────────────┐
                                            │ Vertex AI (STT)    │
                                            └─────────┬──────────┘
                                                      │
                                                      ▼
                                            ┌────────────────────┐
                                            │ GCS Output Bucket  │
                                            └────────────────────┘
```

## Getting Started

### Prerequisites

- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- Python 3.8+

### Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/diogoguedes11/serverless-voice-transcriber.git
   cd serverless-voice-transcriber
   ```

2. **Configure Google Cloud:**

   - Authenticate with your GCP account:
     ```sh
     gcloud auth login
     gcloud config set project <YOUR_PROJECT_ID>
     ```

3. **Set up environment variables:**

   - Copy `.env.example` to `.env` and fill in the required values (for local testing).

4. **Install Python dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

### Infrastructure Deployment

1. **Initialize Terraform:**

   ```sh
   terraform init
   ```

2. **Review and apply the Terraform plan:**

   ```sh
   terraform plan
   terraform apply
   ```

3. **Deploy the Cloud Function:**
   - The function is deployed as part of the Terraform process. If you need to update the function code, redeploy using Terraform or manually via `gcloud functions deploy`.

### Usage

1. **Upload an MP3 file to the input GCS bucket.**
2. The Cloud Function will be triggered automatically.
3. The transcribed text will be saved in the output GCS bucket with the same base filename and a `.txt` extension.

### File Structure

```
.
├── main.py                # Cloud Function source code
├── requirements.txt       # Python dependencies
├── main.tf                # Terraform root module
├── modules/               # Terraform modules (e.g., storage)
├── assets/                # (Optional) Project assets
├── variables.tf           # Terraform variables
├── outputs.tf             # Terraform outputs
└── README.md              # Project documentation
```

## Customization

- **Buckets**: Change bucket names in Terraform variables as needed.
- **Function Logic**: Modify `main.py` to adjust transcription logic or output format.

## Security

- Buckets are private by default.
- Service accounts follow the principle of least privilege.

## Troubleshooting

- Check Cloud Function logs in Google Cloud Console for errors.
- Ensure all required APIs (Cloud Functions, Vertex AI, Storage) are enabled in your GCP project.

## License

MIT License. See [LICENSE](LICENSE) for details.

## Author

Diogo Guedes
