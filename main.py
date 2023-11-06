# Import necessary modules
import os
from dotenv import load_dotenv
import openai
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, download_loader

def main():
# Load environment variables from a .env file
  load_dotenv()
  
  # Set OpenAI API key from the environment variable
  openai.api_key = os.getenv("key")
  
  # Downloads and loads the PDFReader module
  PDFReader = download_loader("PDFReader")
  loader = PDFReader()
  
  # Load data from the 'Resume.pdf' file using the PDFReader. Insert the path of your file here. 
  documents = loader.load_data(file='Resume.pdf') 
  
  # Create an index for the loaded documents
  index = GPTVectorStoreIndex(documents)
  
  # Save the index in a .JSON file for repeated use (to save on ADA API calls)
  query_engine = index.as_query_engine()

  #Pass the queries you wish here. Ex:"Give me essential details such as name, email, phone number and work experience if any?"
  text_input=input("What information would you like to retrieve?")
  # Query the index for essential details such as name, email, phone number, and work experience
  response = query_engine.query(text_input)
  
  # Print the response
  print(response)
main()
