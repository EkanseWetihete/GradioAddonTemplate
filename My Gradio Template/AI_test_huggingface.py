from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class AiChat:
    def __init__(self, model):
        self.model = model

    def chat(self, input_text, max_length=100, no_repeat_size=4, temperature=0.7, top_probability=0.9, do_sample=True):
        chat_output = "Model could not be loaded."
        try:
            tokenizer = AutoTokenizer.from_pretrained(self.model)
            model = AutoModelForCausalLM.from_pretrained(self.model)
        
            bot_input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors='pt')
            attention_mask = torch.ones(bot_input_ids.shape, dtype=torch.long)
            chat_history_ids = model.generate(
                bot_input_ids,
                attention_mask = attention_mask,
                max_length = max_length,
                pad_token_id = tokenizer.eos_token_id, 
                no_repeat_ngram_size = no_repeat_size,   # reduces repetition
                temperature = temperature,               # makes more varied responses
                top_p = top_probability,                 
                do_sample = do_sample                    # more randomness
            )
            
            chat_output = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        except Exception:
            pass
        
        return chat_output
    
if __name__ == "__main__":
    chatbot = AiChat("PhilipTheGreat/DiabloGPT-small-Traveller")
    #chatbot = AiChat("nothing-much")
    response = chatbot.chat("hi, how are you?")
    print(response)