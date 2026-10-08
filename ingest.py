# Document loading and indexing
from langchain_community.document_loaders import (
    TextLoader,
    DirectoryLoader,
    PyPDFLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os

# Take environment variables from .env (api keys)
load_dotenv()

# the parameter is a folder path that is supposed to be a string, with a default value of "./docs"
def load_documents(docs_dir: str = "./docs"): 
    """Load all supported documents from a directory."""
    loaders = {
        ".txt": TextLoader,
        ".pdf": PyPDFLoader,
    }
    documents = []

    # for each file in the folder
    for file in os.listdir(docs_dir): 
        # takes a filename and extracts its file extension, then converts it to lowercase.
        ext = os.path.splitext(file)[1].lower()
        if ext in loaders: 
            # becomes something like: loader = TextLoader("./docs/notes.txt")
            loader = loaders[ext](os.path.join(docs_dir, file))
            documents.extend(loader.load())
    print(f"Loaded {len(documents)} documents")
    return documents