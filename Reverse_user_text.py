import tkinter as tk
from tkinter import messagebox, filedialog

def reverse_character_order(text):
    """Reverse the character order of the input text."""
    return text[::-1]

def reverse_word_order(text):
    """Reverse the word order of the input text."""
    words = text.split()
    return ' '.join(reversed(words))

def save_to_file(text):
    """Save the reversed text to a file."""
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt"),
                                                              ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text)
            messagebox.showinfo("Success", "Reversed text saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

def process_text():
    """Process the input text and display the reversed results."""
    input_text = text_input.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter some text to reverse.")
        return

    reversed_characters = reverse_character_order(input_text)
    reversed_words = reverse_word_order(input_text)

    result_text.delete("1.0", tk.END)  # Clear previous results
    result_text.insert(tk.END, f"Reversed Character Order:\n{reversed_characters}\n\n")
    result_text.insert(tk.END, f"Reversed Word Order:\n{reversed_words}\n")

def create_gui():
    """Create the GUI for the text reversal application."""
    global text_input, result_text

    # Create the main window
    window = tk.Tk()
    window.title("Text Reverser")

    # Create and place the input text area
    tk.Label(window, text="Enter text to reverse:").pack(pady=5)
    text_input = tk.Text(window, height=10, width=50)
    text_input.pack(pady=5)

    # Create and place the process button
    process_button = tk.Button(window, text="Reverse Text", command=process_text)
    process_button.pack(pady=5)

    # Create and place the save button
    save_button = tk.Button(window, text="Save Reversed Text", command=lambda: save_to_file(result_text.get("1.0", tk.END)))
    save_button.pack(pady=5)

    # Create and place the result text area
    tk.Label(window, text="Reversed Results:").pack(pady=5)
    result_text = tk.Text(window, height=10, width=50)
    result_text.pack(pady=5)

    # Start the GUI event loop
    window.mainloop()

if __name__ == "__main__":
    create_gui()
