from openai import AzureOpenAI
import chromadb



class LLMAnalyzer:
    def __init__(self, azure_endpoint, api_key, api_version="2024-02-01"):
        self.client = AzureOpenAI(
            api_key=api_key,
            api_version=api_version,
            azure_endpoint=azure_endpoint
        )
        self.chroma_client = chromadb.Client()
        


    def create_vector_db(self, collection_name, documents):
        collection = self.chroma_client.create_collection(name=collection_name)
        collection.add(
            documents=documents,
            ids=[f"id_{i}" for i in range(len(documents))]
        )
        return collection
    



    def query_vector_db(self, collection, query, n_results=5):
        results = collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results['documents']
    



    def generate_response(self, prompt, model="gpt-35-turbo"):
        response = self.client.chat.completions.create(
            model=model,
            temperature=0,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content