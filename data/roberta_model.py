import torch
from transformers import RobertaTokenizer, RobertaForQuestionAnswering

def answer_question(question):
    # Load pre-trained RoBERTa model and tokenizer
    model = RobertaForQuestionAnswering.from_pretrained('roberta-base')
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    
    # Preprocess question
    inputs = tokenizer(question, return_tensors='pt')
    
    # Generate answer
    outputs = model(**inputs)
    answer = tokenizer.convert_ids_to_tokens(torch.argmax(outputs.start_logits))[0]
    
    return answer
