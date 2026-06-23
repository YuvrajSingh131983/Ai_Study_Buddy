from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from backend.config.settings import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


def load_pdf(file_path):

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    # LIMIT PDF SIZE
    return documents[:15]


# ============================================
# SPLIT DOCUMENTS
# ============================================

def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=CHUNK_SIZE,

        chunk_overlap=CHUNK_OVERLAP,

        separators=[
            "\n\n",
            "\n",
            ". ",
            " "
        ]
    )

    chunks = splitter.split_documents(
        documents
    )

    return chunks