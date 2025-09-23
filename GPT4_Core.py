import time
import os
import openai
from openai import AzureOpenAI
from openai import RateLimitError, APIError
from dotenv import load_dotenv

openai.api_key = ""

load_dotenv()

CHAT_KEY = os.getenv("AZURE_CHAT_API_KEY")
CHAT_ENDPOINT = os.getenv("AZURE_CHAT_ENDPOINT")
CHAT_DEPLOYMENT = os.getenv("AZURE_CHAT_DEPLOYMENT")


chat_client = AzureOpenAI(
    api_key=CHAT_KEY,
    azure_endpoint=CHAT_ENDPOINT,
    api_version="2025-01-01-preview"
)

class Agent:
    def __init__(self, temperature=0.8, model='gpt-4', max_tokens=100):
        self.temperature = temperature
        self.model = model
        self.max_tokens = max_tokens
        self.token_usage=[]
    
    def communicate(self, context):
        prompt = context + "\n\n"
        message = ""

        retries = 3
        backoff_factor = 2
        current_retry = 0

        while current_retry < retries:
            try:
                print(f"\n=== SYSTEM PROMPT DEBUG ===\n{context}\n============================\n")
                response = chat_client.chat.completions.create(
                    model=CHAT_DEPLOYMENT,
                    messages=[
                        {"role": "system", "content": context},
                        {"role": "user", "content": ""}
                    ],
                    max_tokens=self.max_tokens,
                    n=1,
                    temperature=self.temperature,
                    top_p=1
                )
                
                message = response.choices[0].message.content.strip()

                #Token used tracking
                if hasattr(response, "usage") and response.usage is not None:
                    total_tokens= response.usage.total_tokens
                    self.token_usage.append(total_tokens)
                else:
                    self.token_usage.append(0)    #this is the feedback if token info not returned 
                    
                return message
            except RateLimitError as e:
                if current_retry < retries - 1:
                    wait_time = backoff_factor ** current_retry
                    print(f"RateLimitError: Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                    current_retry += 1
                else:
                    print(f"Error {e}")
                    raise e
            except APIError as e:
                if current_retry < retries - 1:
                    wait_time = backoff_factor ** current_retry
                    print(f"RateLimitError: Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                    current_retry += 1
                else:
                    raise e
            except APIError as e:
                if current_retry < retries - 1:
                    wait_time = backoff_factor ** current_retry
                    print(f"RateLimitError: Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                    current_retry += 1
                else:
                    print(f"Error {e}")
                    raise e
