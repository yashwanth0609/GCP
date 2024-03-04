from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    # Process the user input and generate a response
    response = generate_response(user_input)
    return jsonify({'response': response})

def generate_response(user_input):
    # Implement your chatbot logic here
    # Provide answers to the 4 different queries
    if '1' in user_input.lower():
        return 'Yes, the college have a Co-op Program.'
    elif '2' in user_input.lower():
        return 'Yes, the college awards scholarships to the deserved students.'
    elif '3' in user_input.lower():
        return 'The in-state tuition for the college is $10,000 per year.'
    elif '4' in user_input.lower():
        return 'No, the college does not have a cricket team.'
    elif 'exit' in user_input.lower():
        return 'Thanks for Chatting with me, Have a nice day!'
    else:
        return 'I apologize, but I do not have information about that specific query.'

if __name__ == '__main__':
    app.run()
