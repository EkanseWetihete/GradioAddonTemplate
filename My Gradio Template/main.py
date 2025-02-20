# -*- coding: utf-8 -*-
from AI_test_huggingface import AiChat as model
from server import Server

"""
I've made some simple Framework addon or template idk how to call it, that potentially will make Gradio usage slightly easier.
Change the parameters in FrontEnd.py and WebData.json file and sort types in the same order for it to work.
You can reload libraries without turning off the program by typing "restart" 

It is still under development and will be updated in the future ~ShiroSnake.


Run main.py file to start using it. (http://127.0.0.1:7860/)
"""


def run(server):
    command = "start"
    while True:
        match command:
            case "restart": # Restarts server libraries and data. (Recommended)
                server.restart()
            case "start": 
                server.start()
            case "stop": 
                server.stop()
            case "exit": 
                print("Exiting the program.")
                server.stop()
                break
            case _:
                print("Invalid command. Please enter 'start', 'stop', 'restart' or 'exit' to proceed.")
        
        command = input("Input 'start', 'exit', or 'restart' to control the server: \n").strip().lower()

if __name__ == "__main__":
    model().chat("Downloading a model, if you dont have it.")
    
    server = Server(port=7860)
    run(server)
