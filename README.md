Vern is a natural language-powered programming language. It takes regular English phrases and instructions and executes the code through a compiler that has a fine-tuned
LLM built within it. This lets you skip the annoying process of writing code in perfect syntax and instead allows the user to write out well-planned logic for the computer
to execute. 

v.09 serves as a proof of concept. Here, we have 
  User ➔ vern.py ➔ OpenAI GPT ➔ Code ➔ Python interpreter

v.0901 is going to have 
  User ➔ Vern's Internal LLM ➔ AST (Abstract Syntax Tree) ➔ Python ➔ Execute

The internal LLM will have to be fine-tuned meticulously to pick up the correct intent and sentiment of the human language.

v.0901 is going to serve as the first rough proof of concept of using an Internal LLM within the compiler. 
