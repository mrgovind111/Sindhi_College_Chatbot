from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Load the college info file
loader = TextLoader("data/college_info.txt", encoding="utf-8")
docs = loader.load()

# Split the file into small chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)

# Create the embedding model (runs on your computer, free)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Store the chunks in a searchable database
vectorstore = Chroma.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})


def get_context(question):
    """Search the college file and return the most relevant text."""
    results = retriever.invoke(question)
    return "\n\n".join(doc.page_content for doc in results)