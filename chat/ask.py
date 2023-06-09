from dotenv import load_dotenv
load_dotenv()

from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.vectorstores import DeepLake

dataset_path = 'hub://langchain-sukh-real-estate/data2'

embeddings = OpenAIEmbeddings()

db = DeepLake(dataset_path=dataset_path, read_only=True, embedding_function=embeddings)

retriever = db.as_retriever()
retriever.search_kwargs['distance_metric'] = 'cos'
retriever.search_kwargs['k'] = 4

qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever, return_source_documents=False)

query = input("Enter query:")

ans = qa({"query": query})

print(ans)

# openai.error.InvalidRequestError: This model's maximum context length is 8192 tokens. However, your messages resulted in 12767 tokens. Please reduce the length of the messages.
