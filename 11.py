import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import difflib
from PIL import Image, ImageTk
from datetime import datetime
import re
import webbrowser
import random
import customtkinter
from customtkinter import *
import requests
import threading
import datetime
import ntpath
import mysql.connector


now = datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H-%M-%S")
result = "result"
version = '1.0.0'
main_color = '#222222'
main_text_color = '#0e1116'
avaliable_color = 'green'
not_avaliable_color = 'red'

#address Donate
a_w_donate_Btc = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'
a_w_donate_Usdt = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'
paypal ='https://paypal.me/Zanko_legend'


#password itmes
lower = "abcdefghijklmmopqrstuwwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%^&*()_+{}|.,<>:;/"


class DomainInfoManager:
    def __init__(self, root):
        self.root = root
        self.root.title(f"ZL Tools {version}")
        self.root.geometry("1275x950+280+40")  # Set initial window size
        self.root.resizable(False,False)

        # Set window icon
        icon_path = os.path.join(os.path.dirname(__file__), '1.ico')
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)

        # Configure overall style and layout
        self.setup_styles()

        # Create main frame to hold all components
        self.main_frame = ttk.Frame(self.root, padding=(20, 20), border=3, relief='groove', style='Main.TFrame')
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create left frame for buttons on the left side
        self.left_frame = ttk.Frame(self.main_frame, width=300, style='Main.TFrame', border=10)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.frameff = ttk.Frame(self.left_frame, width=300, style='Main.TFrame', border=10)
        self.frameff.pack(fill=tk.Y,side=tk.BOTTOM)


        self.labelf = tk.Label(self.frameff, text="LOG INFORMATION ", font=("Helvetica", 16, 'bold'), justify='center',
                               fg="#d038ff", bg='#0e1116')
        self.labelf.pack(pady=5)

        self.labelff = tk.Label(self.frameff, text="Folders:", font=("Helvetica", 12, 'bold'), justify='center',
                               fg="white", bg='#0e1116')
        self.labelff.pack()
        self.labelffnum = tk.Label(self.frameff, text="0", font=("Helvetica", 12, 'bold'), justify='center',
                               fg="white", bg='#0e1116')
        self.labelffnum.pack()

        self.labelaf = tk.Label(self.frameff, text="All Files:", font=("Helvetica", 12, 'bold'), justify='center',
                               fg="white", bg='#0e1116')
        self.labelaf.pack()
        self.labelafnum = tk.Label(self.frameff, text="0", font=("Helvetica", 12, 'bold'), justify='center',
                               fg="white", bg='#0e1116')
        self.labelafnum.pack()

        self.labelc = tk.Label(self.frameff, text="Cookies:", font=("Helvetica", 12, 'bold'), justify='center',
                               fg="white", bg='#0e1116')
        self.labelc.pack()
        self.labelcnum = tk.Label(self.frameff, text="0", font=("Helvetica", 12, 'bold'), justify='center',
                               fg="white", bg='#0e1116')
        self.labelcnum.pack()

        self.labelpf = tk.Label(self.frameff, text="Foundation files:", font=("Helvetica", 12, 'bold'), justify='center',
                               fg="green", bg='#0e1116')
        self.labelpf.pack()
        self.labelpfnum = tk.Label(self.frameff, text="0", font=("Helvetica", 12, 'bold'), justify='center',
                               fg="green", bg='#0e1116')
        self.labelpfnum.pack()

        self.labelv = tk.Label(self.frameff, text="Foundation:", font=("Helvetica", 12, 'bold'), justify='center',
                               fg="green", bg='#0e1116')
        self.labelv.pack()
        self.labelvnum = tk.Label(self.frameff, text="0", font=("Helvetica", 12, 'bold'), justify='center',
                               fg="green", bg='#0e1116')
        self.labelvnum.pack()


        self.labelnv = tk.Label(self.frameff, text="Not Foundation:", font=("Helvetica", 12, 'bold'), justify='center',
                               fg="red", bg='#0e1116')
        self.labelnv.pack()
        self.labelnvnum = tk.Label(self.frameff, text="0", font=("Helvetica", 12, 'bold'), justify='center',
                               fg="red", bg='#0e1116')
        self.labelnvnum.pack()


        self.labelnl = tk.Label(self.frameff, text="_____________________", font=("Helvetica", 12, 'bold'), justify='center',
                               fg="#d038ff", bg='#0e1116')
        self.labelnl.pack()
        self.labelnl = tk.Label(self.frameff, text="Name Log:", font=("Helvetica", 12, 'bold'),fg="gray", bg='#0e1116')
        self.labelnl.pack()

        self.labelnln = tk.Label(self.frameff, text="Name", font=("Helvetica", 10, 'bold'), justify='center',fg="white", bg='#0e1116')
        self.labelnln.pack()


        self.image = Image.open('./logo.png')
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(self.left_frame, image=self.photo, border=0, relief='sunken', justify='center')
        self.label.pack(padx=10, pady=10)

        self.t_frame = ttk.Frame(self.left_frame, width=300, style='Main.TFrame', border=10)
        self.t_frame.pack(fill=tk.Y)


        self.labelt = tk.Label(self.t_frame, text="ZL Tools ", font=("Helvetica", 20, 'bold'), justify='center',
                               fg='White', bg='#0e1116')
        self.labelt.pack(padx=10, pady=10 ,side=tk.LEFT)
        self.labeltv = tk.Label(self.t_frame, text=f"{version}", font=("Helvetica", 20, 'bold'), fg='sky blue',
                                bg='#0e1116')
        self.labeltv.pack(side=tk.LEFT)

        # Create central frame for displaying content
        self.central_frame = ttk.Frame(self.main_frame, style='Main.TFrame')
        self.central_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20)
        self.buttont = ttk.Frame(self.central_frame,width=1000,height=34,style='Button.TFrame')
        self.buttont.pack(side=tk.TOP,padx=1,fill=tk.BOTH)

        self.labeltt = tk.Label(self.buttont, text=f"ZL TOOL {version} | Channal: https://t.me/ZLTOOLS ", fg="yellow", font=("Helvetica", 14, "bold"), bg='#222222')
        self.labeltt.pack(pady=10,padx=10)

        

        # style
        style = ttk.Style()
        # button style
        style.configure('My.TButton',
                        foreground='#04baf1',  # Text color
                        background='#f1f004',  # Background color
                        justify='center',
                        font=('Helvetica', 14, 'bold'),  # Font and si
                        )
        style.configure('My.TLabel',
                        foreground=avaliable_color,  # Text color
                        background='#f1f004',  # Background color
                        justify='left',
                        borderwidth='10', relief='solid',
                        font=('Helvetica', 14, 'bold'),  # Font and si
                        )

        # Create a dictionary to hold section frames
        self.section_frames = {}

        # Initialize frames for different sections
        self.create_section_frame("Cookies")
        self.create_section_frame("Logs Tools")
        self.create_section_frame("Info")
        self.create_section_frame("Proxy")
        self.create_section_frame("About")


        # Show the default section (Main)
        self.show_section_frame("Cookies")

        # Create buttons on the left side
        self.create_left_buttons()

    def setup_styles(self):
        self.root.style = ttk.Style()
        self.root.style.configure('Main.TFrame', background='#0e1116')
        self.root.style = ttk.Style()
        self.root.style.configure('Button.TFrame', background='#222222')


    def create_section_frame(self, section_name):
        frame = ttk.Frame(self.central_frame, style='Main.TFrame')
        self.section_frames[section_name] = frame

        # Customize each section frame based on section_name (if needed)
        #Cookies
        if section_name == "Cookies":

            framecook = ttk.Frame(frame)
            framecook.pack()
        


           

            central_frame = ttk.Frame(frame, style='Main.TFrame')
            central_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            url_frame = ttk.Frame(central_frame, style='Main.TFrame')
            url_frame.pack(padx=5, pady=5)
            # URL Entry
            url_label = ttk.Label(url_frame, text="Enter Your Url For Search :",
                                       font=("Helvetica", 12, 'bold'), foreground='green', background=main_text_color)
            url_label.pack(side=tk.LEFT, padx=10, pady=10)

            url_entry = tk.Entry(url_frame, width=35, font=("Vertical", 12, "bold"))
            url_entry.pack(side=tk.LEFT)

            search_button = RoundedButtons(url_frame, text="START PATH LOG")
            search_button.pack(side=tk.LEFT, padx=10)
            # Result Display (Scrollable Text Area)
            result_text = scrolledtext.ScrolledText(central_frame, width=60, height=20,
                                                         font=("Helvetica", 16, "bold"), wrap="word", fg="green",
                                                         bg='#222222')
            result_text.pack(pady=10)    
            #LOGS TOOLS frame
        elif section_name == "Logs Tools":
                def start():
                    input_urls = [url.strip() for url in url_entry.get().split(",") if url.strip()]

                    if not input_urls:
                        messagebox.showwarning("Input URLs Missing", "Please enter one or more URLs.")
                        return

                    # Get domain info from selected folder
                    folder_path = browse_for_folder()
                    if folder_path:
                        domain_info = extract_domain_info(folder_path)
                        matching_entries = find_matching_urls(domain_info, input_urls)
                        save_results_to_file(matching_entries)
                        display_results(matching_entries)
                        count_folders_files(folder_path)
                        show_selected_folder(folder_path)
                        count_password_files(folder_path)
                        liner()

                def browse_for_folder():
                    folder_path = filedialog.askdirectory(title="Select logs folder")
                    return folder_path

                def extract_domain_info(folder_path):
                    domain_info = []

                    try:
                        for root, _, filenames in os.walk(folder_path):
                            for filename in filenames:
                                if filename.lower() == 'passwords.txt':  # Adjust based on your file naming convention
                                    file_path = os.path.join(root, filename)
                                    with open(file_path, 'r', encoding='utf-8') as file:
                                        current_entry = {}
                                        for line in file:
                                            line = line.strip()
                                            if line.startswith("URL:"):
                                                current_entry["URL"] = line.split("URL:")[1].strip()
                                            elif line.startswith("Username:"):
                                                current_entry["Username"] = line.split("Username:")[1].strip()
                                            elif line.startswith("Password:"):
                                                current_entry["Password"] = line.split("Password:")[1].strip()
                                            elif line.startswith("==="):
                                                if current_entry:
                                                    domain_info.append(current_entry)
                                                    current_entry = {}
                                        if current_entry:  # Ensure the last entry is added
                                            domain_info.append(current_entry)
                    except Exception as e:
                        messagebox.showerror("Error", f"An error occurred while extracting domain info: {e}")

                    return domain_info

                def find_matching_urls(domain_info, input_urls):
                    matching_entries = {url: [] for url in input_urls}

                    for entry in domain_info:
                        url = entry.get('URL')
                        if not url:
                            continue  # Skip entries without a URL

                        for input_url in input_urls:
                            if url == input_url:
                                matching_entries[input_url].append(entry)
                            else:
                                similarity_ratio = difflib.SequenceMatcher(None, url, input_url).ratio()
                                if similarity_ratio > 0.5:
                                    matching_entries[input_url].append(entry)

                    return matching_entries

                def save_results_to_file(results_dict):
                    folder_name = f"results Search BY ZLTools {version}"
                    try:
                        if not os.path.exists(folder_name):
                            os.makedirs(folder_name)

                        input_urls = [url.strip() for url in url_entry.get().split(",") if url.strip()]

                        for url in input_urls:
                            cleaned_url = re.sub(r'[<>:\/\\|?*]', '', url)
                            url_folder_name = os.path.join(folder_name, f"{cleaned_url} {formatted_date}")

                            if not os.path.exists(url_folder_name):
                                os.makedirs(url_folder_name)

                            file_name = f"{cleaned_url}.txt"
                            file_path = os.path.join(url_folder_name, file_name)

                            with open(file_path, 'w') as file:
                                file.write("SEARCH BY ZL Tools\n")
                                file.write(f"{formatted_date}\n")
                                file.write("=" * 30 + "\n")
                                file.write(f"Results for URL: {url}\n")
                                file.write("=" * 30 + "\n")

                                if url in results_dict:
                                    entries = results_dict[url]
                                    if entries:
                                        for entry in entries:
                                            username = entry.get('Login', 'N/A')
                                            username = entry.get('Username', 'N/A')
                                            password = entry.get('Password', 'N/A')
                                            file.write(f"{username}:{password}\n")
                                    else:
                                        file.write("No matching entries found.\n")
                                else:
                                    file.write("No matching entries found.\n")

                            urlsaver(results_dict, url, url_folder_name)

                            messagebox.showinfo("Results Saved", f"Results for URL {url} have been saved to '{file_path}'.")

                    except Exception as e:
                        messagebox.showerror("Error", f"An error occurred while saving results: {e}")

                def urlsaver(results_dict, url, folder_path):
                    try:
                        cleaned_url = re.sub(r'[<>:\/\\|?*]', '', url)
                        file_name = f"url-user_pass_{cleaned_url}.txt"
                        file_path = os.path.join(folder_path, file_name)

                        with open(file_path, 'w') as file:
                            file.write("BY ZL Tools\n")
                            file.write(f"{formatted_date}\n")
                            file.write(f"Results for URL: {url}\n")
                            file.write("=" * 30 + "\n")

                            if url in results_dict:
                                entries = results_dict[url]
                                if entries:
                                    for entry in entries:
                                        entry_url = entry.get('URL', 'N/A')
                                        username = entry.get('Username', 'N/A')
                                        password = entry.get('Password', 'N/A')
                                        file.write(f"{entry_url}/{username}:{password}\n")
                                else:
                                    file.write("No matching entries found.\n")
                            else:
                                file.write("No matching entries found.\n")

                    except Exception as e:
                        messagebox.showerror("Error", f"An error occurred while saving results: {e}")

                def display_results(results_dict):
                    result_text.delete(1.0, tk.END)
                    for url, entries in results_dict.items():
                        result_text.insert(tk.END, f"Results for URL: {url}\n")
                        result_text.insert(tk.END, "*" * 30 + "\n")
                        if entries:
                            for entry in entries:
                                username = entry.get('Username', 'N/A')
                                password = entry.get('Password', 'N/A')
                                result_text.insert(tk.END, f"{username}:{password}\n")
                        else:
                            result_text.insert(tk.END, "No matching entries found.\n")
                        result_text.insert(tk.END, "\n")

                def update_url_entry():
                    # Get selected texts from checkboxes
                    selected_texts = [text for text, var in checkbox_vars.items() if var.get()]
                    # Update entry field
                    if selected_texts:
                        url_entry.delete(0, tk.END)
                        url_entry.insert(0, ','.join(selected_texts))
                    else:
                        url_entry.delete(0, tk.END)

                def show_selected_folder(folder_path):
                    # Extract the last directory name from the folder path
                    folder_name = ntpath.basename(folder_path)
                    self.labelnln.config(text=f"{folder_name}")

                def count_password_files(folder_path):
                    password_file_count = sum(1 for _, _, files in os.walk(folder_path) if 'Passwords.txt' in files)
                    self.labelpfnum.config(text=f"{password_file_count}")
                  
            
                def count_folders_files(folder_path):
                    folder_count = sum(1 for _, dirs, _ in os.walk(folder_path))
                    file_count = sum(len(files) for _, _, files in os.walk(folder_path))
                    self.labelafnum.config(text=f"{folder_count}")
                    self.labelffnum.config(text=f"{file_count}")

                def liner():
                    text_content = result_text.get("1.0", "end-1c") 
                                    # Count the number of lines
                    lines = text_content.count('\n') + 1

                    # Display the line count
                    self.labelvnum .config(text=f"{lines}")
        





                central_frame = ttk.Frame(frame, style='Main.TFrame')
                central_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                url_frame = ttk.Frame(central_frame)
                url_frame.pack(padx=5, pady=20)

                url_label = ttk.Label(url_frame, text="Enter Your URL For Search:",
                                      font=("Helvetica", 12, 'bold'), foreground='green')
                url_label.pack(side=tk.LEFT, padx=10, pady=10)

                url_entry = tk.Entry(url_frame, width=35, font=("Helvetica", 12, "bold"))
                url_entry.pack(side=tk.LEFT)

                search_button = RoundedButtons(url_frame, text="START PATH LOG", command=start)
                search_button.pack(side=tk.LEFT, padx=10)

                frameop = ttk.Frame(central_frame)
                frameop.pack()

                # Dictionary to store checkbutton variables and their corresponding texts
                checkbox_vars = {
                    "facebook.com": tk.BooleanVar(),
                    "tiktok.com": tk.BooleanVar(),
                    "midasbuy.com": tk.BooleanVar(),
                    "amazon.com": tk.BooleanVar(),
                    "express.com": tk.BooleanVar(),
                    "netflix.com": tk.BooleanVar(),
                    "store.steampowered.com": tk.BooleanVar(),
                }

                # Create and pack checkbuttons
                for text, var in checkbox_vars.items():
                    checkbox = ttk.Checkbutton(frameop, text=text, variable=var, command=update_url_entry)
                    checkbox.pack(side=tk.LEFT, padx=5)

                result_text = scrolledtext.ScrolledText(central_frame, width=65, height=17,
                                                        font=("Helvetica", 16, "bold"), wrap="word", fg="green", bg="white")
                result_text.pack(pady=10, side=tk.BOTTOM)

        #info section
        elif section_name == "Info":

            
            # Create the Notebook widget
            notebook = ttk.Notebook(frame,style='Main.TFrame')

            # Create frames for each tab
            tab1 = ttk.Frame(notebook,style='Main.TFrame')
            tab2 = ttk.Frame(notebook,style='Main.TFrame')
            tab3 = ttk.Frame(notebook,style='Main.TFrame')
            tab4 = ttk.Frame(notebook,style='Main.TFrame')

            # Add frames to notebook
            notebook.add(tab1, text="Credit Card")
            notebook.add(tab2, text="Discord Tokens")
            notebook.add(tab3, text="Wallet Adress")
            notebook.add(tab4, text="Coming soon")

            # Pack the notebook widget
            notebook.pack(expand=1, fill="both",padx=20,pady=15)

            tab1frame = ttk.Frame(tab1,style='Main.TFrame')
            tab1frame.pack()
            # Function to extract credit card info
            def extract_credit_card_info(folder_path):
                credit_card_info = []
                try:
                    for root, _, filenames in os.walk(folder_path):
                        for filename in filenames:
                            if filename.lower().endswith('microsoft_[edge]_default.txt'):  # Adjust based on your file naming convention
                                file_path = os.path.join(root, filename)
                                show_selected_folder(folder_path)
                                with open(file_path, 'r', encoding='utf-8') as file:
                                    current_entry = {}
                                    for line in file:
                                        line = line.strip()
                                        if line.startswith("Holder:"):
                                            current_entry["Holder"] = line.split("Holder:")[1].strip()
                                        elif line.startswith("CardType:"):
                                            current_entry["CardType"] = line.split("CardType:")[1].strip()
                                        elif line.startswith("Card:"):
                                            current_entry["Card"] = line.split("Card:")[1].strip()
                                        elif line.startswith("Expire:"):
                                            current_entry["Expire"] = line.split("Expire:")[1].strip()
                                            count_folders_files(folder_path)
                                            count_cc_files(folder_path)
                                        elif line.startswith("==="):
                                            if current_entry:
                                                credit_card_info.append(current_entry)
                                                current_entry = {}
                                    if current_entry:  # Ensure the last entry is added
                                        credit_card_info.append(current_entry)
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred while extracting credit card info: {e}")
                return credit_card_info

            # Function to browse folder
            def browse_folder_cc():
                folder_path = filedialog.askdirectory()
                if folder_path:
                    folder_path_entry_cc.delete(0, tk.END)
                    folder_path_entry_cc.insert(0, folder_path)

            # Function to extract info
            def extract_info_cc():
                folder_path = folder_path_entry_cc.get()
                if not folder_path:
                    messagebox.showwarning("Warning", "Please select a folder.")
                    return
                
                credit_card_info = extract_credit_card_info(folder_path)
                if credit_card_info:
                    result_text_cc.delete(1.0, tk.END)
                    for info in credit_card_info:
                        result_text_cc.insert(tk.END, "CardType: {} | ".format(info.get("CardType", "")))
                        result_text_cc.insert(tk.END, "Holder: {} | ".format(info.get("Holder", "")))
                        result_text_cc.insert(tk.END, "Card: {} | ".format(info.get("Card", "")))
                        result_text_cc.insert(tk.END, "Expire: {}\n".format(info.get("Expire", "")))
                        result_text_cc.insert(tk.END, "-" * 60 + "\n")
                    count_cc()
                  


            def count_cc():
                # Get the text content from the text box
                text_content = result_text_cc.get("1.0", "end-1c")  # Retrieve all text excluding the trailing newline
                text_c = "-" * 60

                # Count the number of lines
                lines = text_content.count(text_c) + 1  # Count newlines to determine lines

                # Display the line count
                self.labelvnum.config(text=f"{lines}")
                return



            def count_cc_files(folder_path):
                Token_file_count = sum(1 for _, _, files in os.walk(folder_path) if '.txt' in files)
                self.labelpfnum.config(text=f"{Token_file_count}")

            def count_folders_files(folder_path):
                folder_count = sum(1 for _, dirs, _ in os.walk(folder_path))
                file_count = sum(len(files) for _, _, files in os.walk(folder_path))
                self.labelafnum.config(text=f"{folder_count}")
                self.labelffnum.config(text=f"{file_count}")

            def show_selected_folder(folder_path):
                # Extract the last directory name from the folder path
                folder_name = ntpath.basename(folder_path)
                self.labelnln.config(text=f"{folder_name}")


            # Create main frame
            main_frame = ttk.Frame(tab1frame, style='Main.TFrame')
            main_frame.pack(pady=20, padx=20)

            # Create central frame
            frame_cen = ttk.Frame(main_frame, style='Main.TFrame')
            frame_cen.pack(pady=20)

            frame_be = ttk.Frame(frame_cen, style='Main.TFrame')
            frame_be.pack(pady=20)

            # Input frame
            frame_input = ttk.Frame(frame_be, style='Main.TFrame')
            frame_input.pack(pady=20)

            folder_label = tk.Label(frame_input, text="Enter Your Local log:", font=("Helvetica", 14, 'bold'), foreground='red', background='#0e1116')
            folder_label.pack(padx=5, pady=5, side=tk.LEFT)

            folder_path_entry_cc = tk.Entry(frame_input, width=50, font=("Helvetica", 12, 'bold'))
            folder_path_entry_cc.pack(padx=5, pady=5, side=tk.LEFT)

            # Button frame
            frame_but = ttk.Frame(frame_be, style='Main.TFrame')
            frame_but.pack(pady=20, padx=5,side=tk.LEFT)

            browse_button = tk.Button(frame_but, text="Select Folder", width=30,height=2, font=("Helvetica", 12, 'bold'), command=browse_folder_cc)
            browse_button.pack(padx=8, pady=5, side=tk.LEFT)

            extract_button = tk.Button(frame_but, text="Extract Info",width=30, height=2, font=("Helvetica", 12, 'bold'), command=extract_info_cc)
            extract_button.pack(padx=13, pady=5, side=tk.LEFT)

            # Result text
            result_text_cc= tk.Text(main_frame, height=20, width=80, font=("Helvetica", 14, "bold"), wrap="word", fg="green", bg="white")
            result_text_cc.pack(padx=5, pady=5, side=tk.BOTTOM)



            tab2frame = ttk.Frame(tab2,style='Main.TFrame')
            tab2frame.pack(pady=20, padx=20, side=tk.TOP)

  
            # Function to find text files in "Discord" folder
            def find_discord_files(folder_path):
                discord_files = []
                try:
                    for root, dirs, filenames in os.walk(folder_path):
                        if 'discord' in [d.lower() for d in dirs]:
                            discord_folder = os.path.join(root, 'Discord')
                            show_selected_folder_discord(discord_folder)  # Corrected here
                            for filename in os.listdir(discord_folder):
                                if filename.lower().endswith('.txt'):
                                    discord_files.append(os.path.join(discord_folder, filename))
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred while finding Discord files: {e}")
                return discord_files

            def extract_discord_tokens(folder_path):
                tokens = []
                try:
                    discord_files = find_discord_files(folder_path)
                    for file_path in discord_files:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            for line in file:
                                token = line.strip()
                                if token:
                                    tokens.append(token)
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred while extracting tokens: {e}")
                return tokens

            def browse_folder():
                folder_path = filedialog.askdirectory()
                if folder_path:
                    folder_path_entry_discord.delete(0, tk.END)
                    folder_path_entry_discord.insert(0, folder_path)

            def extract_and_display_info():
                folder_path = folder_path_entry_discord.get()
                if not folder_path:
                    messagebox.showwarning("Warning", "Please select a folder.")
                    return
                tokens = extract_discord_tokens(folder_path)
                if tokens:
                    result_text_discord.delete(1.0, tk.END)
                    for token in tokens:
                        result_text_discord.insert(tk.END, f"Token: {token}\n")
                        result_text_discord.insert(tk.END, "-" * 80 + "\n")
                    count_tokens()
                    count_tokens_files(folder_path)
                    count_folders_files(folder_path)

            def count_tokens():
                text_content = result_text_discord.get("1.0", "end-1c")  # Get all text from result_text_discord
                token_count = len(text_content.split('Token')) 
                self.labelvnum.config(text=f"{lines}")

            def count_tokens_files(folder_path):
                Token_file_count = sum(1 for _, _, files in os.walk(folder_path) if 'Tokens.txt' in files)
                self.labelpfnum.config(text=f"{Token_file_count}")

            def show_selected_folder_discord(folder_path):
                folder_name = ntpath.basename(folder_path)
                self.labelnln.config(text=f"{folder_name}")

            def count_folders_files(folder_path):
                folder_count = sum(1 for _, dirs, _ in os.walk(folder_path))
                file_count = sum(len(files) for _, _, files in os.walk(folder_path))
                self.labelafnum.config(text=f"{folder_count}")
                self.labelffnum.config(text=f"{file_count}")


           
            framebe = ttk.Frame(tab2frame, style='Main.TFrame')
            framebe.pack(pady=40, padx=20, side=tk.TOP)
                
            input_frame = ttk.Frame(framebe, style='Main.TFrame')
            input_frame.pack(pady=20, side=tk.TOP)

            folder_label = tk.Label(input_frame, text='Enter Your Local log:', font=("Helvetica", 14, 'bold'), foreground='red', background='#0e1116')
            folder_label.pack(padx=5, pady=5, side=tk.LEFT)

            folder_path_entry_discord = tk.Entry(input_frame, width=50, font=("Helvetica", 12, 'bold'))
            folder_path_entry_discord.pack(padx=5, pady=5, side=tk.LEFT)

            button_frame = ttk.Frame(framebe, style='Main.TFrame')
            button_frame.pack(pady=20,padx=5,side=tk.TOP)

            browse_button = tk.Button(button_frame, text="Select Folder", height=2, width=30,font=("Helvetica", 12, 'bold'), command=browse_folder)
            browse_button.pack(padx=8, pady=5, side=tk.LEFT)

            extract_button = tk.Button(button_frame, text="Extract Info", height=2, width=30,  font=("Helvetica", 12, 'bold'), command=extract_and_display_info)
            extract_button.pack(padx=13, pady=5, side=tk.LEFT)

            
            result_text_discord = tk.Text(tab2frame, height=20, width=80, font=("Helvetica", 14, "bold"), wrap="word", fg="green", bg="white")
            result_text_discord.pack(padx=5, pady=5, side=tk.BOTTOM)   





            tab3frame = ttk.Frame(tab3,)
            tab3frame.pack()







            
        #Proxy
        elif section_name == "Proxy":

           
             # Global variable to track the proxy checking thread
            proxy_check_thread = None

            def check_proxy(proxy):
                try:
                    response = requests.get("https://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=5)
                    if response.status_code == 200:
                        return True
                    else:
                        return False
                except Exception as e:
                    return False

            def start_proxy_check():
                global proxy_check_thread
                api_url = api_entry.get().strip()
                file_path = file_entry.get().strip()

                proxies = []

                if api_url:
                    proxies.extend(fetch_proxies_from_api(api_url))
                
                if file_path:
                    proxies.extend(fetch_proxies_from_file(file_path))
                
                if proxies:
                    # Start a new thread to check proxies
                    proxy_check_thread = threading.Thread(target=check_proxies_and_display, args=(proxies,))
                    proxy_check_thread.start()
                    

            def stop_proxy_check():
                global proxy_check_thread
                if proxy_check_thread and proxy_check_thread.is_alive():
                    proxy_check_thread.join()  # Wait for the thread to finish
                    messagebox.showinfo("Proxy Checker", "Proxy checking process stopped.")

            def check_proxies_and_display(proxy_list):
                good_proxies = []
                for proxy in proxy_list:
                    if check_proxy(proxy):
                        good_proxies.append(proxy)
                        count_lines_Good()
                        result_textbox.insert(tk.END, f"{proxy}\n")
                        
                    else:
                        resultb_textbox.insert(tk.END, f"{proxy}\n")
                        count_lines_Bad()
                    resultb_textbox.see(tk.END)  # Scroll to the end of the textbox
                    

                    
                if not good_proxies:
                    result_textbox.insert(tk.END, "No 'GOOD' proxies found.\n")

            def fetch_proxies_from_api(api_url):
                try:
                    proxies = requests.get(api_url).text.split()
                    return proxies
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to fetch proxies from API: {e}")
                    return []

            def fetch_proxies_from_file(file_path):
                try:
                    with open(file_path, 'r') as file:
                        proxies = [line.strip() for line in file if line.strip()]
                    return proxies
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to read proxies from file: {e}")
                    return []
            def browse_file():
                file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
                if file_path:
                    file_entry.delete(0, tk.END)
                    file_entry.insert(tk.END, file_path)
                    # Call load_file_contents with the file path
                    load_file_contents(file_path, None)  # Pass None for api_url since it's not needed

            def browse_api():
                api_url = filedialog.askstring("API URL", "Enter API URL:")
                if api_url:
                    api_entry.delete(0, tk.END)
                    api_entry.insert(tk.END, api_url)
                    # Call load_file_contents with None for file_path since it's not needed
                    load_file_contents(None, api_url)

            def load_file_contents(file_path, api_url):
                if file_path:
                    try:
                        # Open the selected file in read mode
                        with open(file_path, 'r') as file:
                            # Read the contents of the file
                            file_contents = file.read()
                            # Update the textbox with the file contents
                            show_textbox.delete('1.0', tk.END)  # Clear existing text
                            show_textbox.insert(tk.END, file_contents)  # Insert new text
                    except Exception as e:
                        # Display error message if file cannot be opened
                        show_textbox.delete('1.0', tk.END)
                        show_textbox.insert(tk.END, f"Error: {str(e)}")
                elif api_url:
                    try:
                        # Make a GET request to the API
                        response = requests.get(api_url)
                        if response.status_code == 200:
                            api_data = response.text
                            show_textbox.delete('1.0', tk.END)
                            show_textbox.insert(tk.END, api_data)
                        else:
                            show_textbox.delete('1.0', tk.END)
                            show_textbox.insert(tk.END, f"API Error: {response.status_code}")
                    except Exception as e:
                        show_textbox.delete('1.0', tk.END)
                        show_textbox.insert(tk.END, f"API Error: {str(e)}")

            def count_lines_Bad():
                # Get the text content from the text box
                text_content = resultb_textbox.get("1.0", "end-1c")  # Retrieve all text excluding the trailing newline
                
                # Count the number of lines
                lines = text_content.count('\n') + 1  # Count newlines to determine lines

                # Display the line count
                textc0.config(text=f" {lines} ")
                return



            def count_lines_Good():
                # Get the text content from the text box
                text_content = result_textbox.get("1.0", "end-1c")  # Retrieve all text excluding the trailing newline
                
                # Count the number of lines
                lines = text_content.count('\n') + 1  # Count newlines to determine lines

                # Display the line count
                texth0.config(text=f" {lines} ")
                return

            def count_lines_tproxy():
                # Get the text content from the text box
                text_content = show_textbox.get("1.0", "end-1c")  # Retrieve all text excluding the trailing newline
                
                # Count the number of lines
                lines = text_content.count('\n') + 1  # Count newlines to determine lines

                # Display the line count
                textt0.config(text=f" {lines} ")

            def browsefile():
                browse_file()
                count_lines_tproxy()

            def browseapi():
                browse_api()
                count_lines_tproxy()


            def browse():
                root = tk.Tk()
                root.title('Browse Proxy')
                root.geometry("470x300+600+300")
                root.resizable(False,False)
                tabview = ttk.Notebook(root)
                tab1 = tk.Frame(tabview)

                tab2 = tk.Frame(tabview)
                tab3 = tk.Frame(tabview)

                tabview.add(tab1, text='File')
                tabview.add(tab2, text='Api')
                tabview.add(tab3, text='Paste')
                tabview.pack(expand=1, fill='both')

                frame_input = tk.Frame(tab1)
                frame_input.pack(pady=10)

                label_api = tk.Label(tab2, text="API URL:")
                label_api.grid(row=0, column=0, padx=10, pady=5, sticky="e")
                global api_entry  # Make api_entry and file_entry global
                api_entry = tk.Entry(tab2, width=40)
                api_entry.grid(row=0, column=1, padx=10, pady=5)

                label_file = tk.Label(frame_input, text="Proxy File (txt):")
                label_file.grid(row=1, column=0, padx=10, pady=5, sticky="e")
                global file_entry
                file_entry = tk.Entry(frame_input, width=40)
                file_entry.grid(row=1, column=1, padx=10, pady=5)

                load_button = tk.Button(frame_input, text="Browse File", command=browsefile)
                load_button.grid(row=1, column=2, padx=10, pady=5)
                

                button_browse_api = tk.Button(tab2, text="Browse API", command=browseapi)
                button_browse_api.grid(row=0, column=2, padx=10, pady=5)

                # Centering the root window on the screen
                window_width = 400
                window_height = 200
                

                root.mainloop()


            def startpch():
                start_proxy_check()

                


            # Example content for Cookies Checker section
            label = ttk.Label(frame, text="Welcom Proxy Checker", font=("Helvetica", 20, 'bold'), foreground='white', background='#0e1116')
            label.pack(pady=9)

            frame1  = tk.Frame(frame,background='#0e1116')
            frame1.pack(pady=9)



            frame_show =tk.Frame(frame1,background='#0e1116')
            frame_show.pack(pady=0,side=tk.LEFT)

            show_textbox = tk.Text(frame_show, width=40, height=15,font=("Helvetica", 12))
            show_textbox.pack(pady=9,padx=100)



            frame_button = tk.Frame(frame1, background='#0e1116')
            frame_button.pack(padx=40,pady=9,side=tk.RIGHT)

            button_browse_api = tk.Button(frame_button, text="Browse proxy", font=("Helvetica", 12, 'bold'),height=2, command=browse)
            button_browse_api.pack(pady=17,padx=20)

            button_start = tk.Button(frame_button, text="Start Proxy Check", font=("Helvetica", 12, 'bold'),height=2, command=start_proxy_check)
            button_start.pack(pady=17,padx=20)


            button_stop = tk.Button(frame_button, text="Stop Proxy Check", font=("Helvetica", 12, 'bold'),height=2, command=stop_proxy_check)
            button_stop.pack(pady=17,padx=20)



            frame2  = tk.Frame(frame,background='#0e1116')
            frame2.pack(pady=9)

            framerh  = tk.Frame(frame2,background='#0e1116')
            framerh.pack(padx=10,pady=9,side=tk.LEFT)

            labeltit = ttk.Label(framerh, text="GOODS:", font=("Helvetica", 14, 'bold'), foreground='Green', background='#0e1116')
            labeltit.pack()

            result_textbox = tk.Text(framerh, width=45, height=13,foreground="green",font=("Helvetica", 10),background='#222222')
            result_textbox.pack(padx=40)



            framerb  = tk.Frame(frame2,background='#0e1116')
            framerb.pack(padx=10,pady=9,side=tk.RIGHT)


            labeltit = ttk.Label(framerb, text="BADS:", font=("Helvetica", 14, 'bold'), foreground='Red', background='#0e1116')
            labeltit.pack()

            resultb_textbox = tk.Text(framerb, width=45, height=13,foreground="red",font=("Helvetica", 10),background='#222222')
            resultb_textbox.pack(padx=30)




            # cookies
            result_frame4 = ttk.Frame(frame, style='Main.TFrame', borderwidth=2, relief="groove")
            result_frame4.pack(padx=30,pady=10,side=tk.BOTTOM)
            textTotal = ttk.Label(result_frame4, text="Total Proxy :",
                                  font=("Helvetica", 12, "bold"), foreground="Sky blue",
                                  background=main_text_color)
            textTotal.pack(pady=10, side=tk.LEFT, padx=7)
            textt0 = ttk.Label(result_frame4, text=" 0 ", font=("Helvetica", 12, 'bold'), foreground="sky blue",
                               background=main_text_color)
            textt0.pack(pady=10, side=tk.LEFT, padx=7)

            textHITS = ttk.Label(result_frame4, text="Proxy Work:", font=("Helvetica", 12, "bold"),
                                 foreground="green", background=main_text_color)
            textHITS.pack(pady=10, side=tk.LEFT, padx=7)
            texth0 = ttk.Label(result_frame4, text=" 0 ", font=("Helvetica", 12, 'bold'), foreground="green",
                               background=main_text_color)
            texth0.pack(pady=10, side=tk.LEFT, padx=7)

            textBADS = ttk.Label(result_frame4, text="Proxy Custom : ", font=("Helvetica", 12, "bold"),
                                 foreground="orange", background=main_text_color)
            textBADS.pack(pady=10, side=tk.LEFT, padx=7)
            textb0 = ttk.Label(result_frame4, text=" 0 ", font=("Helvetica", 12, "bold"), foreground="orange",
                               background=main_text_color)
            textb0.pack(pady=10, side=tk.LEFT, padx=7)

            textCUSTOM = ttk.Label(result_frame4, text="Proxy Not Work : ", font=("Helvetica", 12, "bold"),
                                   foreground="Red", background=main_text_color)
            textCUSTOM.pack(pady=10, side=tk.LEFT, padx=7)
            textc0 = ttk.Label(result_frame4, text=" 0 ", font=("Helvetica", 12, "bold"), foreground="red",
                               background=main_text_color)
            textc0.pack(pady=10, side=tk.LEFT, padx=7)

            result_frame4 = ttk.Frame(frame, style='Main.TFrame', borderwidth=2, relief="groove")
            result_frame4.pack(pady=10,side=tk.BOTTOM)
            textTotal = ttk.Label(result_frame4, text="Https : ",
                                  font=("Helvetica", 12, "bold"), foreground="White",
                                  background=main_text_color)
            textTotal.pack(pady=10, side=tk.LEFT, padx=7)
            texths0 = ttk.Label(result_frame4, text=" 0 ", font=("Helvetica", 12, 'bold'), foreground="White",
                               background=main_text_color)
            texths0.pack(pady=10, side=tk.LEFT, padx=7)

            textHITS = ttk.Label(result_frame4, text="Http : ", font=("Helvetica", 12, "bold"),
                                 foreground="white", background=main_text_color)
            textHITS.pack(pady=10, side=tk.LEFT, padx=7)
            texthh0 = ttk.Label(result_frame4, text=" 0 ", font=("Helvetica", 12, 'bold'), foreground="white",
                               background=main_text_color)
            texthh0.pack(pady=10, side=tk.LEFT, padx=7)

            textBADS = ttk.Label(result_frame4, text="Socks5:", font=("Helvetica", 12, "bold"),
                                 foreground="white", background=main_text_color)
            textBADS.pack(pady=10, side=tk.LEFT, padx=7)
            textb0 = ttk.Label(result_frame4, text=" 0 ", font=("Helvetica", 12, "bold"), foreground="white",
                               background=main_text_color)
            textb0.pack(pady=10, side=tk.LEFT, padx=7)

            texts4 = ttk.Label(result_frame4, text="Socks4:", font=("Helvetica", 12, "bold"),
                                   foreground="white", background=main_text_color)
            texts4.pack(pady=10, side=tk.LEFT, padx=7)
            texts40 = ttk.Label(result_frame4, text=" 0 ", font=("Helvetica", 12, "bold"), foreground="white",
                               background=main_text_color)
            texts40.pack(pady=10, side=tk.LEFT, padx=7)

        
        
  



        elif section_name == "About":

            def facebook_link():
                webbrowser.open("https://www.facebook.com/Zank0.H.Aziz?mibextid=LQQJ4d")

            def instagram_link():
                webbrowser.open("https://www.instagram.com/zanolegend?igsh=MXVybWQ1MXQ3MHd5cQ%3D%3D&utm_source=qr")

            def youtube_link():
                webbrowser.open("https://youtube.com/@zanolegend")

            def telegram_link():
                webbrowser.open("https://t.me/ZANKO_LEGEND")

            def channal_link():
                webbrowser.open("https://t.me/ZLTools")

            label = ttk.Label(frame, text="About Me", font=("Helvetica", 20, 'bold'), foreground='white',
                              background='#0e1116')
            label.pack(pady=30)

            labela = ttk.Label(frame, text="Hello Guys .My Nmae is Zanko Hatam . i'm From Kurdistan in Iraq . i'm 17 Years old.And I'm Muslim\nMy Nikname is Zanko LEGEND. I'm Create ZL Tools By Myself Alone .\ni'm Create This Tools For To Test My Abilities . Thanks Useing My Tool.\nEnjoy Using My Tool ", font=("Helvetica", 14, 'bold'), foreground='Green',justify='center',
                              background='#0e1116')
            labela.pack(pady=30)

            labelb = ttk.Label(frame, text=f"For Donate Me", font=("Helvetica", 16, 'bold'), foreground='white',
                              background='#0e1116')
            labelb.pack(pady=20)
            labelb = ttk.Label(frame, text=f"Bitcon: {a_w_donate_Btc}\n\nUsdt: {a_w_donate_Usdt}\n\n Paypal: {paypal}",
                               font=("Helvetica", 16, 'bold'), foreground='Gold',
                               background='#0e1116')
            labelb.pack()

            labelb = ttk.Label(frame, text=f"For Contact And Problem And Totrial  :",
                               font=("Helvetica", 16, 'bold'), foreground='sky blue',
                               background='#0e1116')
            labelb.pack(pady=20)

            framebtncon = ttk.Frame(frame, style="Main.TFrame",)
            framebtncon.pack(pady=10, padx=7)

            button = ttk.Button(framebtncon, text="Facebook", style='My.TButton', command=facebook_link)
            button.pack(pady=10,side=tk.LEFT,padx=7)

            button = ttk.Button(framebtncon, text="Instagram", style='My.TButton', command=instagram_link)
            button.pack(pady=10, side=tk.LEFT,padx=7)

            button = ttk.Button(framebtncon, text="Youtube", style='My.TButton', command=youtube_link)
            button.pack(pady=10, side=tk.LEFT, padx=7)

            button = ttk.Button(framebtncon, text="Telegram Me", style='My.TButton',command=telegram_link)
            button.pack(pady=10, side=tk.LEFT,padx=7)

            button = ttk.Button(framebtncon, text="Channal", style='My.TButton',command=channal_link)
            button.pack(pady=10, side=tk.LEFT,padx=7)

    # Add more sections as needed...
    def show_section_frame(self, section_name):
        # Hide all section frames
        for frame in self.section_frames.values():
            frame.pack_forget()

        # Show the selected section frame
        self.section_frames[section_name].pack(fill=tk.BOTH, expand=True)

    def create_left_buttons(self):
        left_button_names = ["Cookies", "Logs Tools","Info","Proxy", "About" ]
        for name in left_button_names:
            button = RoundedButton(self.left_frame, text=name, width=160, height=30, bg='green', hover_color='gray', command=lambda n=name: self.show_section_frame(n))
            button.pack(padx=10, pady=10)

    def button_click(self, button_name):
        if button_name == "Main":
            print("main button clicked")
        elif button_name == "Cookies Checker":
            print("Cookies Checker")
        elif button_name == "Proxy":
            print("Proxy")
        elif button_name == "Sitting":
            print("Sitting")
        elif button_name == "START PATH LOG":
            self.root.search()
        elif button_name == "ZL Tools":
            print("ZL Tools")
        elif button_name == "Contact":
            print("Contact")
        elif button_name == "About":
            print("About")
        else:
            # Display content based on the button clicked
            self.display_content(f"Content for {button_name}")

    
class RoundedButton(tk.Canvas):
    def __init__(self, master=None, text="", width=200, height=40, corner_radius=20, bg='lightgray', hover_color='#0e1116', command=None):
        super().__init__(master, width=width, height=height, highlightthickness=0)
        self.corner_radius = corner_radius
        self.default_color = bg
        self.hover_color = hover_color
        self.command = command

        self.create_rounded_rectangle()
        self.create_text(width//2, height//2, text=text, font=('Helvetica', 12,'bold'), fill='white')

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", lambda event: self.invoke())

    def create_rounded_rectangle(self):
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()

        self.create_rectangle(0, 0, width, height, fill=self.default_color, outline='', width=0)
        self.create_arc(0, 0, self.corner_radius*2, self.corner_radius*2, start=90, extent=90, fill=self.default_color, outline='')
        self.create_arc(width - self.corner_radius*2, 0, width, self.corner_radius*2, start=0, extent=90, fill=self.default_color, outline='')
        self.create_arc(0, height - self.corner_radius*2, self.corner_radius*2, height, start=180, extent=90, fill=self.default_color, outline='')
        self.create_arc(width - self.corner_radius*2, height - self.corner_radius*2, width, height, start=270, extent=90, fill=self.default_color, outline='')
        self.create_rectangle(self.corner_radius, 0, width - self.corner_radius, height, fill=self.default_color, outline='')
        self.create_rectangle(0, self.corner_radius, width, height - self.corner_radius, fill=self.default_color, outline='')

    def on_enter(self, event):
        self.itemconfig(0, fill=self.hover_color)  # Change fill color on hover

    def on_leave(self, event):
        self.itemconfig(0, fill=self.default_color)  # Restore fill color on leave

    def invoke(self):
        if self.command:
            self.command()

class RoundedButtons(tk.Canvas):
    def __init__(self, master=None, text="", width=200, height=40, corner_radius=0, bg='#67bcff',font=("Helvetica", 14, 'bold'), hover_color='', command=None):
        super().__init__(master, width=width, height=height, highlightthickness=0)
        self.corner_radius = corner_radius
        self.default_color = bg
        self.hover_color = hover_color
        self.command = command

        self.create_rounded_rectangle()
        self.create_text(width//2, height//2, text=text, font=('Helvetica', 12), fill='black')

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", lambda event: self.invoke())

    def create_rounded_rectangle(self):
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()

        self.create_rectangle(0, 0, width, height, fill=self.default_color, outline='', width=0)

        # Draw rounded corners
        self.create_arc(0, 0, self.corner_radius*2, self.corner_radius*2, start=90, extent=90, fill=self.default_color, outline='')
        self.create_arc(width - self.corner_radius*2, 0, width, self.corner_radius*2, start=0, extent=90, fill=self.default_color, outline='')
        self.create_arc(0, height - self.corner_radius*2, self.corner_radius*2, height, start=180, extent=90, fill=self.default_color, outline='')
        self.create_arc(width - self.corner_radius*2, height - self.corner_radius*2, width, height, start=270, extent=90, fill=self.default_color, outline='')

        # Draw straight edges
        self.create_rectangle(self.corner_radius, 0, width - self.corner_radius, height, fill=self.default_color, outline='')
        self.create_rectangle(0, self.corner_radius, width, height - self.corner_radius, fill=self.default_color, outline='')

    def on_enter(self, event):
        self.itemconfig(1, fill=self.hover_color)  # Change color on hover

    def on_leave(self, event):
        self.itemconfig(1, fill=self.default_color)  # Restore color on leave

    def invoke(self):
        if self.command:
            self.command()


class RoundedButtonstop(tk.Canvas):
    def __init__(self, master=None, text="", width=170, height=40, corner_radius=20, bg='#00aaf5', hover_color='#00aaf5',font=("Helvetica", 16, 'bold'), command=None):
        super().__init__(master, width=width, height=height, highlightthickness=0)
        self.corner_radius = corner_radius
        self.default_color = bg
        self.hover_color = hover_color
        self.command = command

        self.create_rounded_rectangle()
        self.create_text(width//2, height//2, text=text, font=('Helvetica', 12), fill='black')

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", lambda event: self.invoke())

    def create_rounded_rectangle(self):
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()

        self.create_rectangle(0, 0, width, height, fill=self.default_color, outline='', width=0)

        # Draw rounded corners
        self.create_arc(0, 0, self.corner_radius*2, self.corner_radius*2, start=90, extent=90, fill=self.default_color, outline='')
        self.create_arc(width - self.corner_radius*2, 0, width, self.corner_radius*2, start=0, extent=90, fill=self.default_color, outline='')
        self.create_arc(0, height - self.corner_radius*2, self.corner_radius*2, height, start=180, extent=90, fill=self.default_color, outline='')
        self.create_arc(width - self.corner_radius*2, height - self.corner_radius*2, width, height, start=270, extent=90, fill=self.default_color, outline='')

        # Draw straight edges
        self.create_rectangle(self.corner_radius, 0, width - self.corner_radius, height, fill=self.default_color, outline='')
        self.create_rectangle(0, self.corner_radius, width, height - self.corner_radius, fill=self.default_color, outline='')

    def on_enter(self, event):
        self.itemconfig(1, fill=self.hover_color)  # Change color on hover

    def on_leave(self, event):
        self.itemconfig(1, fill=self.default_color)  # Restore color on leave

    def invoke(self):
        if self.command:
            self.command()


def main():
    root = tk.Tk()
    app = DomainInfoManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
