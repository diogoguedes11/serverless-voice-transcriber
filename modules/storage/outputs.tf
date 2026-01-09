output "input_bucket_name" {
  description = "Bucket name where audio files will be stored"
  value       = google_storage_bucket.input_bucket.name
}

output "output_bucket_name" {
  description = "Bucket name where transcribed texts will be stored"
  value       = google_storage_bucket.output_bucket.name
}