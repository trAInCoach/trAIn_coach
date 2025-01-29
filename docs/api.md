# trAIn API Documentation 🚀

## Base URL:
http://127.0.0.1:5000


## 📡 **Endpoints**

### 🔹 `POST /analyze`
**Description:** It analyzes the user's biometric data and returns a posture score.
**Request Body (JSON):**
```json
{
  "data": [0.5, 0.7, 0.2]
}
```
**Response Body (JSON):**
```json
{
  "status": "success",
  "analysis": "Good form",
  "confidence": 0.89
}
```
### 🔹 `GET /status`
Description: Checks the status of the AI server.
**Response Body:**
```
{
  "status": "running",
  "uptime": "24 hours"
}
```

