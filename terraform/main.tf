provider = "google"{
    project = "your-project-id"
    region = "us-central1"
}

resource "google_storage_bucket" "ml_bucket"{
    name = "ml-model-ml_bucket"
}