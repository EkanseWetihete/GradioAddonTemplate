from AI_test_huggingface import AiChat

def gradio_output(AI_Type, AI_Model, name, length, repetition_size, temperature, probability, randomness):
    output_instance = OutputClass(name, length, repetition_size, temperature, probability, randomness)
    
    
    return output_instance.output()

class OutputClass:
    def __init__(self,  name, length, repetition_size, temperature, probability, randomness):
        self.name = name
        self.length = length
        self.repetition_size = repetition_size
        self.temperature = temperature
        self.probability = probability
        self.randomness = randomness

    def chat(self):
        chatbot = AiChat()
        response = chatbot.chat(
            "hi, how are you?",
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
            name=self.name,
            length=self.length,
            repetition_size=self.repetition_size,
            temperature=self.temperature,
            probability=self.probability,
            randomness=self.randomness,
            response=response
        )

        return html_content
    
