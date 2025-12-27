import streamlit as st
import requests

# Page setup
st.set_page_config(page_title="Local LLM Chat", layout="wide")

# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    
    # Check Ollama status
    try:
        requests.get("http://localhost:11434/api/tags", timeout=3)
        st.success("✅ Ollama is running")
    except:
        st.error("❌ Ollama not running")
    
    # Clear button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Main chat
st.title("🤖 Local LLM Chat Interface")
st.markdown("**Chat with your local AI model**")

# Show chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input area
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Show assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Call Ollama
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "llama3.1:8b",
                        "prompt": user_input,
                        "stream": False
                    },
                    timeout=30
                )
                
                if response.status_code == 200:
                    answer = response.json()["response"]
                    st.markdown(answer)
                    # Save to history
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error(f"Error: API returned {response.status_code}")
                    
            except requests.exceptions.ConnectionError:
                st.warning("Cannot connect to Ollama. Make sure 'ollama serve' is running.")
            except Exception as e:
                st.error(f"Error: {str(e)}")
