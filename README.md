# How to use:

1. Clone repo
2. Install prerequisites:

pip install fastapi uvicorn python-dotenv requests

2. Start app:

uvicorn main:app --reload

3. Test the app with CURL/Postman. Example:

curl -X 'POST' \
  'http://127.0.0.1:8000/translate/' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Hello, how are you?"
}'
