"""
Legal chatbot page for the Legal AI Platform
"""
import streamlit as st
import random
import json
import os
from typing import Dict, List, Any
import pandas as pd
from config.config import DATA_DIR

def get_mock_chat_response(query: str) -> str:
    """Get detailed response for the chatbot based on query content"""
    
    query_lower = query.lower()
    
    # Dictionary of detailed responses for specific legal topics
    responses = {
        "contract": "A contract is a legally binding agreement between two or more parties. For a contract to be valid, it needs:\n\n1. An offer from one party\n2. Acceptance of that offer by another party\n3. Consideration (something of value exchanged)\n4. Legal capacity of both parties (they must be adults of sound mind)\n5. A lawful purpose\n\nContracts can be written or verbal, though some types (like real estate) must be in writing to be enforceable.",
        
        "nda": "A Non-Disclosure Agreement (NDA) is a legal contract where parties agree to keep certain information confidential. Key elements include:\n\n1. Definition of what information is considered confidential\n2. How the confidential information can be used\n3. Duration of the confidentiality obligation\n4. Consequences for breaching the agreement\n\nNDAs are commonly used in business relationships, employment, and when discussing potential partnerships.",
        
        "alimony": "Alimony (also called spousal support) is a legal obligation where one spouse provides financial support to the other after separation or divorce. The court considers:\n\n1. Marriage duration\n2. Each spouse's age and health\n3. Income and earning capacity of each spouse\n4. Standard of living during marriage\n5. Contributions to the marriage (including as a homemaker)\n\nAlimony can be temporary or permanent, and ends if the receiving spouse remarries.",
        
        "rights as a consumer": "As a consumer in India, you have these key rights under the Consumer Protection Act, 2019:\n\n1. Right to Safety - Protection against hazardous goods and services\n2. Right to Information - Complete information about products\n3. Right to Choose - Access to a variety of goods at competitive prices\n4. Right to be Heard - Your interests receive due consideration\n5. Right to Seek Redressal - Compensation for unfair practices\n6. Right to Consumer Education - Knowledge about your rights\n\nYou can file complaints with the Consumer Disputes Redressal Commission at district, state, or national levels.",
        
        "police complaint": "To file a police complaint (FIR) in India, follow these steps:\n\n1. Visit the police station with jurisdiction over the area where the incident occurred\n2. Provide a detailed written statement about the incident\n3. The officer must register your FIR and give you a copy for free\n4. Get the FIR number for future reference\n5. Follow up on the investigation\n\nIf police refuse to file your FIR, you can approach the Superintendent of Police or file a complaint with the Magistrate under Section 156(3) of CrPC.",
        
        "intellectual property": "Intellectual Property (IP) refers to creations of the mind that are protected by law. The main types are:\n\n1. Patents - Protect inventions (valid for 20 years in India)\n2. Trademarks - Protect brand names, logos, and slogans (renewable every 10 years)\n3. Copyrights - Protect creative works like books, music, and software (author's life + 60 years in India)\n4. Trade Secrets - Protect confidential business information\n\nIn India, IP rights are enforced through the courts, with specialized IP tribunals in major cities.",
        
        "divorce": "Divorce in India varies by personal law. Under Hindu Marriage Act, grounds include:\n\n1. Adultery\n2. Cruelty (physical or mental)\n3. Desertion for at least 2 years\n4. Conversion to another religion\n5. Mental disorder\n6. Communicable disease\n7. Mutual consent (with 1-year separation)\n\nThe process typically involves filing a petition, attempts at reconciliation, evidence presentation, and final decree. Mutual consent divorces are faster (6-18 months) than contested ones (3+ years).",
        
        "legal age to marry": "In India, the legal age to marry is:\n\n- For males: 21 years\n- For females: 18 years\n\nThese ages are set by the Prohibition of Child Marriage Act, 2006. Marriages below these ages are voidable (can be nullified) but not automatically void. Officials who conduct child marriages and parents who permit them can face imprisonment up to 2 years and fines up to ₹1 lakh.",
        
        "will": "A will is a legal document that specifies how your property should be distributed after death. To make a valid will in India:\n\n1. You must be 18+ years old and of sound mind\n2. It must be in writing\n3. It should be signed by you\n4. At least two witnesses must sign in your presence\n\nWills don't need to be registered or notarized, though registration provides stronger legal protection. Without a will, property is distributed according to succession laws based on religion.",
        
        "rti": "The Right to Information (RTI) Act gives Indian citizens the right to request information from government bodies. Process:\n\n1. Submit application to the Public Information Officer (PIO) with ₹10 fee\n2. Information must be provided within 30 days (48 hours for life/liberty matters)\n3. If denied, you can appeal to a senior officer, then to Information Commission\n\nExemptions include national security, cabinet papers, and personal information with no public interest.",
    }
    
    # Check for topic matches in the dictionary
    for keyword, response in responses.items():
        if keyword in query_lower:
            return response
    
    # Additional specific query matches
    if "legal age" in query_lower or "age to" in query_lower:
        if "vote" in query_lower or "voting" in query_lower:
            return "In India, the legal age to vote is 18 years. Any citizen who has reached 18 years of age on January 1st of the election year can register as a voter. This is established by the 61st Amendment of the Constitution of India, which lowered the voting age from 21 to 18 in 1989."
        
        if "drive" in query_lower or "driving" in query_lower:
            return "In India, the legal age to obtain a driving license is:\n\n- 16 years: For motorcycles below 50cc\n- 18 years: For cars and motorcycles above 50cc\n- 20 years: For commercial vehicles\n\nBefore getting a full license, you must obtain a learner's license and practice for at least 30 days."
        
        if "drink" in query_lower or "alcohol" in query_lower:
            return "In India, the legal drinking age varies by state:\n\n- 18 years: Himachal Pradesh, Sikkim, Puducherry\n- 21 years: Telangana, Maharashtra, Arunachal Pradesh\n- 25 years: Delhi, Haryana, Punjab\n\nSome states like Gujarat, Bihar, Nagaland, and Mizoram prohibit alcohol completely."
    
    if "gst" in query_lower or "goods and services tax" in query_lower:
        return "Goods and Services Tax (GST) in India is a comprehensive indirect tax on manufacture, sale, and consumption of goods and services. Key facts:\n\n1. Implemented on July 1, 2017\n2. Replaced multiple taxes like VAT, Service Tax, Excise Duty\n3. Main rates: 0%, 5%, 12%, 18%, and 28%\n4. Businesses with turnover above ₹40 lakhs must register (₹20 lakhs in some states)\n5. Returns are filed monthly or quarterly\n\nThe GST Council decides rates and policies, and the system operates through GSTN portal."
    
    if "tenant" in query_lower or "landlord" in query_lower or "rent" in query_lower:
        return "Tenancy laws in India vary by state, but generally:\n\n1. Rental agreements should be in writing and registered\n2. Security deposits are typically 2-3 months' rent (up to 10 months in Bangalore)\n3. Notice period for vacating is usually 1-3 months\n4. Landlords must maintain essential services and structural repairs\n5. Tenants must pay rent on time and maintain the property\n\nThe Model Tenancy Act, 2021 aims to standardize these laws but states need to adopt it."
    
    # General response for queries that don't match specific topics
    general_responses = [
        f"Regarding '{query}': This is a complex legal matter that depends on specific circumstances and applicable laws. Consider consulting with a qualified legal professional for advice tailored to your situation.",
        f"On the topic of '{query}': Legal interpretations vary based on jurisdiction and case specifics. This area of law involves multiple factors including applicable statutes, case precedents, and specific circumstances of each case.",
        f"About '{query}': This legal question requires consideration of relevant laws, court decisions, and specific facts of your situation. For definitive guidance, consulting a legal professional is recommended.",
        f"For your query on '{query}': The legal position involves analyzing applicable laws, regulations, and how courts have interpreted similar situations. A legal professional can provide advice specific to your circumstances."
    ]
    
    return random.choice(general_responses)

def load_quiz_data():
    """Load quiz data from JSON file or create a default set"""
    quiz_data_path = os.path.join(DATA_DIR, "training", "legal_quiz.json")
    
    # Default quiz data if file doesn't exist
    if not os.path.exists(quiz_data_path):
        default_quiz_data = [
            {
                "question": "Under Indian Contract Act, what is the minimum age for entering into a valid contract?",
                "options": [
                    "16 years", 
                    "18 years", 
                    "21 years", 
                    "No minimum age"
                ],
                "correct_answer": 1,
                "explanation": "According to the Indian Contract Act, a person must be at least 18 years old to enter into a valid contract. Contracts made by minors (under 18) are typically void."
            },
            {
                "question": "Which of the following is NOT an essential element of a valid contract?",
                "options": [
                    "Offer and acceptance", 
                    "Free consent", 
                    "Written documentation", 
                    "Lawful consideration"
                ],
                "correct_answer": 2,
                "explanation": "Written documentation is NOT an essential element of a valid contract in India. Verbal contracts can be valid as long as they contain other essential elements like offer, acceptance, free consent, lawful consideration, and lawful object."
            },
            {
                "question": "Under the Right to Information Act, within how many days must a public authority provide information?",
                "options": [
                    "10 days", 
                    "30 days", 
                    "45 days", 
                    "60 days"
                ],
                "correct_answer": 1,
                "explanation": "Under the Right to Information Act, 2005, a public authority is required to provide information within 30 days of receiving the request. In cases involving life or liberty, information must be provided within 48 hours."
            },
            {
                "question": "What is the limitation period for filing a suit for recovery of movable property under the Limitation Act?",
                "options": [
                    "1 year", 
                    "3 years", 
                    "7 years", 
                    "12 years"
                ],
                "correct_answer": 1,
                "explanation": "Under the Limitation Act, 1963, the limitation period for filing a suit for recovery of movable property is 3 years from the date when the right to sue accrues."
            },
            {
                "question": "Which of the following is a valid ground for divorce under the Hindu Marriage Act?",
                "options": [
                    "Different political opinions", 
                    "Conversion to another religion", 
                    "Financial disagreements", 
                    "Different food preferences"
                ],
                "correct_answer": 1,
                "explanation": "Conversion to another religion is a valid ground for divorce under the Hindu Marriage Act, 1955. Other grounds include adultery, cruelty, desertion, mental disorder, communicable disease, renunciation, and presumption of death."
            }
        ]
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(quiz_data_path), exist_ok=True)
        
        # Save default quiz data
        with open(quiz_data_path, 'w') as f:
            json.dump(default_quiz_data, f, indent=2)
        
        return default_quiz_data
    
    # Load quiz data from file
    try:
        with open(quiz_data_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading quiz data: {e}")
        return []

def show_chatbot_page():
    """Display the legal chatbot page"""
    
    # Main heading
    st.markdown('<h1 class="main-header">Legal Chatbot & Quiz</h1>', unsafe_allow_html=True)
    
    # Create tabs for chatbot and quiz
    tabs = st.tabs(["Legal Chatbot", "Legal Quiz"])
    
    # Chatbot tab
    with tabs[0]:
        show_chatbot_tab()
    
    # Quiz tab
    with tabs[1]:
        show_quiz_tab()

def show_chatbot_tab():
    """Display the legal chatbot tab"""
    
    # Initialize Groq service if not already initialized
    if 'groupq_service' not in st.session_state:
        from services.groupq_service import GroupQService
        st.session_state.groupq_service = GroupQService()
    
    # Custom CSS for better chat styling
    st.markdown("""
    <style>
    .chat-container {
        max-height: 500px;
        overflow-y: auto;
        padding: 20px;
        margin-bottom: 20px;
    }
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px 20px;
        border-radius: 18px;
        margin: 10px 0;
        margin-left: 20%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .assistant-message {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 15px 20px;
        border-radius: 18px;
        margin: 10px 0;
        margin-right: 20%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .message-label {
        font-weight: bold;
        font-size: 0.9em;
        margin-bottom: 8px;
        opacity: 0.9;
    }
    .message-content {
        line-height: 1.6;
        font-size: 1em;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 10px 30px;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    .info-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 4px solid #667eea;
        color: #1a1a1a;
        font-weight: 500;
    }
    .info-box strong {
        color: #000000;
        font-weight: 700;
    }
    .sample-question {
        background-color: #f8f9fa;
        color: #333;
        padding: 10px 15px;
        border-radius: 20px;
        margin: 5px;
        display: inline-block;
        border: 2px solid #667eea;
        cursor: pointer;
        transition: all 0.3s;
    }
    .sample-question:hover {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("### 💬 Legal Chatbot")
    
    # Info box
    st.markdown("""
    <div class="info-box">
        <strong>ℹ️ How to use:</strong> Ask questions about legal concepts, processes, or documents. 
        The chatbot can help you understand legal terminology, explain procedures, and provide general legal information.
        <br><br>
        <strong>⚠️ Note:</strong> This chatbot provides general information only and not legal advice.
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize chat history if not already in session
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Display chat history with improved styling
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    if not st.session_state.chat_history:
        st.markdown("""
        <div style="text-align: center; padding: 40px; color: #666;">
            <h3>👋 Welcome to Legal Assistant!</h3>
            <p>Ask me any legal question to get started.</p>
        </div>
        """, unsafe_allow_html=True)
    
    for message in st.session_state.chat_history:
        role = message.get("role", "user")
        content = message.get("content", "")
        
        if role == "user":
            st.markdown(f"""
            <div class="user-message">
                <div class="message-label">👤 You</div>
                <div class="message-content">{content}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="assistant-message">
                <div class="message-label">⚖️ Legal Assistant</div>
                <div class="message-content">{content}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Use a form to handle input submission
    with st.form(key="chat_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])
        with col1:
            user_input = st.text_input("💭 Ask a legal question:", key="chat_input_field", label_visibility="collapsed", placeholder="Type your legal question here...")
        with col2:
            submit_button = st.form_submit_button("📤 Send", use_container_width=True)
        
        if submit_button and user_input and user_input.strip():
            # Add user message to chat history
            st.session_state.chat_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Get response from Groq API
            with st.spinner("Thinking..."):
                response = st.session_state.groupq_service.chat_query(
                    user_input,
                    st.session_state.chat_history
                )
            
            # Add assistant message to chat history
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": response
            })
            
            # Rerun to update chat display
            st.rerun()
    
    # Clear chat button
    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        if st.button("🗑️ Clear Chat", key="clear_button", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()
    
    # Sample questions
    st.markdown("---")
    st.markdown("### 💡 Sample Questions")
    st.markdown("Click on any question below to see the answer:")
    
    sample_questions = [
        ("📄 What is a contract?", "contract"),
        ("🛡️ What are my rights as a consumer?", "consumer rights"),
        ("💍 What is the legal age to marry?", "marriage age"),
        ("🚔 How do I file a police complaint?", "police complaint"),
        ("💰 What is alimony?", "alimony"),
        ("🧠 What is intellectual property law?", "intellectual property"),
        ("📝 What is an NDA?", "nda"),
        ("⚖️ What is RTI?", "rti")
    ]
    
    # Display sample questions in columns with better styling
    cols = st.columns(2)
    for i, (question_text, question_key) in enumerate(sample_questions):
        with cols[i % 2]:
            if st.button(question_text, key=f"sample_{question_key}_{i}", use_container_width=True):
                # Extract the actual question without emoji
                actual_question = question_text.split(" ", 1)[1] if " " in question_text else question_text
                
                # Add question to chat history
                st.session_state.chat_history.append({
                    "role": "user",
                    "content": actual_question
                })
                
                # Get response from Groq API
                response = st.session_state.groupq_service.chat_query(
                    actual_question,
                    st.session_state.chat_history
                )
                
                # Add response to chat history
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": response
                })
                
                # Rerun to update chat display
                st.rerun()

def show_quiz_tab():
    """Display the legal quiz tab"""
    
    # Custom CSS for quiz
    st.markdown("""
    <style>
    .quiz-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .quiz-question {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 5px solid #667eea;
        font-size: 1.1em;
        font-weight: 600;
        color: #333;
    }
    .score-badge {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 25px;
        display: inline-block;
        font-weight: bold;
        margin: 10px 0;
    }
    .explanation-box {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 15px;
        border-radius: 10px;
        margin-top: 15px;
        color: #333;
        border-left: 4px solid #f5576c;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="quiz-header"><h2>📚 Legal Knowledge Quiz</h2><p>Test your legal knowledge with interactive questions!</p></div>', unsafe_allow_html=True)
    
    # Load quiz data
    quiz_data = load_quiz_data()
    
    if not quiz_data:
        st.error("No quiz questions available.")
        return
    
    # Initialize quiz state if not already in session
    if 'quiz_state' not in st.session_state:
        st.session_state.quiz_state = {
            "current_question": 0,
            "score": 0,
            "questions_answered": set(),
            "last_answer": None,
            "last_correct": None,
            "available_questions": list(range(len(quiz_data)))
        }
    
    # Current question index
    current_idx = st.session_state.quiz_state["current_question"]
    
    # Ensure current index is valid
    if len(quiz_data) > 0:
        current_idx = current_idx % len(quiz_data)
        st.session_state.quiz_state["current_question"] = current_idx
    
        # Get current question
        question = quiz_data[current_idx]
        
        # Display score
        total_answered = len(st.session_state.quiz_state["questions_answered"])
        st.markdown(f'<div class="score-badge">📊 Score: {st.session_state.quiz_state["score"]} / {total_answered}</div>', unsafe_allow_html=True)
        
        # Display question
        st.markdown(f"**Question {current_idx + 1} of {len(quiz_data)}**")
        st.markdown(f'<div class="quiz-question">{question["question"]}</div>', unsafe_allow_html=True)
        
        # Check if this question has been answered
        already_answered = current_idx in st.session_state.quiz_state["questions_answered"]
        
        # Display options as buttons or show previous answer
        if not already_answered:
            st.markdown("**Select your answer:**")
            for i, option in enumerate(question["options"]):
                if st.button(f"{chr(65+i)}. {option}", key=f"option_{i}", use_container_width=True):
                    # Record answer
                    st.session_state.quiz_state["last_answer"] = i
                    st.session_state.quiz_state["last_correct"] = (i == question["correct_answer"])
                    
                    # Update score
                    if i == question["correct_answer"]:
                        st.session_state.quiz_state["score"] += 1
                    
                    # Mark question as answered
                    st.session_state.quiz_state["questions_answered"].add(current_idx)
                    
                    # Rerun to show result
                    st.rerun()
        else:
            # Show options with correct one highlighted
            st.markdown("**Your answer:**")
            for i, option in enumerate(question["options"]):
                if i == question["correct_answer"]:
                    st.success(f"✅ **{chr(65+i)}. {option}** (Correct Answer)")
                elif i == st.session_state.quiz_state["last_answer"]:
                    st.error(f"❌ {chr(65+i)}. {option} (Your Answer)")
                else:
                    st.info(f"{chr(65+i)}. {option}")
            
            # Show explanation
            st.markdown(f'<div class="explanation-box"><strong>💡 Explanation:</strong><br>{question["explanation"]}</div>', unsafe_allow_html=True)
        
        # Navigation buttons
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Previous Question", use_container_width=True):
                # Go to previous question
                st.session_state.quiz_state["current_question"] = (current_idx - 1) % len(quiz_data)
                st.rerun()
        
        with col2:
            if st.button("Next Question", use_container_width=True):
                # Go to next question
                st.session_state.quiz_state["current_question"] = (current_idx + 1) % len(quiz_data)
                st.rerun()
        
        # Display score
        st.markdown("---")
        st.markdown(f"**Current Score:** {st.session_state.quiz_state['score']} / {len(st.session_state.quiz_state['questions_answered'])}")
        
        # Progress bar
        progress = len(st.session_state.quiz_state["questions_answered"]) / len(quiz_data)
        st.progress(progress)
    
    # Reset quiz button
    if st.button("Reset Quiz"):
        # Select random questions for the next quiz session
        available_indices = list(range(len(quiz_data)))
        random.shuffle(available_indices)
        
        st.session_state.quiz_state = {
            "current_question": 0,
            "score": 0,
            "questions_answered": set(),
            "last_answer": None,
            "last_correct": None,
            "available_questions": available_indices
        }
        st.rerun()