terraform {
  backend "s3" {
    bucket = "jm3-state"
    key    = "lambda-iam-creator.tfstate"
    region = "us-east-1"
    #dynamodb_table  = "jm3-state"
  }
}
