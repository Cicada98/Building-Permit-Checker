# Building-Permit-Checker
A GenAi app which gives the user information regarding Ontario building codes.<br>
## Information about the Repository<br>
The repository contains two main files.
  * faiss_index.zip - This is embedded pdf text where the llm (llama3.2) is fetching the data from.
  * app.py - This is the script which which contains whole code
## Steps to run this Repository on Google Colab
This project was made on Google Colab because of lack of local resources. In order to run this repository, run the following commands in order in a new colab notebook with a gpu runtime:
  *  **Transfer the vector store file from GitHub to the Colab local directory:** This will download and unzip the vector store (faiss_index.zip), which contains the necessary data for querying Ontario building codes.
   ```bash
   !wget https://github.com/Cicada98/Building-Permit-Checker/raw/main/faiss_index.zip
   !unzip faiss_index.zip
   ```
  * **Install the necessary requirements:** Use the following command to install all dependencies required to run the app. This ensures that all libraries and tools are up-to-date.
   ``` bash
   !pip install -qU -r https://raw.githubusercontent.com/Cicada98/Building-Permit-Checker/main/requirements.txt
   ```
  * **Download the main Python script (app.py):** This is the core script that runs the application, interacts with the vector store, and fetches the building codes based on user queries.
   ``` bash
   !wget https://raw.githubusercontent.com/Cicada98/Building-Permit-Checker/main/app.py
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

