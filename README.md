# **Streamlit LLM Chat Interface**

A web application for interacting with locally-installed large language models (LLMs) through Ollama. This project provides a clean, interactive chat interface that runs entirely on your local machine.

## 📋 **Project Overview**

### **Features**
- 🎨 **Clean Web Interface**: Built with Streamlit for an intuitive user experience
- 💬 **Real-time Chat**: Interactive conversation with your local LLM
- 📜 **Conversation History**: Maintains context across multiple messages
- 🗑️ **Clear Chat Functionality**: Reset the conversation with one click
- 🔍 **Connection Status Monitoring**: Real-time Ollama server status indicator
- ⚡ **Error Handling**: Robust error messages for common issues
- 🔒 **Local & Private**: All processing happens on your machine - no data leaves your computer

### **Technology Stack**
- **Frontend**: Streamlit (Python web framework)
- **LLM Backend**: Ollama with Llama 3.1 8B model
- **Communication**: REST API calls via HTTP requests
- **Platform**: Cross-platform (Linux, macOS, Windows with WSL)

## 🚀 **Quick Start Guide**

### **Prerequisites**
1. **Python 3.8+** installed on your system
2. **Ollama** installed and configured
3. At least one LLM model downloaded via Ollama

### **Installation Steps**

#### **1. Install Ollama**
```bash
# Linux/macOS
curl -fsSL https://ollama.ai/install.sh | sh

# Windows: Download from https://ollama.ai/download
```

#### **2. Download a Model**
```bash
# Download Llama 3.1 8B (recommended)
ollama pull llama3.1:8b

# Alternative smaller models (faster, less resource-intensive)
# ollama pull gemma:2b
# ollama pull mistral:7b
```

#### **3. Clone and Setup the Project**
```bash
# Clone this repository
git clone https://github.com/YOUR-USERNAME/streamlit-llm-interface.git
cd streamlit-llm-interface

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### **4. Run the Application**
```bash
# Terminal 1: Start Ollama server (keep this running)
ollama serve

# Terminal 2: Run the Streamlit app
streamlit run app.py
```

#### **5. Open in Browser**
- The application will automatically open at `http://localhost:8501`
- If not, manually navigate to that address in your web browser

## 🖥️ **Application Interface**

### **Main Components**
1. **Sidebar (Left Panel)**:
   - Ollama connection status indicator
   - Current model information
   - Clear chat button
   - Usage instructions

2. **Main Chat Area (Center)**:
   - Conversation history display
   - User and assistant message bubbles
   - Input field at the bottom

### **How to Use**
1. **Check Connection**: Ensure the sidebar shows "✅ Ollama is running"
2. **Start Chatting**: Type your message in the input box at the bottom
3. **View Responses**: AI responses appear in assistant message bubbles
4. **Clear History**: Click "🗑️ Clear Chat" in the sidebar to start fresh
5. **Continue Conversation**: The model maintains context from previous messages

## 📁 **Project Structure**
```
streamlit-llm-interface/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python package dependencies
├── README.md          # This documentation file
├── .gitignore         # Git ignore rules
└── screenshots/       # Application screenshots (optional)
```

### **File Descriptions**
- **app.py**: Contains all the Streamlit application logic, UI components, and Ollama API integration
- **requirements.txt**: Lists Python dependencies (Streamlit and Requests)
- **README.md**: Project documentation and setup instructions

## 🔧 **Technical Implementation**

### **Key Components**
1. **Session State Management**: Uses `st.session_state` to maintain conversation history
2. **Ollama API Integration**: HTTP POST requests to `localhost:11434/api/generate`
3. **Error Handling**: Comprehensive try-catch blocks for network and API errors
4. **UI Components**: Streamlit's `st.chat_input`, `st.chat_message`, and sidebar widgets

### **API Configuration**
```python
# Default API settings (configurable in app.py)
API_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1:8b"
TIMEOUT = 30  # seconds
```

## 🐛 **Troubleshooting**

### **Common Issues & Solutions**

| Issue | Solution |
|-------|----------|
| **"Ollama not running"** | Start Ollama: `ollama serve` in a terminal |
| **"Connection refused"** | Check if port 11434 is accessible: `curl http://localhost:11434/api/tags` |
| **"Model not found"** | Download the model: `ollama pull llama3.1:8b` |
| **Streamlit not starting** | Check Python installation: `python --version` |
| **Slow responses** | Try a smaller model or check system resources |
| **Port 8501 already in use** | Use a different port: `streamlit run app.py --server.port 8502` |

### **Diagnostic Commands**
```bash
# Check Ollama status
curl http://localhost:11434/api/tags

# Check if Ollama process is running
ps aux | grep ollama

# Check if port is listening
netstat -tulpn | grep :11434  # Linux
lsof -i :11434                 # macOS
```

## 📊 **Performance Tips**

1. **For Faster Responses**:
   - Use smaller models like `gemma:2b` or `mistral:7b`
   - Ensure sufficient RAM/VRAM availability
   - Close other resource-intensive applications

2. **For Better Accuracy**:
   - Use larger models like `llama3.1:8b` or `llama3.1:70b`
   - Provide clear, specific prompts
   - Break complex questions into simpler parts

3. **Resource Requirements**:
   - **Llama 3.1 8B**: ~8GB RAM/VRAM recommended
   - **Streamlit App**: ~500MB RAM
   - **Total**: ~9GB system memory recommended

## 🔄 **Customization**

### **Changing the Model**
Edit `app.py` and modify the `MODEL` variable:
```python
# Line 50-55 in app.py
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.1:8b",  # Change this to your preferred model
        # ... rest of configuration
    }
)
```

### **Available Models**
- `llama3.1:8b` - Balanced performance (default)
- `llama3.1:70b` - Most capable (requires significant resources)
- `mistral:7b` - Good balance of speed and quality
- `gemma:2b` - Fastest, lightest option
- `codellama:7b` - Specialized for code generation

### **UI Customization**
Modify the `app.py` file to:
- Change colors and styling
- Add additional features (file upload, voice input, etc.)
- Modify layout and component arrangement
- Add model parameter controls (temperature, max tokens)

## 📝 **Development**

### **Setting Up Development Environment**
```bash
# Clone repository
git clone https://github.com/YOUR-USERNAME/streamlit-llm-interface.git

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -r requirements.txt
pip install black flake8  # Optional: code formatting and linting

# Run with auto-reload for development
streamlit run app.py --server.runOnSave true
```

### **Code Structure**
```python
# app.py main sections:
1. Imports and configuration
2. Session state initialization
3. Sidebar UI components
4. Main chat interface
5. Message handling logic
6. Ollama API integration
7. Error handling
```

## 🤝 **Contributing**

### **How to Contribute**
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

### **Feature Ideas**
- [ ] Multiple model support with dropdown selector
- [ ] Conversation export/import functionality
- [ ] Model parameter controls (temperature, top-p, etc.)
- [ ] Dark/light mode toggle
- [ ] Voice input/output support
- [ ] File upload for document analysis
- [ ] Plugin system for extended functionality

## 📄 **License**

This project is open source and available for educational and personal use. For commercial use, please check the licenses of the underlying components (Ollama, Streamlit, and the LLM models).

## 🙏 **Acknowledgments**

- **Ollama Team** for making local LLMs accessible
- **Streamlit Team** for the amazing web framework
- **Meta AI** for the Llama models
- **All open-source contributors** who make projects like this possible

## 📧 **Support & Contact**

For issues, questions, or feedback:
1. Check the [Issues](https://github.com/YOUR-USERNAME/streamlit-llm-interface/issues) page
2. Review the troubleshooting section above
3. Submit a detailed bug report with system information

## 🎯 **Learning Outcomes**

This project demonstrates:
- Building web interfaces with Streamlit
- Integrating local AI models via APIs
- Session management in web applications
- Error handling and user feedback
- Local-first application development
- Python backend development

---

**Happy Chatting!** 🤖💬

*Note: AI responses may contain inaccuracies. Always verify important information from authoritative sources.*
