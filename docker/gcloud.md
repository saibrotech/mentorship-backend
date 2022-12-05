# Google Gloud

Project ID: **mentorship-368321**

## Region

**southamerica-east1**

## Shell

[Open Shell](https://console.cloud.google.com/welcome?project=mentorship-368321&cloudshell=true)

## Secret Manager

[mentorship-backend-django-settings"](https://console.cloud.google.com/security/secret-manager/secret/mentorship-backend-django-settings/versions?project=mentorship-368321)

## Database

[postgres-vm-1](https://console.cloud.google.com/compute/instancesDetail/zones/southamerica-east1-b/instances/postgres-vm-1?project=mentorship-368321)

## Connect to Data Base

`jdbc:postgresql://35.247.198.101:5432/mentorship`

## Logs

[Logs Explorer](https://console.cloud.google.com/logs/query;project=mentorship-368321?project=mentorship-368321)

## Manual deploy

`gcloud builds submit --config cloudmigrate.yaml --substitutions _INSTANCE_NAME=INSTANCE_NAME,_REGION=REGION`

`gcloud run deploy mentorship-backend --region southamerica-east1 --source .`
