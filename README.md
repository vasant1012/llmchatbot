# llmchatbot

## Objective:
To provide information in the form of questions and answers using OpenAI, Faiss, and vectordb. Dash UI is used as the User interface.

## Getting Started
- User will provide questions in UI. The question/s will be converted to embedding and sent to llm vectordb. Then the vector db used a similarity search index and collected relevant words related to the question. Finally, those embeddings will be converted into words and then sentences and return as result:
![UI1](https://github.com/vasant1012/llmchatbot/assets/52622703/ff86ae7f-0dd4-43fc-8e8a-db787b5610b5)

- User also can provide questions in the form of batch questions e.g. .xlsx, .csv file. will get output using the same mechanism added in the same form.
![UI2](https://github.com/vasant1012/llmchatbot/assets/52622703/8f69ee8f-f219-4fea-a17e-e88d1bbc9159)

## Tech Stack Involved
- **OpenAI**: To get the relevant output using locally fined tuned vectordb. This product is trained on limited pdf data which are converted into chunks of sentences. To get faster results from the similarity search index, locally the vectordb is stored.
- **Plotly Dash UI**: The user interface works as medium user input texts and LLM embeddings.

*This is the base version. 1.0*
