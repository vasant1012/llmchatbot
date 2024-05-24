# llmchatbot

## Objective:
To provide information in form of questions and answers using OpenAI, Faiss and vectordb. Dash UI is used as User interface.

## Getting Started
- User will provide question in UI. The question/s will be converted to embedding and send to llm vectordb. Then the vector db used simillarity search index and collect relavant words related to the question. Finally those embeddings will be converted words and then sentences and return as result:


- User also can provide questions in form of batch questions e.g. .xlsx, .csv file. will get output using same mechanism added in same form.

## Tech Stack Involved
- **OpenAI**: To get the relavant output using locally fined tuned vectordb. This product is trained on limited pdf data which are converted into chunks of sentenses. To get faster results from simillarity search index, locally the vectordb is stored.
- **Plotly Dash UI**: The user interface works as mediun user input texts and llm embeddings.

*This is the base version. 1.0*
