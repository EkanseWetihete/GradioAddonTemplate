import gradio as gr
import json

def get_JS():
    with open('website/main.js', 'r') as file:
        return file.read()

def load_data_types(): # Gets the data from json file and sends to the input file through the server.
    with open('WebData.json', 'r') as json_file:
        data = json.load(json_file)
        inputs = []
        for input_data in data["inputs"]:
            match input_data["type"]: 
                case "slider":
                    inputs.append(gr.Slider(minimum=input_data["min"], maximum=input_data["max"], value=input_data["default"], step=input_data["step"], label=input_data["label"]))
                case "textbox":
                    inputs.append(gr.Textbox(label=input_data["label"], placeholder=input_data.get("placeholder", "")))
                case "checkbox":
                    inputs.append(gr.Checkbox(label=input_data["label"], value=input_data["Enabled"]))
                case "radio":
                    inputs.append(gr.Radio(choices=input_data["choices"], label=input_data["label"]))
                case "dropdown":
                    inputs.append(gr.Dropdown(choices=input_data["choices"], label=input_data["label"]))
                case "number":
                    inputs.append(gr.Number(label=input_data["label"], value=input_data.get("value", 0)))
                case "file":
                    inputs.append(gr.File(label=input_data["label"]))
                case "image":
                    inputs.append(gr.Image(type=input_data.get("type", "pil"), label=input_data["label"]))
                case "audio":
                    inputs.append(gr.Audio(label=input_data["label"]))
                case "video":
                    inputs.append(gr.Video(label=input_data["label"]))
                case _:
                    raise ValueError(f"Unsupported input type: {input_data['type']}")
        return inputs
    
