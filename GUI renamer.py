import os
import customtkinter as ctk
from tkinter import filedialog

app = ctk.CTk()
app.geometry("430x500")
app.title("File Renamer Tool")

def renamer_func(old_name, new_name, old, new):
    try:
        if old_name==new_name:
            return
        os.rename(old, new)
        msg=f"Sucessfully renamed {old_name} -> {new_name}\n"
        preview_box.insert("end", msg)
        return 1
    except Exception as e:
        msg=f"File {old_name} not successfully renamed...\nReason: {e}\n"
        preview_box.insert("end", msg)
        return 0
# 0=false, 1=true, return=unchanged
# |        |       |___>File was already in required format
# |        |_____________>Operation performed succesfully
# |________________________>Operation cannot be perfomed
def renamer_btn_func():
    path = path_entry.get()

    preview_box.configure(state="normal")
    preview_box.delete("0.0", "end")
    if not os.path.isdir(path):
        preview_box.insert("end", "Invalid Path... :(\n\nEnter valid path :)")
        preview_box.configure(state="disabled")
        return
    else:
        files = os.listdir(path)
        num_files = 0
        for old_name in files:
            if os.path.isfile(os.path.join(path, old_name)):
                num_files+=1
        msg=f"Total files : {num_files}\n"
        if num_files==0:
            msg="This folder contains no files...\nAdd files to this directory or Enter a different path.\n"
            preview_box.insert("end", msg)
            preview_box.configure(state="disabled")
            return
        msg=msg+"Starting Rename Process...\n------------------------\n"
        preview_box.insert("end", msg)
        pattern = pattern_menu.get()
        if pattern=="Sequence":
            success_count = 0
            fail_count = 0
            total_files = 0
            format=s_format_menu.get()
            if format=="New Name":
                count=1
                for old_name in files:
                    if os.path.isfile(os.path.join(path, old_name)):
                        name, ext = os.path.splitext(old_name)
                        entry_name=text_entry.get()
                        new_name = entry_name + str(count) + ext
                        old=os.path.join(path, old_name)
                        new=os.path.join(path, new_name)

                        result=renamer_func(old_name, new_name, old, new)


                        if result == 1:
                            count+=1
                            success_count += 1
                            total_files+=1
                        elif result== 0:
                            fail_count += 1
                            total_files+=1
            elif format=="Original Name":
                count=1
                for old_name in files:
                    if os.path.isfile(os.path.join(path, old_name)):
                        name, ext = os.path.splitext(old_name)
                        new_name = name + str(count) + ext
                        old=os.path.join(path, old_name)
                        new=os.path.join(path, new_name)

                        result=renamer_func(old_name, new_name, old, new)

                        if result == 1:
                            count+=1
                            success_count += 1
                            total_files+=1
                        elif result== 0:
                            fail_count += 1
                            total_files+=1
            summary(total_files, success_count, fail_count)
        elif pattern=="Prefix":
            success_count = 0
            fail_count = 0
            total_files = 0
            prefix = text_entry.get()
            for old_name in files:
                if os.path.isfile(os.path.join(path, old_name)):
                    new_name = prefix + old_name
                    old=os.path.join(path, old_name)
                    new=os.path.join(path, new_name)
                    result=renamer_func(old_name, new_name, old, new)
                    if result == 1:
                        success_count += 1
                        total_files+=1
                    elif result== 0:
                        fail_count += 1
                        total_files+=1
            summary(total_files, success_count, fail_count)
        elif pattern=="Suffix":
            success_count = 0
            fail_count = 0
            total_files = 0
            suffix = text_entry.get()
            for old_name in files:
                if os.path.isfile(os.path.join(path, old_name)):
                    name, ext = os.path.splitext(old_name)
                    new_name = name + suffix + ext
                    old=os.path.join(path, old_name)
                    new=os.path.join(path, new_name)
                    result=renamer_func(old_name, new_name, old, new)
                    if result == 1:
                        success_count += 1
                        total_files+=1
                    elif result== 0:
                        fail_count += 1
                        total_files+=1
            summary(total_files, success_count, fail_count)
        elif pattern=="Case Swap":
            success_count = 0
            fail_count = 0
            total_files = 0
            if var_lower.get()==1:
                for old_name in files:
                    if os.path.isfile(os.path.join(path, old_name)):
                        name, ext = os.path.splitext(old_name)
                        new_name = name.lower() + ext
                        old=os.path.join(path, old_name)
                        new=os.path.join(path, new_name)
                        result=renamer_func(old_name, new_name, old, new)
                        if result == 1:
                            success_count += 1
                            total_files+=1
                        elif result== 0:
                            fail_count += 1
                            total_files+=1
            elif var_upper.get()==1:
                for old_name in files:
                    if os.path.isfile(os.path.join(path, old_name)):
                        name, ext = os.path.splitext(old_name)
                        new_name = name.upper() + ext
                        old=os.path.join(path, old_name)
                        new=os.path.join(path, new_name)
                        result=renamer_func(old_name, new_name, old, new)
                        if result == 1:
                            success_count += 1
                            total_files+=1
                        elif result== 0:
                            fail_count += 1
                            total_files+=1
            summary(total_files, success_count, fail_count)
        elif pattern=="Replace":
            success_count = 0
            fail_count = 0
            total_files = 0
            old=text_entry.get()
            new=text_entry1.get()
            for old_name in files:
                if os.path.isfile(os.path.join(path, old_name)):
                    name, ext = os.path.splitext(old_name)
                    name=name.replace(old, new)
                    new_name= name+ext
                    old_path=os.path.join(path, old_name)
                    new_path=os.path.join(path, new_name)
                    result=renamer_func(old_name, new_name, old_path, new_path)
                    if result == 1:
                        success_count += 1
                        total_files+=1
                    elif result== 0:
                        fail_count += 1
                        total_files+=1
            summary(total_files, success_count, fail_count)
        else:
           msg="Select a Valid Pattern to continue..."
           preview_box.insert("end", msg) 
           return

    preview_box.configure(state="disabled")

def summary(all, success, fail):
    msg=f"\n" + "="*30 + "\n" + "       TASK SUMMARY" + "\n" +"="*30 + "\n" + "Total Files Processed: " f"{all}" + "\n" + "Successfully Renamed:  " f"{success}" +"\n" + "Failed to Rename:      " f"{fail}" + "\n" + "="*30 + "\n"
    preview_box.insert("end", msg)

def update_preview(event=None):
    path = path_entry.get()

    preview_box.configure(state="normal")
    preview_box.delete("1.0", "end")
    
    if not os.path.isdir(path):
        preview_box.insert("end", "Invalid Path...")
        preview_box.configure(state="disabled")
        return
    
    files = os.listdir(path)[:20]
    header = f"{'ORIGINAL':<25} | {'PREVIEW':<25}\n"
    preview_box.insert("end", header + "-"*55 + "\n")
    pattern = pattern_menu.get()

    if pattern=="Sequence":
        format=s_format_menu.get()
        if format=="New Name":
            count=1
            for old_name in files:
                if os.path.isfile(os.path.join(path, old_name)):
                    name, ext = os.path.splitext(old_name)
                    entry_name=text_entry.get()
                    new_name = entry_name + str(count) + ext
                    count+=1
                    disp_old = shorten_filename(old_name)
                    disp_new = shorten_filename(new_name)
                    line = f"{disp_old:<25} | {disp_new:<25}\n"
                    preview_box.insert("end", line)
        elif format=="Original Name":
            count=1
            for old_name in files:
                if os.path.isfile(os.path.join(path, old_name)):
                    name, ext = os.path.splitext(old_name)
                    new_name = name + str(count) + ext
                    count+=1
                    disp_old = shorten_filename(old_name)
                    disp_new = shorten_filename(new_name)
                    line = f"{disp_old:<25} | {disp_new:<25}\n"
                    preview_box.insert("end", line)
        else:
            preview_box.delete(0.0, "end")
            msg="No Format Selected"
            preview_box.insert("end", msg)
    elif pattern=="Prefix":
        prefix = text_entry.get()
        for old_name in files:
            if os.path.isfile(os.path.join(path, old_name)):
                # Create the preview string
                new_name = prefix + old_name

                # Format with dots if too long
                disp_old = shorten_filename(old_name)
                disp_new = shorten_filename(new_name)

                # 4. Render
                line = f"{disp_old:<25} | {disp_new:<25}\n"
                preview_box.insert("end", line)
    elif pattern=="Suffix":
        suffix = text_entry.get()
        for old_name in files:
            if os.path.isfile(os.path.join(path, old_name)):
                # Create the preview string
                name, ext = os.path.splitext(old_name)
                new_name = name + suffix + ext
                # Format with dots if too long
                disp_old = shorten_filename(old_name)
                disp_new = shorten_filename(new_name)

                # 4. Render
                line = f"{disp_old:<25} | {disp_new:<25}\n"
                preview_box.insert("end", line)
    elif pattern=="Case Swap":
        if var_lower.get()==1:
            for old_name in files:
                if os.path.isfile(os.path.join(path, old_name)):
                    # Create the preview string
                    name, ext = os.path.splitext(old_name)
                    new_name = name.lower() + ext
                    # Format with dots if too long
                    disp_old = shorten_filename(old_name)
                    disp_new = shorten_filename(new_name)

                    # 4. Render
                    line = f"{disp_old:<25} | {disp_new:<25}\n"
                    preview_box.insert("end", line)
        elif var_upper.get()==1:
            for old_name in files:
                if os.path.isfile(os.path.join(path, old_name)):
                    # Create the preview string
                    name, ext = os.path.splitext(old_name)
                    new_name = name.upper() + ext
                    # Format with dots if too long
                    disp_old = shorten_filename(old_name)
                    disp_new = shorten_filename(new_name)

                    # 4. Render
                    line = f"{disp_old:<25} | {disp_new:<25}\n"
                    preview_box.insert("end", line)

    elif pattern=="Replace":
        old=text_entry.get()
        new=text_entry1.get()
        for old_name in files:
                if os.path.isfile(os.path.join(path, old_name)):
                    # Create the preview string
                    name, ext = os.path.splitext(old_name)
                    new_name=name.replace(old, new)
                    final_name=new_name+ext
                    # Format with dots if too long
                    disp_old = shorten_filename(old_name)
                    disp_new = shorten_filename(final_name)

                    # 4. Render
                    line = f"{disp_old:<25} | {disp_new:<25}\n"
                    preview_box.insert("end", line)
        
    else:
        for old_name in files:
            if os.path.isfile(os.path.join(path, old_name)):

                # Format with dots if too long
                disp_old = shorten_filename(old_name)

                # 4. Render
                line = f"{disp_old:<25} | {disp_old:<25}\n"
                preview_box.insert("end", line)

    preview_box.configure(state="disabled")

def shorten_filename(filename, max_length=19):
    # Split into name and extension
    name, ext = os.path.splitext(filename)

    # If length is within limit, return unchanged
    if len(name) <= max_length:
        return filename

    # Calculate how many characters we can keep before adding "(...)"
    keep_length = max_length - 5  # 5 chars for "(...)"
    shortened_name = name[:keep_length] + "(...)"

    return shortened_name + ext

def format_preview(choice):
    update_seq_ui(choice)
    update_preview()

def main_preview(choice):
    update_main_ui(choice)
    update_preview()

def browse_func():
    selected_path=filedialog.askdirectory()
    if selected_path:
        path_entry.delete(0, 'end')
        path_entry.insert(0, selected_path)
    update_preview()

# def preview_func():
#     preview=preview_switch.get()
#     if preview==1:
#         preview_label.grid(row=6, column=0)
#     else:
#         preview_label.grid_forget()

def update_main_ui(choice):

    s_format_label.grid_forget()
    s_format_menu.grid_forget()
    text_label.grid_forget()
    text_entry.grid_forget()
    text_label1.grid_forget()
    text_entry1.grid_forget()
    cb_lower.grid_forget()
    cb_upper.grid_forget()
    #update_preview()
    if choice=="Sequence":
        s_format_menu.set("Select Format")
        s_format_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        s_format_menu.grid(row=0, column=1)
    elif choice == "Prefix" or choice == "Suffix":
        text_label.configure(text=f"Enter {choice}:", font=("Arial", 16))
        text_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        text_entry.configure(placeholder_text="")
        text_entry.grid(row=0, column=1, padx=10, pady=10)
    elif choice=="Case Swap":
        cb_upper.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        cb_lower.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    elif choice=="Replace":
        text_label.configure(text="Old Text:", font=("Arial", 16))
        text_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        text_entry.configure(placeholder_text="")
        text_entry.grid(row=0, column=1, padx=10, pady=10)
        text_label1.configure(text="New Text:", font=("Arial", 16))
        text_label1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        text_entry1.grid(row=1, column=1, padx=10, pady=10)

def update_seq_ui(choice):
    if choice=="New Name":
        text_label.configure(text="Name:", font=("Arial", 16))
        text_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        #text_entry.configure(placeholder_text="Enter New Name")
        text_entry.grid(row=1, column=1, padx=10, pady=10)
    elif choice=="Original Name":
        text_label.grid_forget()
        text_entry.grid_forget()

def interlock_upper():
    # if (var_upper.get()==1 or var_upper.get()==0):
        var_upper.set(0)
        var_lower.set(1)
        update_preview()
def interlock_lower():
    # if (var_lower.get()==1 or var_lower.get()==0):
        var_upper.set(1)
        var_lower.set(0)
        update_preview()

patterns = ["Sequence", "Prefix", "Suffix","Case Swap", "Replace"]
s_format = ["Original Name", "New Name"]

#============ PATH (label-entry-button) (FIXED) ===================================
frame_1 = ctk.CTkFrame(app, height=100, width=260,fg_color="transparent")
frame_1.grid(row=0, column=0, sticky="nsew")
path_label= ctk.CTkLabel(frame_1, text="Path:", font=("Arial", 16))
path_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
path_entry =ctk.CTkEntry(frame_1, placeholder_text="Enter Folder Path", width=150)
path_entry.grid(row=0, column=1, pady=10, padx=10)
path_entry.bind("<KeyRelease>", update_preview)
browse_btn= ctk.CTkButton(frame_1, text="Browse", command=browse_func, width=100)
browse_btn.grid(row=0, column=2,pady=10)
#============ PATTERN (label-menu) (FIXED) ========================================
pattern_label = ctk.CTkLabel(frame_1, text="Pattern:", font=("Arial", 16))
pattern_label.grid(row=1, column=0, padx=10,pady=10, sticky="w")
pattern_menu = ctk.CTkOptionMenu(frame_1, values=patterns, command=main_preview, width=150)
pattern_menu.grid(row=1, column=1, pady=10)
pattern_menu.set("Select Pattern")
#============ sequence-> format (label-menu) (DEPENDENT -> PATTERN[sequence]) ================
frame_2 = ctk.CTkFrame(app, height=100, width=360,fg_color="transparent")
frame_2.grid(row=1, column=0, sticky="nsew")
frame_2.grid_propagate(False)
s_format_label= ctk.CTkLabel(frame_2, text="Format:", font=("Arial", 16))
s_format_menu= ctk.CTkOptionMenu(frame_2, values=s_format, command=format_preview, width=150)
s_format_menu.set("Select Format")
#============ TEXT ENTRY (label-entry) (DEPENDENT -> PATTERN[prefix]
#------------------------------------------------ -> PATTERN[suffix]
#------------------------------------------------ -> PATTERN[replace]
#------------------------------------------------ -> FORMAT[new name])
text_label= ctk.CTkLabel(frame_2)
text_entry= ctk.CTkEntry(frame_2, width=150)
text_entry.bind("<KeyRelease>", update_preview)

#============ TEXT ENTRY (label-entry) (DEPENDENT -> -> PATTERN[replace])
text_label1= ctk.CTkLabel(frame_2)
text_entry1= ctk.CTkEntry(frame_2, width=150)
text_entry1.bind("<KeyRelease>", update_preview)
#============ SELECTION (checkbox) (DEPENDENT -> PATTERN[case swap])
var_upper = ctk.IntVar(value=0)
var_lower = ctk.IntVar(value=1)
cb_upper = ctk.CTkCheckBox(frame_2, text="Upper Case",command=interlock_lower, variable=var_upper, onvalue=1, offvalue=0, font=("Arial", 16))
# cb_upper.grid(row=3, column=0, padx=40, pady=20, sticky="w")
cb_lower = ctk.CTkCheckBox(frame_2, text="Lower Case",command=interlock_upper, variable=var_lower, onvalue=1, offvalue=0, font=("Arial", 16))
# cb_lower.grid(row=4, column=0, padx=40, pady=20, sticky="w")

#=========== PREVIEW (Switch) (FIXED) =====================================
# preview_switch = ctk.CTkSwitch(app, text="Preview", progress_color="red", command=preview_func)
# preview_switch.grid(row=5, column=0, sticky="w")
#=========== PREVIEW (Label) (DEPENDENT -> PREVIEW SWITCH)
# preview_label= ctk.CTkLabel(app, text="Rename would be:", font=("Arial", 16))

#=========== FINAL BUTTON (button) (FIXED) =================================
frame_3 = ctk.CTkFrame(app, corner_radius=10)
frame_3.grid(row=2, column=0,padx=10, sticky="nsew")
rename_btn= ctk.CTkButton(frame_3, text="RENAME", width=100, command=renamer_btn_func)
rename_btn.pack(pady=10)

#=========== Preview Mode (label) (FIXED) =====================================
# preview_label= ctk.CTkLabel(app, text="Preview")
# preview_label.grid(row=0, column=3)

#=========== Console Box (textbox) (FIXED) ====================================
preview_box = ctk.CTkTextbox(frame_3, width=410, height=250, state="disabled", border_width=2, font=("Consolas", 12))
preview_box.pack(pady=0)

app.mainloop()