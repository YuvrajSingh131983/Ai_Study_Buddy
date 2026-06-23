from backend.llm.models import (
    get_chat_model
)

# ============================================
# CUSTOM QA CHAIN
# ============================================

class CustomQAChain:

    def __init__(self, retriever):

        self.retriever = retriever

        self.llm = get_chat_model()

    # ============================================
    # MAIN INVOKE
    # ============================================

    def invoke(self, data):

        query = data["query"]

        docs = self.retriever.invoke(
            query
        )

        context = "\n\n".join(
            [
                doc.page_content
                for doc in docs
            ]
        )

        prompt = f"""
You are an advanced AI Study Tutor.

Your job is to teach concepts clearly,
deeply, and in an educational manner.

Use ONLY the provided study material.

If information is missing,
say:
"I could not find this in uploaded notes."

====================================

STUDY MATERIAL:
{context}

====================================

QUESTION:
{query}

====================================

INSTRUCTIONS:

Provide:
1. Definition
2. Detailed Explanation
3. Step-by-step Working
4. Examples
5. Important Points
6. Applications
7. Advantages/Disadvantages (if applicable)
8. Conclusion

Explain in a student-friendly way.

Generate LONG detailed answers.

====================================

ANSWER:
"""

        response = self.llm.invoke(
            prompt
        )

        return {
            "result": response.content
        }

# ============================================
# BUILD QA CHAIN
# ============================================

def build_qa_chain(retriever):

    return CustomQAChain(
        retriever
    )