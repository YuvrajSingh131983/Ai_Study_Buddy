def create_retriever(vectorstore):

    retriever = vectorstore.as_retriever(

        search_type="similarity",

        search_kwargs={

            # MORE CONTEXT
            "k": 10
        }
    )

    return retriever