curl "https://api.groq.com/openai/v1/chat/completions" \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${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}" \
  -d '{
         "messages": [
           {
             "role": "user",
             "content": "¿porque el cielo es azul"
           }
         ],
         "model": "llama3-8b-8192",
         "temperature": 1,
         "max_tokens": 1024,
         "top_p": 1,
         "stream": true,
         "stop": null
       }'


curl "https://api.groq.com/openai/v1/chat/completions" \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${GROQ_API_KEY}" \
  -d '{
         "messages": [
           {
             "role": "user",
             "content": ""
           }
         ],
         "model": "llama3-8b-8192",
         "temperature": 1,
         "max_tokens": 1024,
         "top_p": 1,
         "stream": true,
         "stop": null
       }'
  

  export GROQ_API_KEY=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


  curl -X POST "https://api.groq.com/openai/v1/chat/completions" \
     -H "Authorization: Bearer $GROQ_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"messages": [{"role": "user", "content": "¿porque el cielo es azul?"}], "model": "llama3-8b-8192"}'