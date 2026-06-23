import traceback

results = []

# Test lightweight functions
try:
    from backend.agents.router import route_agent
    v = route_agent("Generate quiz on AI")
    results.append(("route_agent", True, v))
except Exception as exc:
    results.append(("route_agent", False, traceback.format_exc()))

try:
    from backend.flashcards.parser import parse_flashcards
    cards = parse_flashcards("Q: What is AI? A: Artificial Intelligence")
    results.append(("parse_flashcards", True, cards))
except Exception as exc:
    results.append(("parse_flashcards", False, traceback.format_exc()))

try:
    from backend.rag.context import get_pdf_context
    class DummyRetriever:
        def invoke(self, query):
            class Doc:
                page_content = "sample content"
            return [Doc()]
    class DummyChain:
        retriever = DummyRetriever()
    context = get_pdf_context(DummyChain(), "topic")
    results.append(("get_pdf_context", True, context))
except Exception as exc:
    results.append(("get_pdf_context", False, traceback.format_exc()))

# Test imports and model instantiation (external services may be unavailable)
for label, module in [
    ("llm_model", "backend.llm.models"),
    ("embedding_model", "backend.rag.embeddings"),
    ("vision_module", "backend.vision.diagram_analyzer"),
    ("quiz_module", "backend.quizzes.generator"),
    ("flashcard_module", "backend.flashcards.generator"),
    ("knowledge_graph_module", "backend.knowledge_graph.generator"),
    ("planner_module", "backend.agents.study_planner"),
    ("manager_module", "backend.agents.manager"),
]:
    try:
        imported = __import__(module, fromlist=["*"])
        results.append((label, True, f"imported {module}"))
    except Exception as exc:
        results.append((label, False, traceback.format_exc()))

# Attempt external LLM calls only if Ollama likely available
try:
    from backend.quizzes.generator import generate_quiz
    quiz = generate_quiz("AI", "Medium", 1, "This is sample study content.")
    results.append(("generate_quiz", True, repr(quiz)[:400]))
except Exception as exc:
    results.append(("generate_quiz", False, traceback.format_exc()))

try:
    from backend.flashcards.generator import generate_flashcards
    flashcards = generate_flashcards("AI")
    results.append(("generate_flashcards", True, repr(flashcards)[:400]))
except Exception as exc:
    results.append(("generate_flashcards", False, traceback.format_exc()))

try:
    from backend.knowledge_graph.generator import generate_topic_map
    topic_map = generate_topic_map("AI", "Sample context")
    results.append(("generate_topic_map", True, repr(topic_map)[:400]))
except Exception as exc:
    results.append(("generate_topic_map", False, traceback.format_exc()))

try:
    from backend.agents.manager import process_agent_request
    result_quiz = process_agent_request("Generate quiz on AI")
    result_flashcard = process_agent_request("Create flashcards for AI")
    result_planner = process_agent_request("Create a study schedule")
    result_graph = process_agent_request("Create a topic graph")
    results.append(("process_agent_request", True, (result_quiz[:200], result_flashcard[:200], result_planner[:200], result_graph[:200])))
except Exception as exc:
    results.append(("process_agent_request", False, traceback.format_exc()))

print("FEATURE TEST RESULTS")
for name, ok, detail in results:
    print("===", name, "===")
    print("OK:" if ok else "FAIL:", detail)
