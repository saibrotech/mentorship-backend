# Google Gloud

Project ID: **mentorship-368321**

## Region

**us-central1**

## Secret Manager

[Secrets](https://console.cloud.google.com/security/secret-manager?project=mentorship-368321)

## Database

[mentorship-db](https://console.cloud.google.com/sql/instances/mentorship-db/overview?project=mentorship-368321)

### SQL proxy

Download the Cloud SQL Auth proxy:

`wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy`

Run Proxy:

`./cloud_sql_proxy -instances="mentorship-368321:us-central1:mentorship-db"=tcp:5432`

Set project ot use proxy
`export USE_CLOUD_SQL_AUTH_PROXY=true`

## Logs

[Logs Explorer](https://console.cloud.google.com/logs/query;project=mentorship-368321?project=mentorship-368321)

## Manual deploy

`gcloud run deploy`
