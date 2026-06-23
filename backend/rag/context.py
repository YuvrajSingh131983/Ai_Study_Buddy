def get_pdf_context(
    qa_chain,
    query
):
    # Handle missing QA chain or retriever gracefully
    if qa_chain is None:
        return ""

    retriever = getattr(qa_chain, "retriever", None)

    if retriever is None:
        return ""

    docs = retriever.invoke(
        query
    )

    context = "\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    return context