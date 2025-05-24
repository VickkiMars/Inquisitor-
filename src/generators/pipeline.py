from src.generators.question_generator import generate_question_type, map_type_to_prompt, generate_prompt
from src.api.gemini_call import call_gemini

def run(question: str) -> dict:
    type_ = generate_question_type(question)
    print(type_)
    prompt = map_type_to_prompt(type_)
    question = generate_prompt(question, prompt)
    response = call_gemini(question)
    return response

print(run("Economics is the social science that studies how societies allocate their scarce resources to satisfy unlimited wants and needs. A market is a place where buyers and sellers interact to exchange goods and services. Demand represents the quantity of a food or service that consumers are willing and able to purchase at various prices duting a specific period. Supply represents the quantity of a good or service that producers are willing and able to offer for sale at various prices during a specific period"))
