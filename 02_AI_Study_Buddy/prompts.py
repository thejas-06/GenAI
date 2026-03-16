# Prompt templates for AI Study Buddy

def get_flashcard_prompt(subject, difficulty, notes):
    """Generate flashcards prompt"""
    return f'''You are a helpful study assistant for a student.

Subject: {subject}
Difficulty: {difficulty}

Based on the following notes, generate 10 flashcards for exam revision.

Notes:
{notes}

Instructions:
1. Each flashcard should have a clear Question and a concise Answer.
2. Cover the most important concepts from the notes.
3. Keep answers short (1-3 sentences).
4. Format each flashcard like this:

    Flashcard 1
   Q: [question]
   A: [answer]

5. Make questions suitable for {difficulty} level students.'''


def get_mcq_prompt(subject, difficulty, notes):
    """Generate MCQ quiz prompt"""
    return f'''You are a helpful study assistant for a student.

Subject: {subject}
Difficulty: {difficulty}

Based on the following notes, generate 5 Multiple Choice Questions (MCQs).

Notes:
{notes}

Instructions:
1. Each MCQ should have 4 options (A, B, C, D).
2. Mark the correct answer clearly.
3. Add a brief explanation for the correct answer.
4. Format like this:

    Question 1: [question text]
   A) [option]
   B) [option]
   C) [option]
   D) [option]
    Answer: [correct option letter]
    Explanation: [brief explanation]

5. Make questions suitable for {difficulty} level students.'''


def get_short_answer_prompt(subject, difficulty, notes):
    """Generate short answer questions prompt"""
    return f'''You are a helpful study assistant for a student.

Subject: {subject}
Difficulty: {difficulty}

Based on the following notes, generate 5 short answer questions with answers.

Notes:
{notes}

Instructions:
1. Questions should test understanding, not just memory.
2. Answers should be 2-4 sentences long.
3. Format like this:

    Question 1: [question]
   Answer: [detailed answer in 2-4 sentences]

4. Make questions suitable for {difficulty} level students.'''


def get_summary_prompt(subject, difficulty, notes):
    """Generate revision summary prompt"""
    return f'''You are a helpful study assistant for a student.

Subject: {subject}
Difficulty: {difficulty}

Based on the following notes, create a revision summary.

Notes:
{notes}

Instructions:
1. Organize the summary with clear headings.
2. Use bullet points for key concepts.
3. Highlight important terms, definitions, and formulas.
4. Keep it concise but cover all major topics.
5. Add a "Key Points to Remember" section at the end.
6. Make it suitable for {difficulty} level students.'''


# Map mode names to prompt functions
PROMPT_MAP = {
    "Flashcards": get_flashcard_prompt,
    "MCQ Quiz": get_mcq_prompt,
    "Short Answers": get_short_answer_prompt,
    "Revision Summary": get_summary_prompt,
}
