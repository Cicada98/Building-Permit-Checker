# -*- coding: utf-8 -*-

import gradio as gr
from langchain_community.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from transformers import pipeline
from langchain_community.llms import Ollama
from colabcode import ColabCode

# Load the Vector store
def load_vectorstore():
    embedding_model = OllamaEmbeddings(model="nomic-embed-text")
    db = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)
    return db
db = load_vectorstore()

# load the transformer which will be used to rewrite the query
def load_rewriter():
  return pipeline("text2text-generation", model="google/flan-t5-base")

# rewrite the query
def rewrite_query(query):
    rewriter = load_rewriter()
    prompt = f"""
    Rewrite the following user question into a clear, formal, regulation-compliant query suitable for searching a building code database.

    Original Query: {query}

    Rephrased Query:
    """
    clean_query = rewriter(prompt, max_length=64, do_sample=False)[0]["generated_text"]
    return clean_query.strip()

llm = Ollama(model='llama3.2') # using this as my llm to generate answers

# use the rewritten query + context (most relevant docs) to generate a final answer
def generate_response(clean_query,context):
    final_prompt = f"""
    You are a building regulations expert in Ontario.

    Question: {clean_query}

    Relevant Regulation Information:
    {context}

    Answer the user query based on the relevant regulation information.

    """
    return llm.invoke(final_prompt)


# made this function to use in gradio class
def process_query(query):
    rephrased = rewrite_query(query)
    results = db.similarity_search(rephrased, k=4)
    context = "\n\n".join([doc.page_content for doc in results])
    answer = generate_response(rephrased, context)
    return rephrased, answer, context

# Gradio UI
iface = gr.Interface(
    fn=process_query,
    inputs=gr.Textbox(lines=2, placeholder="e.g. Do telescopic bleachers need locking devices?", label="Ask a Building Code Question"),
    outputs=[
        gr.Textbox(label="🔎 Rephrased Query"),
        gr.Textbox(label="📌 Final Answer"),
        gr.Textbox(label="📄 Retrieved Context")
    ],
    title="🏗️ Ontario Building Code Validator",
    description="Ask questions about Ontario building regulations and get AI-generated expert responses based on official compendium."
)

iface.launch(share=True)

