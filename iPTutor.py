import os
from flask import Flask, render_template, request, jsonify
import nltk

nltk.download('punkt')

current_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(current_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

knowledge_base = {
    "define context diagram": "A context diagram is a high-level, simplified view of a system that shows the system as a single process with its interactions with external entities.",
    "define cd": "A context diagram is a high-level, simplified view of a system that shows the system as a single process with its interactions with external entities.",
    
    "how to create context diagram": "To create a context diagram: 1. Identify the main system. 2. Identify external entities. 3. Draw the system as a single process. 4. Place external entities around the system. 5. Use arrows to show data flow.",
    "create context diagram": "To create a context diagram: 1. Identify the main system. 2. Identify external entities. 3. Draw the system as a single process. 4. Place external entities around the system. 5. Use arrows to show data flow.",
    "create cd": "To create a context diagram: 1. Identify the main system. 2. Identify external entities. 3. Draw the system as a single process. 4. Place external entities around the system. 5. Use arrows to show data flow.",
    
    "describe context diagram online bookstore": "A context diagram for an online bookstore system would include the following elements:\n\n1. System: Online Bookstore\n2. External Entities:\n   - Customers: Users who browse and purchase books.\n   - Payment Gateway: External service for processing payments.\n   - Shipping Service: External service for delivering purchased books.\n   - Book Suppliers: External entities providing the books.\n\nInteractions:\n- Customers: Browse books, make purchases, and provide reviews.\n- Payment Gateway: Process payments for book purchases.\n- Shipping Service: Receive shipping requests and deliver books.\n- Book Suppliers: Supply books to the bookstore's inventory.",
    "describe cd online bookstore": "A context diagram for an online bookstore system would include the following elements:\n\n1. System: Online Bookstore\n2. External Entities:\n   - Customers: Users who browse and purchase books.\n   - Payment Gateway: External service for processing payments.\n   - Shipping Service: External service for delivering purchased books.\n   - Book Suppliers: External entities providing the books.\n\nInteractions:\n- Customers: Browse books, make purchases, and provide reviews.\n- Payment Gateway: Process payments for book purchases.\n- Shipping Service: Receive shipping requests and deliver books.\n- Book Suppliers: Supply books to the bookstore's inventory.",
    
    "define dfd": "A Data Flow Diagram (DFD) is a graphical representation of the flow of data through an information system.",
    
    "create dfd": "To create a DFD: 1. Identify external entities. 2. Identify processes. 3. Identify data stores. 4. Draw data flows between elements. 5. Label all elements and flows.",
    "how to create dfd": "To create a DFD: 1. Identify external entities. 2. Identify processes. 3. Identify data stores. 4. Draw data flows between elements. 5. Label all elements and flows.",
    
    "benefits of context diagram": "A context diagram helps to visualize the system as a whole and understand its boundaries and interactions with external entities. It provides clarity in system analysis, ensures communication between stakeholders, and simplifies complex systems into a single, manageable process.",
    "benefits of dfd": "A DFD helps to model how data moves through a system, showing the relationships between processes, external entities, and data stores. It aids in understanding system functionality, identifying potential issues, and improving communication between development teams and stakeholders.",
    "levels of dfd": "A DFD can be broken down into multiple levels:\n1. Level 0 DFD (Context Level): Shows the system as a whole with external entities and data flow.\n2. Level 1 DFD: Provides a deeper view by breaking the main process into sub-processes and showing data flow between them.\n3. Level 2+ DFD: Continues to decompose processes for further detail, refining each sub-process and its data flow.",
    "symbols in context diagram": "Common symbols in context diagrams include:\n- System (a single circle or box representing the system).\n- External Entities (rectangles for actors outside the system).\n- Data Flow (arrows showing the flow of data between the system and external entities).",
    "symbols in dfd": "Key symbols used in DFDs include:\n1. Process (a circle or rounded rectangle representing a function or operation).\n2. External Entity (a rectangle representing actors outside the system).\n3. Data Store (an open rectangle representing where data is stored).\n4. Data Flow (arrows representing the movement of data between processes, data stores, and external entities).",
    "common mistakes context diagram": "Common mistakes in creating context diagrams include:\n1. Adding too much detail (context diagrams should remain high-level).\n2. Forgetting external entities that interact with the system.\n3. Not showing data flow clearly between entities and the system.",
    "common mistakes dfd": "Common mistakes in creating DFDs include:\n1. Including system logic (DFDs focus on data flow, not decision points).\n2. Not distinguishing between processes and data stores.\n3. Mislabeling data flows or failing to label them at all.\n4. Creating a DFD that is too complex or too detailed for the current analysis.",
    "difference between context diagram and dfd": "A context diagram is a high-level, simplified view of a system that shows external entities and how they interact with the system as a single process. A DFD, on the other hand, breaks the system into multiple processes and shows how data flows between these processes, data stores, and external entities, offering a more detailed view.",
    "describe dfd online bookstore": "A DFD for an online bookstore might include processes like:\n1. Browse Books: Allows users to search and view available books.\n2. Make Purchase: Users place orders, and the system processes them.\n3. Manage Inventory: Updates book stock when purchases are made.\n4. Process Payment: Sends payment information to the payment gateway.\n\nExternal entities could include customers, payment gateway, shipping service, and book suppliers, with data stores for book inventory and user accounts.",
    "external entities": "represented by squares or rectangles, they interact with the system but are outside of it.",
    "entity":"People, systems, or organizations that interact with the system.",
    "process": "represented by circles or rectangular with rounded corrners. Every process has a name that identifies the function it performs.",
    "Data Store": "represented by open-ended rectangles, they store data.",
    "Data Flow": "represented by arrows, they show the flow of data.",
    "data store": "represented by open-ended rectangles, they store data.",
    "data flow": "represented by arrows, they show the flow of data."
}


exit_commands = ['quit', 'end', 'bye', 'exit']

def process_input(user_input):
    return user_input.lower().split()

def generate_response(tokens):
    user_input = " ".join(tokens)
    
    if user_input in exit_commands:
        return "Goodbye! Thank you for chatting."
    
    best_match = None
    max_matching_words = 0
    
    for key in knowledge_base:
        matching_words = sum(word in user_input for word in key.split())
        if matching_words > max_matching_words:
            max_matching_words = matching_words
            best_match = key
    
    if best_match:
        return knowledge_base[best_match]
    return "I'm sorry, I don't have information about that. Can you ask something else about context diagrams or DFDs?"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['user_input']
    tokens = process_input(user_input)
    response = generate_response(tokens)
    return jsonify({'response': response, 'exit': user_input.lower() in exit_commands})

if __name__ == '__main__':
    print("Current working directory:", os.getcwd())
    print("Absolute path of app.py:", os.path.abspath(__file__))
    print("Template directory:", template_dir)
    print("Contents of template directory:", os.listdir(template_dir))
    app.run(debug=True)