from flask import Flask, render_template, request
import openai
import math
import os

app = Flask(__name__)

# Set your OpenAI API key safely as environment variable
openai.api_key = "YOUR_API_KEY_HERE"

def ask_ai(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        return response['choices'][0]['message']['content']
    except:
        return "AI Mentor is not available right now."

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    No_of_subjects = 0

    if request.method == 'POST':
        try:
            days_left = int(request.form['days_left'])
            No_of_subjects = int(request.form['No_of_subjects'])
        except:
            days_left = 1
            No_of_subjects = 1

        for i in range(1, No_of_subjects + 1):
            subject = request.form.get(f'subject_{i}')
            chapters = int(request.form.get(f'chapters_{i}', 0))
            difficulty = int(request.form.get(f'difficulty_{i}', 1))

            if subject and chapters > 0:
                chapters_per_day = math.ceil(chapters / days_left)  # Integer division
                priority = chapters * difficulty

                if priority >= 20:
                    priority_text = "HIGH PRIORITY\n!!!Start preparation today itself==You can do it!!"
                elif priority >= 10:
                    priority_text = "MEDIUM PRIORITY\n!!!You are on the right track!!!"
                else:
                    priority_text = "LOW PRIORITY\n!!!Keep going!!!"

                study_time = chapters_per_day * 1  # 1 hour per chapter

                ai_suggestion = ask_ai(
                    f"Suggest a study plan for {subject} with {chapters} chapters in {days_left} days. Include tips and motivation."
                )

                results.append({
                    'subject': subject,
                    'chapters_per_day': chapters_per_day,
                    'priority_text': priority_text,
                    'study_time': study_time,
                    'ai_suggestion': ai_suggestion
                })

    return render_template('index.html', results=results, No_of_subjects=No_of_subjects)

if __name__ == '__main__':
    app.run(debug=True)
