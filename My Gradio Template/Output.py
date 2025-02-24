from AI_test_huggingface import AiChat

def gradio_output(AI_Type, AI_Model, input_text, length, repetition_size, temperature, probability, randomness):
    
    output_instance = OutputClass(input_text, length, repetition_size, temperature, probability, randomness, AI_Model)
    return output_instance.output()

class OutputClass:
    def __init__(self,  input_text, length, repetition_size, temperature, probability, randomness, AI_Model):
        self.input_text = input_text
        self.length = length
        self.repetition_size = repetition_size
        self.temperature = temperature
        self.probability = probability
        self.randomness = randomness
        self.AI_Model = AI_Model

    def chat(self):
        chatbot = AiChat(self.AI_Model)
        response = chatbot.chat(
            self.input_text,
            self.length,
            int(self.repetition_size),
            float(self.temperature),
            float(self.probability),
            self.randomness
        )
        return response

    def get_HTML(self):
        with open('website/body.html', 'r') as file:
            return file.read()
    
    def output(self):
        response = self.chat()
        
        html_content = self.get_HTML().format(
            input_text=self.input_text,
            length=self.length,
            repetition_size=self.repetition_size,
            temperature=self.temperature,
            probability=self.probability,
            randomness=self.randomness,
            response=response
        )
        
        return html_content
    
