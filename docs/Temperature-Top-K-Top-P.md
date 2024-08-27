*** Experiment with different parameter values ***

Every time you ask an AI model a question or assign it a task your question or task includes parameter values (hard coded in the code)that control how the model generates a response. The AI model can and will generate different results for different parameter values. Experiment with different parameter values to determine the best values for the task. The most common parameters for AI/LLMs are the following:

*** Max output tokens ***     
*** Temperature ***  
*** Top-K ***
*** Top-P ***
    

*** Max output tokens ***
Maximum number of tokens (characters) that can be generated in the response. A token is approximately four characters. 100 tokens correspond to roughly 20 words. 1000 tokens correspond to roughly 200 words. 8000 tokens correspond to roughly 1600 words. 

Specify a lower value for shorter responses and a higher value for longer responses.

*** Temperature ***
The temperature is used for sampling during response generation, which occurs when topP and topK are applied. Temperature controls the degree of randomness in token selection. Lower temperatures are good for prompts that require a more deterministic and less open-ended or creative response, while higher temperatures can lead to more diverse or creative results. A temperature of 0 is deterministic, meaning that the highest probability response is always selected.

For most use cases, try starting with a temperature of 0.2. If the model returns a response that's too generic, too short, or the model gives a fallback response, try increasing the temperature.

*** Top-K ***
Top-K changes how the model selects tokens for output. A top-K of 1 means the next selected token is the most probable among all tokens in the model's vocabulary (also called greedy decoding), while a top-K of 3 means that the next token is selected from among the three most probable tokens by using temperature.

For each token selection step, the top-K tokens with the highest probabilities are sampled. Then tokens are further filtered based on top-P with the final token selected using temperature sampling.

Specify a lower value for less random responses and a higher value for more random responses. The default top-K is 40.

*** Top-P ***
Top-P changes how the model selects tokens for output. Tokens are selected from the most (see top-K) to least probable until the sum of their probabilities equals the top-P value. For example, if tokens A, B, and C have a probability of 0.3, 0.2, and 0.1 and the top-P value is 0.5, then the model will select either A or B as the next token by using temperature and excludes C as a candidate.

Specify a lower value for less random responses and a higher value for more random responses. The default top-P is 0.95.

*** Prompt iteration strategies ***

Prompt design is an iterative process that often requires a few iterations before you get the desired response consistently. This section provides guidance on some things you can try when iterating on your prompts.
Use different phrasing

Using different words or phrasing in your prompts often yields different responses from the model even though they all mean the same thing. If you're not getting the expected results from your prompt, try rephrasing it.