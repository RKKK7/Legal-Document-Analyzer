# 📜 Legal Document Analyzer

A comprehensive AI-powered legal document analysis platform built with Streamlit and Groq API, specializing in Indian law. This platform helps users analyze legal documents, detect risks, simplify legal jargon, generate legal guides, and get instant answers to legal questions through an intelligent chatbot.


---

## 🌟 Features

### 1. **AI-Powered Legal Chatbot**
- Intelligent conversational AI specialized in Indian law
- Answers ANY legal question with detailed, context-aware responses
- References specific Indian acts, sections, and court precedents
- Maintains conversation context for follow-up questions
- Beautiful gradient UI with message history

### 2. **Document Analysis**
- **Upload & Process:** Support for PDF and DOCX documents
- **Smart Summarization:** AI-generated summaries highlighting key clauses and obligations
- **Risk Detection:** Automatically identifies risky clauses with confidence scores
- **Jargon Simplification:** Converts complex legal terms to plain English
- **Risk Scoring:** Overall document risk assessment with color-coded indicators

### 3. **Legal Guides Generator**
- Generate ultra-detailed, comprehensive legal guides on any topic
- 5000-8000 word guides with 15+ sections
- Step-by-step procedures specific to Indian legal system
- Complete document checklists and fee breakdowns
- Relevant case law and practical tips
- Downloadable in Markdown format

### 4. **Interactive Legal Quiz**
- Test your legal knowledge with multiple-choice questions
- Immediate feedback with detailed explanations
- Score tracking and progress monitoring
- Questions on Indian law and legal concepts

### 5. **Insights Dashboard**
- Document analytics and statistics
- Risk trend analysis
- Common risky phrases identification
- Visual charts and graphs

---

## 🎯 Key Highlights

- ✅ **India-First:** All responses default to Indian law, Indian Constitution, and Indian legal framework
- ✅ **Comprehensive:** Detailed, practical information that users can actually use
- ✅ **User-Friendly:** Clean, modern UI with excellent readability
- ✅ **AI-Powered:** Uses Groq API with Llama 3.3 70B model for intelligent responses
- ✅ **No Legal Knowledge Required:** Explains everything in simple, understandable language

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Groq API key (free tier available)
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/legal-document-analyzer.git
cd legal-document-analyzer
```

2. **Create a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download required NLP models**
```bash
# Download NLTK data
python -m nltk.downloader punkt stopwords averaged_perceptron_tagger

# Download spaCy model
python -m spacy download en_core_web_sm
```

5. **Set up API key**

Create a `.env` file in the project root:
```env
GROUPQ_API_KEY=your_groq_api_key_here
```

Get your free API key from [Groq Console](https://console.groq.com/keys)

6. **Run the application**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
legal-document-analyzer/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .env                           # Environment variables (API keys)
├── .gitignore                     # Git ignore file
│
├── config/
│   ├── __init__.py
│   └── config.py                  # Configuration settings
│
├── pages/
│   ├── __init__.py
│   ├── home.py                    # Home page
│   ├── document_analysis.py       # Document upload & analysis
│   ├── insights.py                # Analytics dashboard
│   ├── chatbot.py                 # Interactive chatbot
│   └── legal_guides.py            # AI-generated guides
│
├── services/
│   ├── __init__.py
│   ├── groupq_service.py          # Groq API integration
│   ├── document_processor.py      # Document text extraction
│   └── risk_scoring.py            # Risk calculation logic
│
├── models/
│   ├── __init__.py
│   ├── summarization.py           # Text summarization
│   ├── simplification.py          # Legal jargon simplification
│   ├── risk_detection.py          # Risk clause detection
│   └── translation.py             # Multilingual translation
│
├── utils/
│   ├── __init__.py
│   ├── document_utils.py          # Helper functions
│   └── visualization.py           # Charts and graphs
│
├── data/
│   ├── dictionaries/
│   │   ├── legal_terms.json       # Legal terminology database
│   │   └── risk_keywords.json     # Risk keyword patterns
│   └── training/
│       ├── legal_jargon.csv       # Jargon to plain English mapping
│       ├── risk_clauses.csv       # Sample risky clauses
│       └── legal_quiz.json        # Quiz questions database
│
└── temp/                          # Temporary file storage
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# API Configuration
GROUPQ_API_KEY=your_groq_api_key_here

# Optional Configurations
SUMMARIZATION_MODEL=groupq
RISK_DETECTION_MODEL=rule_based
TRANSLATION_MODEL=googletrans
SIMPLIFICATION_MODEL=groupq
```

### Supported Languages

The platform supports translation to multiple Indian languages:
- Hindi (हिन्दी)
- Marathi (मराठी)
- Tamil (தமிழ்)
- Telugu (తెలుగు)
- Kannada (ಕನ್ನಡ)
- Malayalam (മലയാളം)
- Bengali (বাংলা)
- Gujarati (ગુજરાતી)
- Punjabi (ਪੰਜਾਬੀ)

---

## 💡 Usage Examples

### Chatbot Queries

**Example 1: Understanding Legal Concepts**
```
User: "What is bail in India?"
Bot: [Detailed response with CrPC sections, types of bail, procedures]
```

**Example 2: Legal Procedures**
```
User: "How to file a consumer complaint?"
Bot: [Step-by-step guide with Consumer Protection Act details]
```

### Document Analysis

1. Upload a legal document (PDF/DOCX)
2. Navigate through tabs:
   - **Summary:** Get AI-generated summary
   - **Risk Analysis:** See detected risky clauses
   - **Simplification:** View plain English version

### Legal Guides

1. Go to "Legal Guides" page
2. Select a topic or enter your own
3. Click "Generate Guide"
4. Get a comprehensive 5000+ word manual
5. Download as Markdown file

---

## 🎨 UI Features

- **Modern Design:** Clean, professional interface with gradient backgrounds
- **Dark Mode Compatible:** Excellent contrast and readability
- **Responsive:** Works on desktop, tablet, and mobile
- **Intuitive Navigation:** Tab-based interface for easy access
- **Visual Feedback:** Loading spinners, success messages, and progress indicators

---

## 🔒 Security & Privacy

- **API Key Security:** Stored in `.env` file, never committed to version control
- **Data Privacy:** Documents processed locally, only text sent to AI for analysis
- **No Permanent Storage:** Uploaded documents stored temporarily in session
- **Secure Communication:** HTTPS communication with Groq API

---

## 📊 Performance

- **Response Time:** 2-5 seconds for chatbot queries
- **Document Processing:** 5-15 seconds depending on size
- **Legal Guides:** 10-20 seconds for comprehensive guides
- **Max File Size:** 10 MB for document uploads

---

## 🛠️ Technology Stack

### Frontend
- **Streamlit 1.30.0** - Web framework
- **Custom CSS** - Styling and UI enhancements

### Backend
- **Python 3.9+** - Programming language
- **Groq API** - AI text generation (Llama 3.3 70B)
- **NLTK** - Natural language processing
- **spaCy** - Advanced NLP tasks

### Document Processing
- **PyPDF2** - PDF text extraction
- **python-docx** - DOCX processing
- **pdfplumber** - Advanced PDF parsing

### Data Analysis
- **pandas** - Data manipulation
- **scikit-learn** - ML algorithms
- **matplotlib, seaborn, plotly** - Visualizations

### Translation
- **googletrans** - Multi-language support

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Add docstrings to all functions and classes
- Update README.md for significant changes
- Test thoroughly before submitting PR

---

## 🐛 Known Issues & Limitations

- **Rate Limits:** Free tier Groq API has limits (30 requests/minute)
- **Document Size:** Large documents (>10 MB) may take longer to process
- **OCR:** Scanned PDFs require OCR preprocessing (not included)
- **Languages:** Translation quality varies by language
- **Legal Advice:** Platform provides information only, not legal advice

---

## 📝 Roadmap

### Version 2.0 (Planned)
- [ ] User authentication and profiles
- [ ] Document version control
- [ ] Batch document processing
- [ ] REST API endpoints
- [ ] Export to PDF/DOCX
- [ ] Document comparison feature
- [ ] Email notifications
- [ ] Admin dashboard

### Future Enhancements
- [ ] Fine-tuned models on legal corpus
- [ ] Custom NER for legal entities
- [ ] Citation extraction
- [ ] Clause classification ML model
- [ ] Document similarity search
- [ ] Voice input support

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Groq** for providing powerful AI API
- **Streamlit** for the amazing web framework
- **NLTK & spaCy** for NLP capabilities
- **Indian Legal Community** for inspiring this project

---

## 📧 Contact

**Project Maintainer:** S RAVI

For questions, suggestions, or support:
- Create an issue on GitHub
- Email: [your-email@example.com]

---

## ⚖️ Disclaimer

**IMPORTANT:** This platform provides general legal information only and should NOT be considered as legal advice. Always consult with a qualified legal professional for specific legal matters. The developers assume no liability for decisions made based on information provided by this platform.

---

## 📸 Screenshots

### Chatbot Interface
![Chatbot](screenshots/chatbot.png)
*Beautiful gradient UI with intelligent responses*

### Document Analysis
![Document Analysis](screenshots/document-analysis.png)
*Comprehensive document risk analysis*

### Legal Guides
![Legal Guides](screenshots/legal-guides.png)
*Ultra-detailed legal guides generation*

---

## 🌟 Star History

If you find this project useful, please consider giving it a ⭐ on GitHub!

---

<div align="center">

**Made with ❤️ for the Indian Legal Community**

[Report Bug](https://github.com/yourusername/legal-document-analyzer/issues) · [Request Feature](https://github.com/yourusername/legal-document-analyzer/issues)

</div>
