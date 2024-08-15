# 🤖 AI Prompt Engineering (APE) & Fine-Tuning Toolkit (FTT)
⚡Powered by Gemini 1.5 Flash - Gemini 1.5-Pro - Gemini-1.5-Pro-Experimental.  Choose from (3) Gemini Models.

![1250x650-gemini-flash-pro-aug-update](https://github.com/user-attachments/assets/bcd5478c-52f4-4a5b-9793-cf54090ec0ad)

This repository houses a powerful Streamlit application designed to streamline your AI prompt engineering and fine-tuning dataset workflows.  Harness the power of Google's cutting-edge Gemini models (1.5 Flash, 1.5 Pro, and 1.5 Pro Experimental) to generate high-quality prompts, analyze files, and create test datasets for fine-tuning your AI models.


## ✨ Key Features

* **Prompt Generation:** Craft effective prompts for a wide range of tasks, from creative writing to code generation.
* **File Analysis:**  Gain insights from your data by uploading and analyzing CSV, TXT, Markdown (MD), and image files.
* **Test Data Generation:**  Create synthetic datasets for fine-tuning your AI models, ensuring they perform optimally.
* **Multi-Model Support:**  Choose from Gemini 1.5 Flash, 1.5 Pro, or 1.5 Pro Experimental to leverage different capabilities.
* **User-Friendly Interface:**  Intuitive Streamlit interface makes the app accessible to both beginners and experienced users.


# 🛠️ Why Streamlit, Langchain and Langsmith?



## 🎈Streamlit: Rapid AI Frontend User Interface (UI) Application Development
Streamlit provides an intuitive framework for building interactive web applications with minimal code, allowing us to focus on delivering a seamless user experience.
![logo-streamlit](https://github.com/user-attachments/assets/b818f12a-7cc3-4edb-bc69-8e82fbaa4bce)


## Langchain (Langsmith): One Framework, Infinite Use Cases
Langchain is a versatile framework that connects Large Language Models (LLMs) to your company's private data and APIs, enabling context-aware, reasoning applications. It offers:
![1920x738-LangChain-logo-parrot-blk-text](https://github.com/user-attachments/assets/94266e6c-e626-4226-bba0-e645c51c6a5c)

- 📊 Built-in ingestion and retrieval methods to augment LLM knowledge with company or user data
- 🔗 Comprehensive integrations and state-of-the-art techniques for building Retrieval-Augmented Generation (RAG) systems
- 🔍 Langsmith
- 🚀 Rapid prototyping and production deployment capabilities
- 🧩 Infinite composability for creating custom AI-powered workflows
https://github.com/user-attachments/assets/4e997174-05e8-43f7-a70b-24f6ea5a9fd0

## 🔍 Langsmith: LLM Application Lifecycle Management 

LangSmith is a tool for observing, debugging, dataset creation, cost analysis and improving your AI/LLM applications. 

***Get you Langsmith API Key here https://smith.langchain.com/***

Key features include:

https://github.com/user-attachments/assets/6a730a5e-3a5e-4254-8d61-1500d0a30caf


- 🐞 Real-time debugging and performance optimization
- 👥 Collaboration tools for sharing chain traces
- 📝 Hub for crafting, versioning, and commenting on prompts
- 🏷️ Annotation Queues for human labeling and feedback
- 📊 Dataset creation for evaluations, few-shot prompting, and fine-tuning
- 🧪 Comprehensive testing and evaluation capabilities, including AI-assisted evaluation

![2-Langsmith-aiengineeringforgrandmas](https://github.com/user-attachments/assets/1f68ae84-3986-4aa2-aefc-1543526698b3)


## 🚀 Quickstart
![python](https://github.com/user-attachments/assets/14351783-eb15-424a-aff3-238707712614)

***Download and Install Python*** 

https://www.python.org/downloads/macos/

https://www.python.org/downloads/windows/


![Git-Logo-1788C](https://github.com/user-attachments/assets/dc07e6bd-bdb5-4622-a3e0-c7b472129502)

***Download and Install Git***

https://git-scm.com/download/mac

https://git-scm.com/download/win


![png-clipart-honda-anaconda-python-data-science-honda-text-logo](https://github.com/user-attachments/assets/e399ad85-8176-4c1e-bbe3-cbc99fd600bb)

***Download and Install Conda***

We recommend using `conda` for easy and secure environment management. 

Download it from [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html).

Scroll down on the miniconda page *** to the "Latest Miniconda installer links" section to download for Windows, MacOs and Linux ***


### 1. Set Up Your Environment

1. **Create a secure Conda Environment:**
   ```bash
   conda create -n gprmt-engnr python=3.12 
   conda activate gprmt-engnr 
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### 2. Get and Save Your API Keys

1. **Google Gemini API Key:**  This special key allows you to tap into Google's powerful AI model.  Get your free key at [https://https://aistudio.google.com/](https://https://aistudio.google.com/).

* **How to use the Gemini API Key:**  Enter this special key in the left side of the Streamlit frontend UI in order to use the app.

2. **Create a `.env` File:** In your project's folder, create a new text file named `.env`.

2. **Add Your LANGSMITH/LANGCHAIN API Key:** Open the `.env` file and paste in your Langsmith API key:

   ```
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_ENDPOINT="https://api.smith.langchain.com" 
   LANGCHAIN_API_KEY="your api key goes here" #
   LANGCHAIN_PROJECT="gemini-pro-prompts"

   ```

   **Keep this file and your API Keys safe and don't share it!**

### 3. Launch the App

1. **Navigate to the Project Directory:**
   ```bash
   cd /path/to/your/project
   ```

2. **Run the Streamlit App:**
   ```bash
   streamlit run v1.8-gemini-prompt-engineer.py

   ```

Your app will open in your web browser, ready for you to start exploring!

## 🚀 Usage

### 1. Generate Prompts

1. **Enter Your Question or Task:**  Describe the task you want the AI to perform (e.g., "??????").
2. **Add Variables (Optional):**  Provide specific details or constraints (e.g., "topic: adventure, audience: children, tone: humorous").
3. **Click "Generate Prompt":**  The app will generate a prompt tailored to your input.
4. **Download Options:**  Download the prompt as a TXT or JSONL file for later use.

### 2. Analyze Files

1. **Upload a File:**  Select a CSV, TXT, Markdown (MD), or image file from your computer.
2. **Enter Analysis Prompt:**  Provide instructions for the AI to analyze the file (e.g., "Summarize the key findings of this research paper").
3. **Click "Analyze File":**  The app will generate an analysis based on your prompt and the file contents.

### 3. Generate Test Data

1. **Enter Topic or Text:**  Provide a topic or text as a basis for generating conversation pairs.
2. **Specify Number of Pairs:**  Choose how many conversation pairs you want to generate.
3. **Click "Generate Test Data":**  The app will create a JSON or JSONL file containing the generated conversation pairs.

## 💡 Tips

* **Be Specific:**  The more specific your task descriptions and analysis prompts, the better the results.
* **Experiment with Variables:**  Try different combinations of input variables to fine-tune your prompts.
* **Iterate and Refine:**  Don't be afraid to experiment and refine your prompts based on the generated results.

## 🙏 Acknowledgements

* **Google Gemini:** For the powerful and versatile language models.
* **Streamlit:** For making it easy to build interactive web applications.
* **Langchain's Langsmith: Tracing and Observability for LLMs** Tracing and observing the behavior of large language models (LLMs)s.

## 🛠️ Under the Hood: Technical Deep Dive

Let's explore the key technologies and techniques that power this application.

**1. Google Gemini: The Brainpower Behind the Magic**

Google Gemini is a family of large language models (LLMs) developed by Google AI.  These models are trained on massive datasets of text and code, enabling them to perform a wide range of tasks, including:

* **Text Generation:**  Write stories, poems, articles, and more.
* **Code Generation:**  Generate code in various programming languages.
* **Translation:**  Translate text between languages.
* **Question Answering:**  Provide informative answers to questions.
* **Summarization:**  Condense large amounts of text into concise summaries.

This app leverages the power of Gemini to generate prompts, analyze files, and create test data.

**2. Langsmith: Tracing and Observability for LLMs**

This application integrates with LangSmith, a framework developed by LangChain for tracing and observing the behavior of large language models (LLMs). LangSmith allows developers to gain insights into how their LLMs are performing, identify potential issues, and improve the overall quality of their AI applications.

**3. Streamlit: Building Interactive User Interfaces**

Streamlit is a Python library that makes it incredibly easy to create interactive web applications for data science and machine learning.  Its intuitive API and focus on simplicity allow developers to quickly build and deploy powerful apps without the need for extensive front end user inteface web development knowledge.

This app leverages Streamlit to provide a user-friendly interface for interacting with the Gemini models and managing your prompt engineering and fine-tuning workflows.

**4. Putting It All Together: The Workflow**

Here's a high-level overview of how the app works:

1. **User Input:**  You provide a task description, analysis prompt, or topic for test data generation.
2. **Prompt Generation (if applicable):**  The app uses Gemini to generate a prompt based on your input.
3. **File Analysis (if applicable):**  The app uploads and analyzes your file using Gemini, providing insights based on your analysis prompt.
4. **Test Data Generation (if applicable):**  The app uses Gemini to generate conversation pairs for fine-tuning your AI models.
5. **Output and Download:**  The app displays the generated prompts, analysis results, or test data, and provides download options for convenient storage and reuse.

This integration of Gemini, LangSmith, and Streamlit empowers you to harness the power of AI for your prompt engineering and fine-tuning tasks.

## 🙌 Contributing

I welcome contributions from the community! Here's how you can get involved:

1. **Fork the Repository:**  Click the "Fork" button at the top right of this page.

2. **Create a New Branch:**  Make your changes in a separate branch to keep things organized.
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit Your Changes:**  Add clear and concise commit messages to explain your work.
   ```bash
   git commit -m "Add your descriptive commit message here"
   ```
4. **Push to Your Fork:**  Send your changes to your forked repository on GitHub.
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request:**  Submit a pull request to the main repository, describing your changes and their benefits.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Learn More

Want to dive deeper into the technologies behind this project? Here are some helpful resources:

* **Google Gemini:** [https://developers.google.com/gemini/](https://developers.google.com/gemini/)
* **Streamlit Documentation:** [https://docs.streamlit.io/](https://docs.streamlit.io/)
* **LangSmith Documentation:** [https://docs.langchain.com/docs/ecosystem/integrations/langsmith](https://docs.langchain.com/docs/ecosystem/integrations/langsmith)

## 🚀 Let's Build the Future of AI Together!

We believe this project is a stepping stone towards a more accessible and powerful future for AI development.  Join us on this exciting journey!

* **Star this Repository:**  Show your support and help others discover this project.
* **Share Your Creations:**  We'd love to see what you build using this app! Share your projects and ideas with the community.
* **Contribute and Collaborate:**  Let's work together to make this project even better!

Let's unlock the potential of AI together!

Okay, here's the final part of the README, wrapping things up with a call to action and contact information:

## 🚀 Get Started Today!

Ready to unleash the power of Gemini for your AI prompt engineering and fine-tuning tasks?  

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   ```

2. **Follow the Quickstart guide above to set up your environment and configure your API key.**

3. **Start exploring the app and see what you can create!**

## 🙋‍♀️  Need Help?  Have Questions?

We're here to support you on your AI journey.  Feel free to reach out if you encounter any issues or have questions about the app.

* **Open an Issue:**  Report bugs or suggest new features by opening an issue on the GitHub repository.
* **Join the Community:**  Connect with other users and developers in our community forum (link to be added soon).

## 🙏 Acknowledgements

* **Thank you to the awesome teams at Google, Streamlit and Langchain!!!:** I extend my gratitude to the amazing teams who have made these project possible:

* **Google AI:** For developing the powerful Gemini models.
* **Streamlit:** For creating an intuitive and user-friendly framework for building web applications.
* **LangChain:** For developing the LangSmith tracing and observability framework.

## ❤️ Let's Make AI More Accessible!

We believe that AI should be accessible to everyone, regardless of their technical background.  This project is a step towards that vision.  Join us in making AI more accessible and empowering!

**Happy Prompt Engineering!**









