# Building-Permit-Checker
A GenAi app which gives the user information regarding Ontario building codes.<br>
## Information about the Repository<br>
The repository contains two main files.
  * faiss_index.zip - This is embedded pdf text where the llm (llama3.2) is fetching the data from.
  * app.py - This is the script which which contains whole code
## Steps to run this Repository on Google Colab
This project was made on Google Colab because of lack of local resources. In order to run this repository, run the following commands in order in a new colab notebook with a gpu runtime:
  *  **Clone this repository onto your local colab directory:**
   ```bash
   !git clone https://github.com/Cicada98/Building-Permit-Checker.git
   ```
  * **Change the PWD to the project folder and unzip the vector store file:** The vector store file (faiss_index.zip) contains the necessary embedded data for querying Ontario building codes.
   ``` bash
   %cd Building-Permit-Checker # change your present working directory to this
   !unzip faiss_index.zip
   ```
  * **Install the necessary requirements:** Use the following command to install all dependencies required to run the app. This ensures that all libraries and tools are up-to-date.
   ``` bash
   !pip install -qU -r requirements.txt
   ```
  * **Install ollama embeddings and llmma3.2:** Open the terminal using colab xterm and run the following commands in the terminal.
   ``` bash
   %load_ext colabxterm
   %xterm
   # now inside the terminal, copy-paste the following commands in order one by one.
   curl -fsSL https://ollama.com/install.sh | sh
   ollama serve &
   ollama pull nomic-embed-text
   ollama pull llama3.2
   ```
 * **Start the Gradio app:**
  ``` bash
   !python app.py
  ```
The Last step will give you a link which you can use as a public link which will work until the colab script is running.
   
