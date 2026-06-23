from langchain_community.vectorstores import (
    Chroma
)

from backend.rag.embeddings import (
    get_embedding_model
)

from backend.config.settings import (
    VECTOR_DB_DIR
)


def create_vectorstore(documents):

    embeddings = get_embedding_model()

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=VECTOR_DB_DIR
    )

    return vectorstore