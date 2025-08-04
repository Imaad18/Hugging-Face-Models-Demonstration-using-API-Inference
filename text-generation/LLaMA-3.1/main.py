import os
from huggingface_hub import InferenceClient
from typing import List, Dict
import time

def initialize_client() -> InferenceClient:
    """Initialize the InferenceClient with error handling."""
    try:
        api_key = os.environ.get("HF_TOKEN")
        if not api_key:
            raise ValueError("HF_TOKEN environment variable not set")
        
        return InferenceClient(
            provider="novita",
            api_key=api_key,
            timeout=30
        )
    except Exception as e:
        print(f"Failed to initialize client: {str(e)}")
        raise

def create_conversation_history() -> List[Dict[str, str]]:
    """Create a sample conversation history."""
    return [
        {"role": "system", "content": "You are a knowledgeable assistant providing detailed and accurate answers."},
        {"role": "user", "content": "What is the capital of France?"},
        {"role": "assistant", "content": "The capital of France is Paris."},
        {"role": "user", "content": "Can you tell me more about its history?"}
    ]

def stream_response(client: InferenceClient, messages: List[Dict[str, str]]) -> None:
    """Stream the model's response with advanced configuration."""
    try:
        # Configure advanced parameters for the model
        stream = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=messages,
            max_tokens=500,
            temperature=0.7,
            top_p=0.9,
            top_k=50,
            presence_penalty=0.2,
            frequency_penalty=0.3,
            stream=True
        )

        print("\nStreaming response:\n")
        start_time = time.time()
        
        # Process streaming response
        for chunk in stream:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
        
        print(f"\n\nResponse completed in {time.time() - start_time:.2f} seconds")
        
    except Exception as e:
        print(f"Error during streaming: {str(e)}")

def main():
    """Main function to demonstrate advanced model features."""
    try:
        # Initialize client
        client = initialize_client()
        
        # Create conversation history
        messages = create_conversation_history()
        
        # Print conversation context
        print("Conversation History:")
        for msg in messages:
            print(f"{msg['role'].capitalize()}: {msg['content']}")
        
        # Stream the response
        stream_response(client, messages)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
