output "function_name" {
  value       = google_cloudfunctions_function.cf_main.name
  description = "Cloud function name"
}

output "input_bucket" {
  value       = module.storage.input_bucket_name
  description = "Input bucket name"
}

output "output_bucket" {
  value       = module.storage.output_bucket_name
  description = "Output bucket name"
}
