# Configure the Storage module
module "storage" {
  source     = "./modules/storage"
  project_id = var.project_id
  region     = var.region
}


resource "google_cloudfunctions_function" "cf_main" {
  name                  = "process_audio"
  region                = var.region
  runtime               = "python311"
  source_archive_bucket = module.storage.input_bucket_name
  source_archive_object = "function.zip"
  entry_point           = "process_audio"
  environment_variables = {
    OUTPUT_BUCKET = module.storage.output_bucket_name
    PROJECT_ID    = var.project_id
    REGION        = var.region
  }
  available_memory_mb = 512
  event_trigger {
    resource   = module.storage.input_bucket_name
    event_type = "google.storage.object.finalize"
  }
}
