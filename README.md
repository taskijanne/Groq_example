# How to use:

1. Clone repo
2. Install prerequisites:

pip install fastapi uvicorn python-dotenv requests

3. Add .env file and "APIKEY" -variable to the file
APIKEY=yourapikeyhere

(If you don't have apikey, get one from Groq)

4. Start app:

uvicorn main:app --reload

5. Test the app with CURL/Postman. Example:

curl -X 'POST' \
  'http://127.0.0.1:8000/translate/' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Hello, how are you?"
}'
