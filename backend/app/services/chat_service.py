from app.llm.llmProcess import llm_processing

def process_query(query:str) -> str:
    response = llm_processing(query)
    return response