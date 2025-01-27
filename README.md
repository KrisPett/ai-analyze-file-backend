fastapi dev main.py

http://127.0.0.1:8000

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/redoc

### Setup

```
.env
OPENAI_API_KEY=...
```

### Curl stuff

```
curl http://127.0.0.1:8000/analyze-file/...
Invoke-WebRequest -Uri "http://localhost:8000/analyze-file/..." -Method Post
```

```
$response = Invoke-WebRequest -Uri "http://localhost:8000/analyze-file/..." -Method Post
$jsonObject = $response.Content | ConvertFrom-Json
$formattedJson = $jsonObject | ConvertTo-Json -Depth 10
Write-Output $formattedJson
```
