resource "google_storage_bucket" "input_bucket" {
  name                        = "${var.project_id}-input-bucket"
  location                    = var.region
  force_destroy               = true
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
}

resource "google_storage_bucket" "output_bucket" {
  name                        = "${var.project_id}-output-bucket"
  location                    = var.region
  force_destroy               = true
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
}
