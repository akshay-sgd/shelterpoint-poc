Linux:-

```bash

curl -X POST https://api-west.millis.ai/agents \
  -H "Authorization: Bearer " \
  -H "Content-Type: application/json" \
  -d @millis_create_agent.json

```

Windows:-

```bash

$body = Get-Content -Raw millis_create_agent.json
Invoke-RestMethod -Method POST -Uri "https://api-west.millis.ai/agents" `
  -Headers @{ "Authorization" = "Bearer "; "Content-Type" = "application/json" } `
  -Body $body

```

Invoke-RestMethod -Method POST -Uri "https://api-west.millis.ai/agents" -Headers @{ "Authorization" = "Bearer nN2G7ZxZOyENKrom38bftOy0cXPycUt0"; "Content-Type" = "application/json" } -Body $body