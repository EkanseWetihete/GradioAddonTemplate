# -*- coding: utf-8 -*-
import Input
import Output
import gradio as gr
import importlib
import time

class Server:
    def __init__(self, port=7860, server_address="0.0.0.0"):
        self.port = port
        self.gradio_interface = None
        self.server_address = server_address
    
    # Server Management
    def start_gradio_server(self):
        if self.gradio_interface is not None:
            print("Gradio server is already running.")
            return
        importlib.reload(Input) # Reloads libraries so you could change while program is running
        importlib.reload(Output)
        
        data_inputs = Input.load_data_types()
        
        data_outputs = [gr.HTML()]
        
        self.gradio_interface = gr.Interface( 
            fn=Output.gradio_output,
            inputs=data_inputs,
            outputs=data_outputs,
            css_paths='website/main.css',
            js=Input.get_JS()
        )
        
        self.gradio_interface.launch(server_port=self.port, server_name=self.server_address, share=False)
    def stop_gradio_server(self):
        if self.gradio_interface is not None:
            self.gradio_interface.close()
            self.gradio_interface = None
            print("Gradio server stopped.")
        else:
            print("Gradio server is not running.")
    
    # Commandline Management
    def restart(self):
        print("Restarting Gradio server...")
        if self.gradio_interface:
            self.stop_gradio_server()
        time.sleep(3)
        self.start_gradio_server()
    
    def start(self):
        if not self.gradio_interface:
            self.start_gradio_server()
            print("Gradio server has started!")
        else:
            print("Gradio server is already running.")
    
    def stop(self):
        print("Turning off Gradio server...")
        if self.gradio_interface:
            self.stop_gradio_server()
            print("Server was closed successfully!")
        else:
            print(f"Server with {self.port} port was not found.")