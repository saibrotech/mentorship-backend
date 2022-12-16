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

## Run as production

`gcloud auth login`
`gcloud config get-value project`


Or create a `.env` file with the secrets as production:

```
DATABASE_URL=postgres://mentorship-app:<password>@35.247.198.101:5432/mentorship
SECRET_KEY=<random secrect>
GS_BUCKET_NAME=mentorship-backend-statics
DEBUG=True
```

## Manual deploy

`gcloud run deploy mentorship-backend --region us-central1 --source .`

### Update static files

`python manage.py collectstatic`
`gcloud storage cp static/* gs://mentorship-backend-statics/ --recursive`
