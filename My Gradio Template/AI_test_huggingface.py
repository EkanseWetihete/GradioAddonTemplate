from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class AiChat:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("PhilipTheGreat/DiabloGPT-small-Traveller")
        self.model = AutoModelForCausalLM.from_pretrained("PhilipTheGreat/DiabloGPT-small-Traveller")  

    def chat(self, input_text, max_length=100, no_repeat_size=4, temperature=0.7, top_probability=0.9, do_sample=True):
        bot_input_ids = self.tokenizer.encode(input_text + self.tokenizer.eos_token, return_tensors='pt')
        attention_mask = torch.ones(bot_input_ids.shape, dtype=torch.long)
        
        chat_history_ids = self.model.generate(
            bot_input_ids,
            attention_mask = attention_mask,
            max_length = max_length,
            pad_token_id = self.tokenizer.eos_token_id, 
            no_repeat_ngram_size = no_repeat_size,   # reduces repetition
            temperature = temperature,               # makes more varied responses
            top_p = top_probability,                 
            do_sample = do_sample                    # more randomness
        )

        chat_output = self.tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        return chat_output
    
if __name__ == "__main__":
    chatbot = AiChat()
    response = chatbot.chat("hi, how are you?")
    print(response)