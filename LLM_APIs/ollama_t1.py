from ollama import chat
import tkinter as tk
from tkinter import scrolledtext
message_list = []
def send_message():
    message_list.append({
        "role": "user",
          "content":  user_input.get(),
    })
    response = chat(model="llama3.2", messages=message_list) 
    
    message_list.append({
        "role": "system",
      "content": response.message["content"],
    })
    conversation_textbox.insert(tk.END,"User: "+ user_input.get() + "\n\n")
    conversation_textbox.insert(tk.END,"Answer: "+ response.message["content"]+ "\n-----------\n")

root = tk.Tk()
root.title("Ruti Chatbot")
user_input=tk.Entry(width=50)
user_input.pack(padx = 10 , pady=5)
send_button=tk.Button(text="Send", command=send_message)
send_button.pack(pady=5)
conversation_textbox = scrolledtext.ScrolledText( width=50, wrap=tk.WORD)
conversation_textbox.pack(padx=10, pady=5)
root.mainloop()


