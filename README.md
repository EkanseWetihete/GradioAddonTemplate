# GradioAddonTemplate
I've made Grodio template that simplifies the startup project.

Input.py - required for server data inputs (JavaScript or Blocks from WebData)

WebData.json - I've tried to add all the important functionalities as it has in documentation. The most important part is sorting, Input parameters has to be go in the same order as in WebData.json file types.

Output.py - According to given parameters, it sends to AI Chat, recieves response and sends back the HTML data after clicking "Submit" towards the website.

Output parameters has to be in the same order and the same amount as WebData.json inputs.

AI_test_huggingface.py - Takes models from huggingface website and downloads them (or uses the downloaded models). You can change and choose your own pre-trained models to test.

Server.py - Server management part has library reloading functions, hosts and reads data from Input and Output. Commandline part can stop, start, exit and restart the server. 
Restarting will reload Input and Output libraries, which makes it way easier to change AI models, website functionality wether it is javascript, css or changing WebData Blocks.

I've made a starting place for html, css and js so you can test your code if it works:
1. body.html - it is the output file after you click "Submit".
2. head.html - it adds headers to the website.
3. main.css - it adds styles.
4. main.js - It waits for a testing button to exist and once it does, gives a functionality to it. If clicked, every output element is removed.

main.py - All you need to do is start this file and the server will be up! (Default ip: http://127.0.0.1:7860/)

It might load a few minutes upon first startup and "submit" click
