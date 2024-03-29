# Ice Breaker

This is an ice-breaker application built using LangChain.

Given a person's name, the LLM will search for their LinkedIn and Twitter data, and then return:

1. Their profile picture from LinkedIn.
2. Their summary and relevant facts.
3. Topics of interest to them.
4. Creative ways to break the ice with them.

## Demo

![demo](/static/demo.png)

## Environment Variables

- Required environment variables in `.env` file
  `OPENAI_API_KEY`
  `PROXYCURL_API_KEY`
  `SERPAPI_API_KEY`
  `TWITTER_API_KEY`
  `TWITTER_ACCESS_TOKEN`
  `TWITTER_BEARER_TOKEN`
  `TWITTER_API_KEY_SECRET`
  `TWITTER_ACCESS_TOKEN_SECRET`

## Run Locally

- Clone the project

```bash
git clone https://github.com/emarco177/ice_breaker.git
```

- Install dependencies

```
poetry install
```

- Start the flask server

```
python app.py
```

## Acknowledgement

This project is part of the LangChain course ([LangChain - Develop LLM-powered applications with LangChain](https://www.udemy.com/course/langchain) by Eden Marco).
