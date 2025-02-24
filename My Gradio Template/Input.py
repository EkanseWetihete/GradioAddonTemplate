import gradio as gr
import json
import os

def get_JS():
    with open('website/main.js', 'r') as file:
        return file.read()

def load_data_types(): # Gets the data from json file and sends to the input file through the server.
    with open('WebData.json', 'r') as json_file:
        data = json.load(json_file)
        inputs = []
        for input_data in data["inputs"]:
            try:
                match input_data["type"]:
                    case "slider":
                        inputs.append(gr.Slider(
                            label=input_data.get("label", "Default Slider Label"),
                            minimum=input_data.get("min", 0),
                            maximum=input_data.get("max", 100),
                            value=input_data.get("default", 50),
                            step=input_data.get("step", 1),
                            interactive=input_data.get("interactive", True),
                            randomize=input_data.get("randomize", False),
                            info=input_data.get("info", ""),
                            visible=input_data.get("visible", True),
                            elem_id=input_data.get("elem_id", ""),
                        ))
                    case "textbox":
                        inputs.append(gr.Textbox(
                            label=input_data.get("label", "Default Textbox Label"),
                            value=input_data.get("value", ""),
                            placeholder=input_data.get("placeholder", ""),
                            interactive=input_data.get("interactive", True),
                            info=input_data.get("info", ""),
                            visible=input_data.get("visible", True),
                            elem_id=input_data.get("elem_id", ""),
                        ))
                    case "checkbox":
                        inputs.append(gr.Checkbox(
                            label=input_data.get("label", "Default Checkbox Label"),
                            value=input_data.get("value", True),
                            info=input_data.get("info", ""),
                            interactive=input_data.get("interactive", True),
                            visible=input_data.get("visible", True),
                            elem_id=input_data.get("elem_id", ""),
                        ))
                    case "radio":
                        inputs.append(gr.Radio(
                            label=input_data.get("label", "Default Radio Label"),
                            choices=input_data.get("name", "").split(),
                            value=input_data.get("value", None),
                            interactive=input_data.get("interactive", True),
                            info=input_data.get("info", ""),
                            visible=input_data.get("visible", True),
                            elem_id=input_data.get("elem_id", ""),
                        ))
                    case "dropdown":
                        choice_list = ""
                        if input_data.get("ai_models_location", "None") == "None":
                            choice_list = input_data["name"]
                        else:
                            choice_list = input_data["name"]
                            
                        inputs.append(gr.Dropdown(
                            label=input_data.get("label", "Default Dropdown Label"),
                            choices=input_data.get("name", "None").split(),
                            value=input_data.get("value", choice_list.split()[0]),
                            multiselect=input_data.get("multiselect", False),
                            interactive=input_data.get("interactive", True),
                            info=input_data.get("info", ""),
                            visible=input_data.get("visible", True),
                            elem_id=input_data.get("elem_id", ""),
                            allow_custom_value=input_data.get("allow_custom_value", False),
                        ))
                    case "number":
                        inputs.append(gr.Number(
                            label=input_data.get("label", "Default Number Label"),
                            value=input_data.get("value", 0),
                            precision=input_data.get("precision", None),
                            info=input_data.get("info", ""),
                            interactive=input_data.get("interactive", True),
                            visible=input_data.get("visible", True),
                            elem_id=input_data.get("elem_id", ""),
                        ))
                    case "file":
                        inputs.append(gr.File(
                            label=input_data.get("label", "Default File Label"),
                            height=input_data.get("height", 168),
                            file_count=input_data.get("file_count", "single"),
                            file_types=input_data.get("file_types", None),
                            interactive=input_data.get("interactive", True),
                            visible=input_data.get("visible", True),
                            elem_id=input_data.get("elem_id", ""),
                        ))
                    case "image":
                        inputs.append(gr.Image(
                            label=input_data.get("label", "Default Image Label"),
                            height=input_data.get("height", 168),
                            interactive=input_data.get("interactive", True),
                            visible=input_data.get("visible", True),
                            elem_id=input_data.get("elem_id", ""),
                        ))
                    case "audio":
                        inputs.append(gr.Audio(
                            label=input_data.get("label", "Default Audio Label"),
                            interactive=input_data.get("interactive", True),
                            visible=input_data.get("visible", True),
                            elem_id=input_data.get("elem_id", ""),
                        ))
                    case "video":
                        inputs.append(gr.Video(
                            label=input_data.get("label", "Default Video Label"),
                            height=input_data.get("height", 272),
                            format=input_data.get("format", "None"),
                            interactive=input_data.get("interactive", True),
                            visible=input_data.get("visible", True),
                            elem_id=input_data.get("elem_id", ""),
                        ))
                    case _:
                        raise ValueError(f"Unsupported input type: {input_data['type']}")
            except KeyError as e:
                print("Error in", os.path.basename(__file__) + ":", e)
        print()
        return inputs
    