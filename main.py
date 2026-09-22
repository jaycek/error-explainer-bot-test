import ollama
import time

name  = input("Enter your name: ")
branch = input("Enter your branch: ")
print(f"Hi {name} from {branch}")
SYSTEM = '''
You explain programming error messages to a  2nd year engineering student. Reply in 3 parts. 1) What it means in plain English. 2) the likely cause. 3) how to fix it. Keep it under 120 words.

Your job is to help users understand and fix:
- Programming errors
- Error messages
- Exceptions
- Bugs
- Stack traces
- Code-related problems

If the user's question is unrelated to programming, coding,
software errors, debugging, or development, do NOT answer the question.

Instead, respond exactly with:
This question is off topic
Do not try to answer off-topic questions

'''
while True:
    # data = input("Enter something to hear echo or exit to stop: ")
    data = input("Paste the last line of error message or exit to stop: ").strip()
    if not data:
        print("Please enter an error")
    elif data.lower() == "exit":
        break
    elif data.lower() == "help":
        print("Paste the last line of error message and ask again.")

    else:
        # print(f"You said.. {data}")
        start = time.time()
        try:
            response = ollama.chat(model="gemma3:1b",messages=[
                {
                    "role":"system",
                    "content":SYSTEM
                },
                {
                    "role":"user",
                    "content":data
                    # "content":"Python error - Explain: NameError: name 'x'is not defined."
                }
            ])
            time_taken = time.time()-start
            answer = response.message.content
            
            print(answer)
            print(f" Time taken for the call: {time_taken:.2f} sec")
        except Exception as e:
            print(f"Could not reach the model: {e}")

    