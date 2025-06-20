from tkinter import *
import tkinter
import customtkinter
import random
import os
import pygame
import threading

customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.title("Xavier's Dice Roller")
root.geometry('1000x1000')

pygame.mixer.init()

def jb4_music():
        pygame.mixer.music.load("/Users/frater47/Documents/cyberSec/fall2024/programming/python/personal_projects/dnd_dice_roller/JB4.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

threading.Thread(target=jb4_music, daemon=True).start()


##Setting Tabs
tabs = customtkinter.CTkTabview(root,
                                width=950,
                                height=950,
                                segmented_button_fg_color='#8c100d',
                                segmented_button_selected_color='#8c100d',
                                segmented_button_unselected_color='#520907',
                                segmented_button_selected_hover_color='#8c100d',
                                segmented_button_unselected_hover_color='#520907'
                                
                                )
tabs.pack(pady=10)
tab1 = tabs.add("Rolls")
tab2 = tabs.add("Spells")
tab3 = tabs.add("Metamagic")
tab4 = tabs.add("Inventory")



###Tab 1 - Rolls




#Advantage/Disadvantage Checkbox and Function

checkbox_toggle = customtkinter.IntVar(value=0)
advantage_checkbox = customtkinter.CTkCheckBox(tab1, text="Advantage/\nDisadvantage", border_color='#8c100d',
                                   hover_color='#8c100d', fg_color='#8c100d', 
                                   variable=checkbox_toggle, onvalue=1, offvalue=0,
                                   checkbox_width=14, checkbox_height=14,
                                   font=('Engravers MT', 10)
                                   )
advantage_checkbox.grid(row=2, column=4, pady=20)



def adv_dis():
    init_text = ''
    rolls20 = []
    if checkbox_toggle.get() == 0:
         for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        init_text = (f'\t{y} + 3 = {y + 3}\n')
         return init_text 
    elif checkbox_toggle.get() == 1:
        for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
        init_text = (f'\t{rolls20[0]} + 3 = {rolls20[0] + 3}\n\t{rolls20[1]} + 3 = {rolls20[1] + 3}\n')
        return init_text     




##Initiative Button and Function

def init():
        
        result=adv_dis()
        
        roll_label.configure(text=f'\tYour Initiative Roll is:\n{result}')




init_button = customtkinter.CTkButton(tab1,border_color="black", fg_color="#8c100d", text_color="white", 
                                      text="Initiative\t+ 3", hover_color="#4b0303",
                                      command=init
                                      
                                      )
init_button.grid(row=1, column=1, pady=90)




##Main Label at Top that shows Results of Rolls

roll_label = customtkinter.CTkLabel(tab1, text="", font=('Engravers MT', 20))
roll_label.grid(row=1, column=3, columnspan=6, rowspan=1, sticky='w')




##HP Label, HP Increase, HP Decrease

hp_entry = customtkinter.CTkTextbox(tab1, width=35, height=30, font=('Engravers MT', 16),
                                    border_color="black", fg_color="#8c100d", 
                                    text_color="white",)
hp_entry.grid(row=10, column=6, sticky='n')


hp_total = int(27)
hp_label = customtkinter.CTkLabel(tab1, text=(f'HP\n{hp_total}'), font=('Engravers MT', 26))
hp_label.grid(row=9, column=6, pady=30, sticky='s' )

def hp_up():
        global hp_total
        global increase
        increase = hp_entry.get("1.0", "end-1c")
        if not increase:
                increase = 1
        else:
                increase = int(hp_entry.get("1.0", "end-1c"))
        if hp_total < 27:
            hp_total += increase
            
        hp_label.configure(text=(f'HP\n{hp_total}'))
        hp_entry.delete("1.0", "end")
        
        
        
        
        

up_button = customtkinter.CTkButton(tab1, text='+', font=('Engravers MT', 16),
                                    border_color="black", fg_color="#8c100d", 
                                    text_color="white", hover_color="#4b0303",
                                    width=30, command=hp_up

                                    )
up_button.grid(row=10, column=6,sticky='e')




def hp_down():
        global hp_total
        global decrease
        decrease = hp_entry.get("1.0", "end-1c")
        if not decrease:
                decrease = 1
        else:
                decrease = int(hp_entry.get("1.0", "end-1c"))
        if hp_total > 0:
            hp_total -= decrease
            if hp_total < 0:
                    hp_total = 0
            
        hp_label.configure(text=(f'HP\n{hp_total}'))
        hp_entry.delete("1.0", "end")


down_button = customtkinter.CTkButton(tab1, text='-', font=('Engravers MT', 16),
                                    border_color="black", fg_color="#8c100d", 
                                    text_color="white", hover_color="#4b0303",
                                    width=30, command=hp_down

                                    )
down_button.grid(row=10, column=6, sticky='w')


def long_rest():
        global current_lv1_slot
        global hp_total
        current_lv1_slot = 1
        spell_slots_1_1.deselect()
        spell_slots_1_2.deselect()
        spell_slots_1_3.deselect()
        spell_slots_1_4.deselect()
        spell_slots_2_1.deselect()
        spell_slots_2_2.deselect()
        spell_slots_2_3.deselect()
        spell_slots_3_1.deselect()
        spell_slots_3_2.deselect()
        hp_total = int(27)
        hp_label.configure(text=(f'HP\n{int(27)}'))
        spell_output_label.configure(text='')
        sorcery_point_1.deselect()
        sorcery_point_2.deselect()
        sorcery_point_3.deselect()
        sorcery_point_4.deselect()
        sorcery_point_5.deselect()
        sorcery_point_6.deselect()
        
        
        
               
long_rest_butt = customtkinter.CTkButton(tab1, text='Long Rest', font=('Engravers MT', 16),
                                    border_color="black", fg_color="#8c100d", 
                                    text_color="white", hover_color="#4b0303",
                                    command=long_rest, width=75)
long_rest_butt.grid(row=10, column=5, sticky='w')


def short_rest():
        global hp_total
        hp_total = int(27)
        hp_label.configure(text=(f'HP\n{int(27)}'))

short_rest_butt = customtkinter.CTkButton(tab1, text='Short Rest',  font=('Engravers MT', 16),
                                    border_color="black", fg_color="#8c100d", 
                                    text_color="white", hover_color="#4b0303",
                                    command=short_rest, width=75)

short_rest_butt.grid(row=9, column=5, sticky='sw', pady=5)

##Clear Roll Button and Functions

def clear():
        roll_label.configure(text='')
        rad_ac.deselect()
        rad_ah.deselect()
        rad_arc.deselect()
        rad_ath.deselect()
        rad_dec.deselect()
        rad_his.deselect()
        rad_ins.deselect()
        rad_int.deselect()
        rad_inv.deselect()
        rad_med.deselect()
        rad_nat.deselect()
        rad_perc.deselect()
        rad_perf.deselect()
        rad_pers.deselect()
        rad_rel.deselect()
        rad_soh.deselect()
        rad_stl.deselect()
        rad_sur.deselect()
        advantage_checkbox.deselect()
        roll_entry.delete(0, END)


clear_button = customtkinter.CTkButton(tab1,border_color="black", fg_color="#8c100d", text_color="white", 
                                      text="Clear Roll", hover_color="#4b0303",
                                      command=clear
                                      
                                      )
clear_button.grid(row=1, column=6, pady=90)



##Skill Check Label

label_chk = customtkinter.CTkLabel(tab1, text="Skill Checks", fg_color="transparent", font=('Engravers MT', 20))
label_chk.grid(row=2, column=1, pady=20)



##Strength Skill Check

def str_roll():
        str_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                str_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                str_text = (f'\t{y} Critical Failure!\n')
                        else:
                                str_text = (f'\t{y} - 2 = {y - 2}\n')
                return str_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                str_text = (f'\t{rolls20[0]} - 2 = {rolls20[0] - 2}\n\t{rolls20[1]} - 2 = {rolls20[1] - 2}\n')
                return str_text



def str():
      result=str_roll() 
      roll_label.configure(text=(f'\tYour Strength Check is:\n{result}')) 





str_butt = customtkinter.CTkButton(tab1,border_color="black", fg_color="#8c100d", 
                              text_color="white", text="Strength\t- 2", hover_color="#4b0303",
                              command=str
                              
                              )
str_butt.grid(row=3, column=1, padx=30, pady=10)



##Dexterity Skill Check

def dex_roll():
        dex_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                dex_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                dex_text = (f'\t{y} Critical Failure!\n')
                        else:
                                dex_text = (f'\t{y} + 3 = {y + 3}\n')
                return dex_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                dex_text = (f'\t{rolls20[0]} + 3 = {rolls20[0] + 3}\n\t{rolls20[1]} + 3 = {rolls20[1] + 3}\n')
                return dex_text




def dex():
      result=dex_roll() 
      roll_label.configure(text=(f'\tYour Dexterity Check is:\n{result}'))




dex_butt = customtkinter.CTkButton(tab1,border_color="black", fg_color="#8c100d", 
                              text_color="white", text="Dexterity\t+ 3", hover_color="#4b0303",
                              command=dex
                              
                              )
dex_butt.grid(row=4, column=1, padx=30, pady=10)






##Constitution Skill Check

def con_roll():
        con_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                con_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                con_text = (f'\t{y} Critical Failure!\n')
                        else:
                                con_text = (f'\t{y} + 0 = {y}\n')
                return con_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                con_text = (f'\t{rolls20[0]} + 0 = {rolls20[0] + 0}\n\t{rolls20[1]} + 0 = {rolls20[1] + 0}\n')
                return con_text




def con():
      result=con_roll() 
      roll_label.configure(text=(f'\tYour Constitution Check is:\n{result}'))



con_butt = customtkinter.CTkButton(tab1,border_color="black", fg_color="#8c100d", 
                              text_color="white", text="Constitution  + 0", hover_color="#4b0303",
                              command=con
                              
                              )
con_butt.grid(row=5, column=1, padx=30, pady=10)




##Intelligence Skill Check

def int_roll():
        int_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                int_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                int_text = (f'\t{y} Critical Failure!\n')
                        else:
                                int_text = (f'\t{y} + 1 = {y}\n')
                return int_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                int_text = (f'\t{rolls20[0]} + 1 = {rolls20[0] + 1}\n\t{rolls20[1]} + 1 = {rolls20[1] + 1}\n')
                return int_text



def intelligence():
      result=int_roll() 
      roll_label.configure(text=(f'\tYour Intelligence Check is:\n{result}'))




int_butt = customtkinter.CTkButton(tab1,border_color="black", fg_color="#8c100d", text_color="white", 
                              text="Intelligence\t+ 1", hover_color="#4b0303",
                              command=intelligence
                              
                              )
int_butt.grid(row=6, column=1, padx=30, pady=10)





##Wisdom Skill Check

def wis_roll():
        wis_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                wis_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                wis_text = (f'\t{y} Critical Failure!\n')
                        else:
                                wis_text = (f'\t{y} + 3 = {y + 3}\n')
                return wis_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                wis_text = (f'\t{rolls20[0]} + 3 = {rolls20[0] + 3}\n\t{rolls20[1]} + 3 = {rolls20[1] + 3}\n')
                return wis_text




def wis():
      result=wis_roll() 
      roll_label.configure(text=(f'\tYour Wisdom Check is:\n{result}'))



wis_butt = customtkinter.CTkButton(tab1,border_color="black", fg_color="#8c100d", 
                              text_color="white", text="Wisdom\t+ 3", hover_color="#4b0303",
                              command=wis
                              
                              )
wis_butt.grid(row=7, column=1, padx=30, pady=10)





##Charisma Skill Check

def cha_roll():
        cha_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                cha_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                cha_text = (f'\t{y} Critical Failure!\n')
                        else:
                                cha_text = (f'\t{y} + 5 = {y + 5}\n')
                return cha_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                cha_text = (f'\t{rolls20[0]} + 5 = {rolls20[0] + 5}\n\t{rolls20[1]} + 5 = {rolls20[1] + 5}\n')
                return cha_text




def cha():
      result=cha_roll() 
      roll_label.configure(text=(f'\tYour Charisma Check is:\n{result}'))



cha_butt = customtkinter.CTkButton(tab1,border_color="black", fg_color="#8c100d", 
                              text_color="white", text="Charisma\t+ 5", hover_color="#4b0303",
                              command=cha
                              
                              )
cha_butt.grid(row=8, column=1, padx=30, pady=10)



##Saving Throw Label

label_sav = customtkinter.CTkLabel(tab1, text="Saving Throws", fg_color="transparent", font=('Engravers MT', 20))
label_sav.grid(row=2, column=6, pady=20)



##Strength Saving Throw

def strsav_roll():
        strsav_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                strsav_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                strsav_text = (f'\t{y} Critical Failure!\n')
                        else:
                                strsav_text = (f'\t{y} - 2 = {y - 2}\n')
                return strsav_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                strsav_text = (f'\t{rolls20[0]} - 2 = {rolls20[0] - 2}\n\t{rolls20[1]} - 2 = {rolls20[1] - 2}\n')
                return strsav_text




def strsav():
      result=strsav_roll() 
      roll_label.configure(text=(f'\tYour Strength Save is:\n{result}'))




sav_str = customtkinter.CTkButton(tab1,border_color="black", fg_color="#8c100d", 
                              text_color="white", text="Strength\t- 2", hover_color="#4b0303",
                              command=strsav
                              
                              )
sav_str.grid(row=3, column=6, padx=30, pady=10)






##Dexterity Saving Throw

def dexsav_roll():
        dexsav_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                dexsav_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                dexsav_text = (f'\t{y} Critical Failure!\n')
                        else:
                                dexsav_text = (f'\t{y} + 3 = {y + 3}\n')
                return dexsav_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                dexsav_text = (f'\t{rolls20[0]} + 3 = {rolls20[0] + 3}\n\t{rolls20[1]} + 3 = {rolls20[1] + 3}\n')
                return dexsav_text




def dexsav():
      result=dexsav_roll() 
      roll_label.configure(text=(f'\tYour Dexterity Save is:\n{result}'))



sav_dex = customtkinter.CTkButton(tab1,border_color="black", fg_color="#8c100d", 
                              text_color="white", text="Dexterity\t+ 3", hover_color="#4b0303",
                              command=dexsav
                              
                              )
sav_dex.grid(row=4, column=6, padx=30, pady=10)







##Consitution Saving Throw

def consav_roll():
        consav_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                consav_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                consav_text = (f'\t{y} Critical Failure!\n')
                        else:
                                consav_text = (f'\t{y} + 2 = {y + 2}\n')
                return consav_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                consav_text = (f'\t{rolls20[0]} + 2 = {rolls20[0] + 2}\n\t{rolls20[1]} + 2 = {rolls20[1] + 2}\n')
                return consav_text




def consav():
      result=consav_roll() 
      roll_label.configure(text=(f'\tYour Constitution Save is:\n{result}'))






sav_con = customtkinter.CTkButton(tab1,border_color="black", fg_color="#8c100d", 
                              text_color="white", text="Consitution\t+ 2", hover_color="#4b0303",
                              command=consav
                              
                              )
sav_con.grid(row=5, column=6, padx=30, pady=10)






##Intelligence Saving Throw

def intsav_roll():
        intsav_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                intsav_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                intsav_text = (f'\t{y} Critical Failure!\n')
                        else:
                                intsav_text = (f'\t{y} + 0 = {y}\n')
                return intsav_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                intsav_text = (f'\t{rolls20[0]} + 0 = {rolls20[0] + 0}\n\t{rolls20[1]} + 0 = {rolls20[1] + 0}\n')
                return intsav_text




def intsav():
      result=intsav_roll() 
      roll_label.configure(text=(f'\tYour Intelligence Save is:\n{result}'))





sav_int = customtkinter.CTkButton(tab1,border_color="black", fg_color="#8c100d", 
                              text_color="white", text="Intelligence  + 0", hover_color="#4b0303",
                              command=intsav
                              
                              )
sav_int.grid(row=6, column=6, padx=30, pady=10)






##Wisdom Saving Throw

def wissav_roll():
        wissav_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                wissav_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                wissasv_text = (f'\t{y} Critical Failure!\n')
                        else:
                                wissav_text = (f'\t{y} + 3 = {y + 3}\n')
                return wissav_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                wissav_text = (f'\t{rolls20[0]} + 3 = {rolls20[0] + 3}\n\t{rolls20[1]} + 3 = {rolls20[1] + 3}\n')
                return wissav_text




def wissav():
      result=wissav_roll() 
      roll_label.configure(text=(f'\tYour Wisdom Save is:\n{result}'))




sav_wis = customtkinter.CTkButton(tab1,border_color="black", fg_color="#8c100d", 
                              text_color="white", text="Wisdom\t+ 3", hover_color="#4b0303",
                              command=wissav
                              
                              )
sav_wis.grid(row=7, column=6, padx=30, pady=10)






##Charisma Saving Throw

def chasav_roll():
        chasav_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                chasav_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                chasav_text = (f'\t{y} Critical Failure!\n')
                        else:
                                chasav_text = (f'\t{y} + 7 = {y + 7}\n')
                return chasav_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                chasav_text = (f'\t{rolls20[0]} + 7 = {rolls20[0] + 7}\n\t{rolls20[1]} + 7 = {rolls20[1] + 7}\n')
                return chasav_text




def chasav():
      result=chasav_roll() 
      roll_label.configure(text=(f'\tYour Charisma Save is:\n{result}'))



sav_cha = customtkinter.CTkButton(tab1,border_color="black", fg_color="#8c100d", 
                              text_color="white", text="Charisma\t+ 7", hover_color="#4b0303",
                              command=chasav
                              
                              )
sav_cha.grid(row=8, column=6, padx=30, pady=10)









##Acrobatics Skill Check

def ac_roll():
        ac_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                ac_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                ac_text = (f'\t{y} Critical Failure!\n')
                        else:
                                ac_text = (f'\t{y} + 3 = {y + 3}\n')
                return ac_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                ac_text = (f'\t{rolls20[0]} + 3 = {rolls20[0] + 3}\n\t{rolls20[1]} + 3 = {rolls20[1] + 3}\n')
                return ac_text




def ac():
      result=ac_roll() 
      roll_label.configure(text=(f'\tYour Acrobatics Check is:\n{result}'))




radio_var = tkinter.IntVar(value=0)
rad_ac = customtkinter.CTkRadioButton(tab1, text="Acrobatics\t+ 3", value=1, variable=radio_var,
                                      fg_color="#8c100d", border_color="#8c100d", hover=False,
                                      command=ac
                                      
                                      )
rad_ac.grid(row=3, column=3, sticky='w')





##Animal Handling Skill Check

def ah_roll():
        ah_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                ah_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                ah_text = (f'\t{y} Critical Failure!\n')
                        else:
                                ah_text = (f'\t{y} + 3 = {y + 3}\n')
                return ah_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                ah_text = (f'\t{rolls20[0]} + 3 = {rolls20[0] + 3}\n\t{rolls20[1]} + 3 = {rolls20[1] + 3}\n')
                return ah_text




def ah():
      result=ah_roll() 
      roll_label.configure(text=(f'\tYour Animal Handling Check is:\n{result}'))




rad_ah = customtkinter.CTkRadioButton(tab1, text="Animal\nHandling\t+ 3", value=2, variable=radio_var,
                                      fg_color="#8c100d", border_color="#8c100d", hover=False,
                                     command=ah
                                     
                                     )
rad_ah.grid(row=4, column=3, sticky='w')





##Arcana Skill Check

def arc_roll():
        arc_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                arc_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                arc_text = (f'\t{y} Critical Failure!\n')
                        else:
                                arc_text = (f'\t{y} + 2 = {y + 2}\n')
                return arc_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                arc_text = (f'\t{rolls20[0]} + 2 = {rolls20[0] + 2}\n\t{rolls20[1]} + 2 = {rolls20[1] + 2}\n')
                return arc_text




def arc():
      result=arc_roll() 
      roll_label.configure(text=(f'\tYour Arcana Check is:\n{result}'))


rad_arc = customtkinter.CTkRadioButton(tab1, text="Arcana\t+ 2", value=3, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=arc)
rad_arc.grid(row=5, column=3, sticky='w',)





##Athletics Skill Check

def ath_roll():
        ath_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                ath_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                ath_text = (f'\t{y} Critical Failure!\n')
                        else:
                                ath_text = (f'\t{y} - 2 = {y - 2}\n')
                return ath_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                ath_text = (f'\t{rolls20[0]} - 2 = {rolls20[0] - 2}\n\t{rolls20[1]} - 2 = {rolls20[1] - 2}\n')
                return ath_text




def ath():
      result=ath_roll() 
      roll_label.configure(text=(f'\tYour Athletics Check is:\n{result}'))




rad_ath = customtkinter.CTkRadioButton(tab1, text="Athletics\t- 2", value=4, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=ath
                                       )
rad_ath.grid(row=6, column=3)






##Deception Skill Check

def dec_roll():
        dec_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                dec_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                dec_text = (f'\t{y} Critical Failure!\n')
                        else:
                                dec_text = (f'\t{y} + 5 = {y + 5}\n')
                return dec_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                dec_text = (f'\t{rolls20[0]} + 5 = {rolls20[0] + 5}\n\t{rolls20[1]} + 5 = {rolls20[1] + 5}\n')
                return dec_text




def dec():
      result=dec_roll() 
      roll_label.configure(text=(f'\tYour Deception Check is:\n{result}'))




rad_dec = customtkinter.CTkRadioButton(tab1, text="Deception\t+ 5", value=5, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=dec
                                       )
rad_dec.grid(row=7, column=3)





##History Skill Check

def his_roll():
        his_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                his_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                his_text = (f'\t{y} Critical Failure!\n')
                        else:
                                his_text = (f'\t{y} + 2 = {y + 2}\n')
                return his_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                his_text = (f'\t{rolls20[0]} + 2 = {rolls20[0] + 2}\n\t{rolls20[1]} + 2 = {rolls20[1] + 2}\n')
                return his_text




def his():
      result=his_roll() 
      roll_label.configure(text=(f'\tYour History Check is:\n{result}'))




rad_his = customtkinter.CTkRadioButton(tab1, text="History\t+ 2", value=6, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=his
                                       )
rad_his.grid(row=8, column=3)





##Insight Skill Check

def ins_roll():
        ins_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                ins_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                ins_text = (f'\t{y} Critical Failure!\n')
                        else:
                                ins_text = (f'\t{y} + 5 = {y + 5}\n')
                return ins_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                ins_text = (f'\t{rolls20[0]} + 5 = {rolls20[0] + 5}\n\t{rolls20[1]} + 5 = {rolls20[1] + 5}\n')
                return ins_text




def ins():
      result=ins_roll() 
      roll_label.configure(text=(f'\tYour Insight Check is:\n{result}'))



rad_ins = customtkinter.CTkRadioButton(tab1, text="Insight\t+ 5", value=7, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=ins
                                       )
rad_ins.grid(row=3, column=4, pady=10)





##Intimidation Skill Check

def inti_roll():
        inti_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                inti_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                inti_text = (f'\t{y} Critical Failure!\n')
                        else:
                                inti_text = (f'\t{y} + 5 = {y + 5}\n')
                return inti_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                inti_text = (f'\t{rolls20[0]} + 5 = {rolls20[0] + 5}\n\t{rolls20[1]} + 5 = {rolls20[1] + 5}\n')
                return inti_text




def inti():
      result=inti_roll() 
      roll_label.configure(text=(f'\tYour Intimidation Check is:\n{result}'))



rad_int = customtkinter.CTkRadioButton(tab1, text="Intimidation + 5", value=8, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=inti
                                       )
rad_int.grid(row=4, column=4, pady=10)





##Investigation Skill Check

def inv_roll():
        inv_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                inv_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                inv_text = (f'\t{y} Critical Failure!\n')
                        else:
                                inv_text = (f'\t{y} + 0 = {y}\n')
                return inv_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                inv_text = (f'\t{rolls20[0]} + 0 = {rolls20[0] + 0}\n\t{rolls20[1]} + 0 = {rolls20[1] + 0}\n')
                return inv_text




def inv():
      result=inv_roll() 
      roll_label.configure(text=(f'\tYour Investigation Check is:\n{result}'))



rad_inv = customtkinter.CTkRadioButton(tab1, text="Investigation + 0", value=9, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=inv
                                       )
rad_inv.grid(row=5, column=4,pady=10, padx=20,)






##Medicine Skill Check

def med_roll():
        med_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                med_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                med_text = (f'\t{y} Critical Failure!\n')
                        else:
                                med_text = (f'\t{y} + 3 = {y + 3}\n')
                return med_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                med_text = (f'\t{rolls20[0]} + 3 = {rolls20[0] + 3}\n\t{rolls20[1]} + 3 = {rolls20[1] + 3}\n')
                return med_text




def med():
      result=med_roll() 
      roll_label.configure(text=(f'\tYour Medicine Check is:\n{result}'))



rad_med = customtkinter.CTkRadioButton(tab1, text="Medicine\t+ 3", value=10, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=med
                                       )
rad_med.grid(row=6, column=4, pady=10)






##Nature Skill Check

def nat_roll():
        nat_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                nat_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                nat_text = (f'\t{y} Critical Failure!\n')
                        else:
                                nat_text = (f'\t{y} + 0 = {y}\n')
                return nat_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                nat_text = (f'\t{rolls20[0]} + 0 = {rolls20[0] + 0}\n\t{rolls20[1]} + 0 = {rolls20[1] + 0}\n')
                return nat_text




def nat():
      result=nat_roll() 
      roll_label.configure(text=(f'\tYour Nature Check is:\n{result}'))



rad_nat = customtkinter.CTkRadioButton(tab1, text="Nature\t+ 0", value=11, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=nat
                                       )
rad_nat.grid(row=7, column=4, pady=10)






##Perception Skill Check

def perc_roll():
        perc_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                perc_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                perc_text = (f'\t{y} Critical Failure!\n')
                        else:
                                perc_text = (f'\t{y} + 5 = {y + 5}\n')
                return perc_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                perc_text = (f'\t{rolls20[0]} + 5 = {rolls20[0] + 5}\n\t{rolls20[1]} + 5 = {rolls20[1] + 5}\n')
                return perc_text




def perc():
      result=perc_roll() 
      roll_label.configure(text=(f'\tYour Perception Check is:\n{result}'))



rad_perc = customtkinter.CTkRadioButton(tab1, text="Perception\t+ 5", value=12, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=perc
                                       )
rad_perc.grid(row=8, column=4,pady=10,)






##Performance Skill Check

def perf_roll():
        perf_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                perf_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                perf_text = (f'\t{y} Critical Failure!\n')
                        else:
                                perf_text = (f'\t{y} + 5 = {y + 5}\n')
                return perf_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                perf_text = (f'\t{rolls20[0]} + 5 = {rolls20[0] + 5}\n\t{rolls20[1]} + 5 = {rolls20[1] + 5}\n')
                return perf_text




def perf():
      result=perf_roll() 
      roll_label.configure(text=(f'\tYour Performance Check is:\n{result}'))



rad_perf = customtkinter.CTkRadioButton(tab1, text="Performance  + 5", value=13, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=perf
                                       )
rad_perf.grid(row=3, column=5, pady=10,)






##Persuasion Skill Check

def per_roll():
        per_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                per_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                per_text = (f'\t{y} Critical Failure!\n')
                        else:
                                per_text = (f'\t{y} + 7 = {y + 7}\n')
                return per_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                per_text = (f'\t{rolls20[0]} + 7 = {rolls20[0] + 7}\n\t{rolls20[1]} + 7 = {rolls20[1] + 7}\n')
                return per_text




def per():
      result=per_roll() 
      roll_label.configure(text=(f'\tYour Persuasion Check is:\n{result}'))


rad_pers = customtkinter.CTkRadioButton(tab1, text="Persuasion\t+ 7", value=14, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=per
                                       )
rad_pers.grid(row=4, column=5, pady=10, )






##Religion Skill Check

def rel_roll():
        rel_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                rel_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                rel_text = (f'\t{y} Critical Failure!\n')
                        else:
                                rel_text = (f'\t{y} - 2 = {y - 2}\n')
                return rel_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                rel_text = (f'\t{rolls20[0]} - 2 = {rolls20[0] - 2}\n\t{rolls20[1]} - 2 = {rolls20[1] - 2}\n')
                return rel_text




def rel():
      result=rel_roll() 
      roll_label.configure(text=(f'\tYour Religion Check is:\n{result}'))


rad_rel = customtkinter.CTkRadioButton(tab1, text="Religion\t- 2", value=15, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=rel
                                       )
rad_rel.grid(row=5, column=5,pady=10, padx=20)







##Sleight of Hand Skill Check

def soh_roll():
        soh_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                soh_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                soh_text = (f'\t{y} Critical Failure!\n')
                        else:
                                soh_text = (f'\t{y} + 3 = {y + 3}\n')
                return soh_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                soh_text = (f'\t{rolls20[0]} + 3 = {rolls20[0] + 3}\n\t{rolls20[1]} + 3 = {rolls20[1] + 3}\n')
                return soh_text




def soh():
      result=soh_roll() 
      roll_label.configure(text=(f'\tYour Sleight of Hand Check is:\n{result}'))



rad_soh = customtkinter.CTkRadioButton(tab1, text="Sleight of\nHand\t+ 3", value=16, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=soh
                                       )
rad_soh.grid(row=6, column=5, pady=10)





##Stealth Skill Check

def stl_roll():
        stl_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                stl_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                stl_text = (f'\t{y} Critical Failure!\n')
                        else:
                                stl_text = (f'\t{y} + 3 = {y + 3}\n')
                return stl_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                stl_text = (f'\t{rolls20[0]} + 3 = {rolls20[0] + 3}\n\t{rolls20[1]} + 3 = {rolls20[1] + 3}\n')
                return stl_text




def stl():
      result=stl_roll() 
      roll_label.configure(text=(f'\tYour Stealth Check is:\n{result}'))



rad_stl = customtkinter.CTkRadioButton(tab1, text="Stealth\t+ 3", value=17, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=stl
                                       )
rad_stl.grid(row=7, column=5, pady=10)






##Survival Skill Check

def sur_roll():
        sur_text = ''
        rolls20 = []
        if checkbox_toggle.get() == 0:
                for i in range (1):
                        y = random.randint(1,20)
                        rolls20.append(y)
                        if y == 20:
                                sur_text = (f'\t{y} Critical Success!\n')       
                        elif y == 1:
                                sur_text = (f'\t{y} Critical Failure!\n')
                        else:
                                sur_text = (f'\t{y} + 3 = {y + 3}\n')
                return sur_text
        elif checkbox_toggle.get() == 1:
                for i in range (2):
                        y = random.randint(1,20)
                        rolls20.append(y)
                sur_text = (f'\t{rolls20[0]} + 3 = {rolls20[0] + 3}\n\t{rolls20[1]} + 3 = {rolls20[1] + 3}\n')
                return sur_text




def sur():
      result=sur_roll() 
      roll_label.configure(text=(f'\tYour Survival Check is:\n{result}'))


rad_sur = customtkinter.CTkRadioButton(tab1, text="Survival\t+ 3", value=18, variable=radio_var,
                                       fg_color="#8c100d", border_color="#8c100d", hover=False,
                                       command=sur
                                       )
rad_sur.grid(row=8, column=5,pady=10,)




##Individual Dice Rolls with Entry Box and d20 - d4




roll_entry = customtkinter.CTkEntry(tab1, 
                                    width=70, height=30,
                                    fg_color="#8c100d", border_color="#8c100d",
                                    text_color="white")
roll_entry.grid(row=9, column=1, pady=30, sticky='s')

roll_entry_label = customtkinter.CTkLabel(tab1, 
                                          font=('Engravers MT', 14), 
                                          text='# of Rolls',
                                          
                                          )
roll_entry_label.grid(row=9, column=1, pady=30, sticky='n')



def roll20():
        roll20_text = ''
        rolls20 = []   
        number_roll = roll_entry.get()
        if not number_roll:
                number_roll = 1
        else:
                number_roll = int(roll_entry.get())
               
        for i in range(number_roll):
                y = random.randint(1,20)
                rolls20.append(y)
        roll20_text = ""

        for i in range(number_roll):
            roll20_text += f'\t{rolls20[i]}\n'

        if number_roll > 1:
            roll20_text += f'\tTotal = {sum(rolls20)}'  

          
        return roll20_text
        
        
        
def d20_roll():
        result=roll20()
        number_roll = roll_entry.get()
        if not number_roll:
                number_roll = 1
        else:
                number_roll = int(roll_entry.get())

        if number_roll == 1:
                roll_label.configure(text=(f'\tYour d20 roll:\n{result}'))
        else:
                roll_label.configure(text=(f'\tYour d20 rolls:\n{result}'))


d20 = customtkinter.CTkButton(tab1, text="d20",
                               width=12, 
                               height=12,
                              font=('Engravers MT', 14),
                              border_color="black", 
                              fg_color="#8c100d",
                              text_color="white", 
                              hover_color="#4b0303",
                              
                              command=d20_roll)
d20.grid(row=9, column=2, pady=30)


def roll12():
        roll12_text = ''
        rolls12 = []   
        number_roll = roll_entry.get()

        if not number_roll:
                number_roll = 1
        else:
                number_roll = int(roll_entry.get())
               
        for i in range(number_roll):
                y = random.randint(1,12)
                rolls12.append(y)
        roll12_text = ""

        for i in range(number_roll):
            roll12_text += f'\t{rolls12[i]}\n'

        if number_roll > 1:
            roll12_text += f'\tTotal = {sum(rolls12)}'       
        return roll12_text
        
        
        
def d12_roll():
        result=roll12()
        number_roll = roll_entry.get()
        if not number_roll:
                number_roll = 1
        else:
                number_roll = int(roll_entry.get())

        if number_roll == 1:
                roll_label.configure(text=(f'\tYour d12 roll:\n{result}'))
        else:
                roll_label.configure(text=(f'\tYour d12 rolls:\n{result}'))



d12 = customtkinter.CTkButton(tab1, text="d12", width=12, height=12,
                              font=('Engravers MT', 14),border_color="black", fg_color="#8c100d",text_color="white", hover_color="#4b0303",
                              command=d12_roll)
d12.grid(row=9, column=3, pady=30)




def roll10():
        roll10_text = ''
        rolls10 = []   
        number_roll = roll_entry.get()
        if not number_roll:
                number_roll = 1
        else:
                number_roll = int(roll_entry.get())
               
        for i in range(number_roll):
                y = random.randint(1,10)
                rolls10.append(y)
        roll10_text = ""

        for i in range(number_roll):
            roll10_text += f'\t{rolls10[i]}\n'

        if number_roll > 1:
            roll10_text += f'\tTotal = {sum(rolls10)}'      
        return roll10_text
        
        
        
def d10_roll():
        result=roll10()
        number_roll = roll_entry.get()
        if not number_roll:
                number_roll = 1
        else:
                number_roll = int(roll_entry.get())

        if number_roll == 1:
                roll_label.configure(text=(f'\tYour d10 roll:\n{result}'))
        else:
                roll_label.configure(text=(f'\tYour d10 rolls:\n{result}'))


d10 = customtkinter.CTkButton(tab1, text="d10", width=12, height=12,
                              font=('Engravers MT', 14),border_color="black", fg_color="#8c100d",text_color="white", hover_color="#4b0303",
                              command=d10_roll)
d10.grid(row=9, column=4, pady=30, sticky='w')



def roll8():
        roll8_text = ''
        rolls8 = []   
        number_roll = roll_entry.get()
        if not number_roll:
                number_roll = 1
        else:
                number_roll = int(roll_entry.get())
               
        for i in range(number_roll):
                y = random.randint(1,8)
                rolls8.append(y)
        roll8_text = ""

        for i in range(number_roll):
            roll8_text += f'\t{rolls8[i]}\n'

        if number_roll > 1:
            roll8_text += f'\tTotal = {sum(rolls8)}'     
        return roll8_text
        
        
        
def d8_roll():
        result=roll8()
        number_roll = roll_entry.get()
        if not number_roll:
                number_roll = 1
        else:
                number_roll = int(roll_entry.get())

        if number_roll == 1:
                roll_label.configure(text=(f'\tYour d8 roll:\n{result}'))
        else:
                roll_label.configure(text=(f'\tYour d8 rolls:\n{result}'))



d8 = customtkinter.CTkButton(tab1, text="d8", width=12, 
                             height=12,
                             font=('Engravers MT', 14),
                             border_color="black", 
                             fg_color="#8c100d",
                             text_color="white", 
                             hover_color="#4b0303",
                             command=d8_roll)
d8.grid(row=10, column=2, sticky='n')



def roll6():
        roll6_text = ''
        rolls6 = []   
        number_roll = roll_entry.get()
        if not number_roll:
                number_roll = 1
        else:
                number_roll = int(roll_entry.get())
               
        for i in range(number_roll):
                y = random.randint(1,6)
                rolls6.append(y)
        roll6_text = ""

        for i in range(number_roll):
            roll6_text += f'\t{rolls6[i]}\n'

        if number_roll > 1:
            roll6_text += f'\tTotal = {sum(rolls6)}'     
        return roll6_text
        
        
        
def d6_roll():
        result=roll6()
        number_roll = roll_entry.get()
        if not number_roll:
                number_roll = 1
        else:
                number_roll = int(roll_entry.get())

        if number_roll == 1:
                roll_label.configure(text=(f'\tYour d6 roll:\n{result}'))
        else:
                roll_label.configure(text=(f'\tYour d6 rolls:\n{result}'))


d6 = customtkinter.CTkButton(tab1, text="d6", width=12, height=12,
                             font=('Engravers MT', 14),
                             border_color="black", 
                             fg_color="#8c100d",
                             text_color="white", 
                             hover_color="#4b0303",
                             command=d6_roll)
d6.grid(row=10, column=3, sticky='n')                             


def roll4():
        roll4_text = ''
        rolls4 = []   
        number_roll = roll_entry.get()
        if not number_roll:
                number_roll = 1
        else:
                number_roll = int(roll_entry.get())
               
        for i in range(number_roll):
                y = random.randint(1,4)
                rolls4.append(y)
        roll4_text = ""

        for i in range(number_roll):
            roll4_text += f'\t{rolls4[i]}\n'


        if number_roll > 1:
            roll4_text += f'\tTotal = {sum(rolls4)}'
              
        return roll4_text
        
        
        
def d4_roll():
        result=roll4()
        number_roll = roll_entry.get()
        if not number_roll:
                number_roll = 1
        else:
                number_roll = int(roll_entry.get())

        if number_roll == 1:
                roll_label.configure(text=(f'\tYour d4 roll:\n{result}'))
        else:
                roll_label.configure(text=(f'\tYour d4 rolls:\n{result}'))



d4 = customtkinter.CTkButton(tab1, text="d4", width=12, height=12,
                             font=('Engravers MT', 14),
                             border_color="black", 
                             fg_color="#8c100d",
                             text_color="white", 
                             hover_color="#4b0303",
                             command=d4_roll,)
d4.grid(row=10, column=4, sticky='nw')












##Tab2 - Spells


tab2.grid_columnconfigure(1, weight=0)  
tab2.grid_columnconfigure(5, weight=1)  





##Labels on right side of screen for Spell Information

spell_range_label = customtkinter.CTkLabel(tab2, text='',
                                            font=('Engravers MT', 14),
                                            wraplength=500,
                                            anchor='n',
                                            width=400)
spell_range_label.grid(row=2, column=5, pady=15)

spell_hit_label = customtkinter.CTkLabel(tab2, text='',
                                            font=('Engravers MT', 14),
                                            wraplength=500,
                                            anchor='n',
                                            width=400)
spell_hit_label.grid(row=4, column=5, pady=15)

spell_descr_label = customtkinter.CTkLabel(tab2, text='',
                                          font=('Engravers MT', 14),
                                          wraplength=500,
                                          anchor='w',
                                          width=300
                                          )
spell_descr_label.grid(row=6, column=5, pady=15,)


spell_damage_label = customtkinter.CTkLabel(tab2, text='',
                                            font=('Engravers MT', 14),
                                            wraplength=500,
                                            anchor='n',
                                            width=400)
spell_damage_label.grid(row=8, column=5, pady=15)



spell_roll_button = customtkinter.CTkButton(tab2, text='',
                                           font=('Engravers MT', 14),
                                           command='',
                                           border_color="black", 
                                           fg_color="#8c100d",
                                           text_color="white", 
                                           hover_color="#4b0303")
spell_roll_button.grid(row=10, column=5, pady=15)



spell_output_label = customtkinter.CTkLabel(tab2, text='',font=('Engravers MT', 20)
                                            )
spell_output_label.grid(row=12, column=5, pady=15, sticky='n', rowspan=10)



##Cantrips Label, Buttons, and Functions

cantrip_label = customtkinter.CTkLabel(tab2, text="Cantrips", font=('Engravers MT', 20))
cantrip_label.grid(row=1, column=1, pady=15, rowspan=1,)


def firebolt():
        firebolt_str = ''
        fb_to_hit = []
        firebolt_roll = []
        for i in range(2):
                y = random.randint(1, 10)
                firebolt_roll.append(y)
        for i in range(1):
                y = random.randint(1, 20)
                fb_to_hit.append(y)

        firebolt_str = (f'To hit: {fb_to_hit[0]} + 8\nTotal: {fb_to_hit[0] + 8}\n\nYour Fire Bolt damage is:\n{firebolt_roll[0]}\n{firebolt_roll[1]}\nTotal: {sum(firebolt_roll)}')
        return firebolt_str

def fb():
        result = firebolt()
        spell_output_label.configure(text=result)


def poison_spray():
        poison_str = ''
        poison_roll = []
        for i in range(2):
                y = random.randint(1, 12)
                poison_roll.append(y)
        poison_str = (f"Your Poison Spray damage is:\n\n{poison_roll[0]}\n{poison_roll[1]}\n\nTotal: {sum(poison_roll)}")
        return poison_str

def ps():
        result = poison_spray()
        spell_output_label.configure(text=result)

def ctrips(values):
    description = cantrip_descriptions.get(values)
    damage = cantrip_damages.get(values)
    range = cantrip_ranges.get(values)
    hit = cantrip_hit.get(values)
    roll = cantrip_roll.get(values)
    spell_descr_label.configure(anchor="center", text=description)
    spell_damage_label.configure(anchor="center", text=damage)
    spell_range_label.configure(anchor="center", text=range)
    spell_hit_label.configure(anchor="center", text=hit)
    spell_roll_button.configure(text=roll)
    spell_output_label.configure(text='')
    lv1_button.set(None)
    lv2_button.set(None)
    lv3_button.set(None)
    if values == 'Fire Bolt':
        spell_roll_button.configure(command=fb)
    elif values == 'Poison Spray':
        spell_roll_button.configure(command=ps)
    

            



cantrips = ['Fire Bolt', 'Mage Hand', 'Mending', 'Message', 'Poison Spray']

cantrip_descriptions = {
    'Fire Bolt': 'You hurl a mote of fire at a target!\n',
    'Mage Hand': 'A spectral hand appears, which can manipulate objects.',
    'Mending': 'You repair a break or tear in an object.',
    'Message': 'You whisper a message to someone, and they can reply.',
    'Poison Spray': 'You unleash a puff of noxious gas toward a creature.'
    }

cantrip_damages = {
        'Fire Bolt': 'Make a ranged attack. On a hit,'
                      'target takes 2d10 Fire damage',

        'Mage Hand': 'You can use the hand to manipulate '
                     'an object.\nThe hand can\'t attack, '
                     'activate magic items, or carry more than 10 pounds.',

        'Mending': 'This spell repairs a single break or '
                    'tear in an object you touch. No larger than 1 foot',
                    
        'Message': 'The target (and only the target) hears '
                    'the message and can reply in a whisper that only you can hear.',

        'Poison Spray': 'The creature must succeed on a Constitution '
                        'saving throw or take\n2d12 poison damage.'
        
}

cantrip_ranges = {
        'Fire Bolt': 'Range:\n120 ft.',
        'Mage Hand': 'Range:\n30 ft.',
        'Mending': 'Range:\nTouch',
        'Message': 'Range:120 ft.',
        'Poison Spray': 'Range:\n10 ft.'
}

cantrip_hit = {
        'Fire Bolt': 'To Hit\n+ 8',
        'Mage Hand': 'To Hit:\n-',
        'Mending': 'To Hit:\n-',
        'Message': 'To Hit:\n-',
        'Poison Spray': 'To Hit\nCON 16'
}

cantrip_roll = {
        'Fire Bolt': '2d10',
        'Mage Hand': '',
        'Mending': '',
        'Message': '',
        'Poison Spray': '2d12'
}

cantrip_button = customtkinter.CTkSegmentedButton(tab2, values=cantrips,
                                                  command=ctrips,
                                                  font=('Engravers MT', 14),
                                                  selected_color="#8c100d",
                                                  selected_hover_color="#8c100d",
                                                  unselected_hover_color="#520907",
                                                  unselected_color="#520907", 
                                                  fg_color="#8c100d",
                                                  text_color="white", 
                                                  
                                                  )
cantrip_button.grid(row=2, column=1, pady=20)




##Level 1 Spells Label, Buttons, and Functions

lv1_label = customtkinter.CTkLabel(tab2, text="Level 1", font=('Engravers MT', 20))
lv1_label.grid(row=4, column=1, pady=15)


def magic_missile_1():
        mm1_str = ''
        mm1_rolls = []
        for i in range(3):
                y = random.randint(1,4)
                mm1_rolls.append(y)
        mm1_str = (f"Your Magic Missile damage is:\n\n{mm1_rolls[0]} + 1\n{mm1_rolls[1]} + 1\n{mm1_rolls[2]} + 1\n\nTotal: {sum(mm1_rolls) + 3}")
        return mm1_str


def mm1():

    result = magic_missile_1()
    spell_output_label.configure(text=result)

    if spell_slots_1_1.get() == 0:
            spell_slots_1_1.select()
    elif spell_slots_1_2.get() == 0:
            spell_slots_1_2.select()
    elif spell_slots_1_3.get() == 0:
            spell_slots_1_3.select()
    elif spell_slots_1_4.get() == 0:
            spell_slots_1_4.select()
    elif all(slot.get() == 1 for slot in [spell_slots_1_1, spell_slots_1_2, spell_slots_1_3, spell_slots_1_4]):
            spell_output_label.configure(text='You are out of Level 1 Spell Slots')
            
    

def lv1(values):
        descriptions = lv1_descriptions.get(values)
        damage = lv1_damages.get(values)
        range = lv1_ranges.get(values)
        hit = lv1_hit.get(values)
        roll = lv1_roll.get(values)
        spell_descr_label.configure(anchor="center", text=descriptions)
        spell_damage_label.configure(anchor="center", text=damage)
        spell_range_label.configure(anchor="center", text=range)
        spell_hit_label.configure(anchor="center", text=hit)
        spell_roll_button.configure(text=roll)
        spell_output_label.configure(text='')
        cantrip_button.set(None)
        lv2_button.set(None)
        lv3_button.set(None)
        if values == 'Magic Missile':
                spell_roll_button.configure(command=mm1)
        
                
        

lv1_spells = ['Magic Missile']

lv1_descriptions = {
        'Magic Missile': 'You create three glowing darts of magical force.'
                         '\nEach dart hits a creature of your choice that you can see within range.'

}

lv1_damages = {
        'Magic Missile': 'A dart deals 1d4 + 1 force damage to its target.'

}

lv1_ranges = {
        'Magic Missile': 'Range:\n120 ft.'
}

lv1_hit = {
        'Magic Missile': 'To Hit:\n-'
}


lv1_roll = {
        'Magic Missile': '1d4 + 1'
}


lv1_button = customtkinter.CTkSegmentedButton(tab2, values=lv1_spells,
                                                  command=lv1,
                                                  font=('Engravers MT', 14),
                                                  selected_color="#8c100d",
                                                  selected_hover_color="#8c100d",
                                                  unselected_hover_color="#520907",
                                                  unselected_color="#520907", 
                                                  fg_color="#8c100d",
                                                  text_color="white",
                                                  )
lv1_button.grid(row=5, column=1,)



##level 2 Spells Label, Buttons, and Functions


lv2_label = customtkinter.CTkLabel(tab2, text="Level 2", font=('Engravers MT', 20))
lv2_label.grid(row=7, column=1, pady=15,)


def a_scorcher2():
        scorcher2_str = ''
        scorcher2_rolls = []
        for i in range(3):
                y = random.randint(1, 8)
                scorcher2_rolls.append(y)
        scorcher2_str = (f"Your Aganazzar's Scorcher damage is:\n\n{scorcher2_rolls[0]}\n{scorcher2_rolls[1]}\n{scorcher2_rolls[2]}\n\nTotal: {sum(scorcher2_rolls)}")
        return scorcher2_str


def ag2():
        result = a_scorcher2()
        spell_output_label.configure(text=result)
        if spell_slots_2_1.get() == 0:
                spell_slots_2_1.select()
        elif spell_slots_2_2.get() == 0:
                spell_slots_2_2.select()
        elif spell_slots_2_3.get() == 0:
                spell_slots_2_3.select()
        elif all(slot.get() == 1 for slot in [spell_slots_2_1, spell_slots_2_2, spell_slots_2_3]):
                spell_output_label.configure(text='You are out of Level 2 Spell Slots')



def magic_missile_2():
        mm2_str = ''
        mm2_rolls = []
        for i in range(4):
                y = random.randint(1,4)
                mm2_rolls.append(y)
        mm2_str = (f"Your Magic Missile damage is:\n\n{mm2_rolls[0]} + 1\t{mm2_rolls[1]} + 1\n{mm2_rolls[2]} + 1\t{mm2_rolls[3]} + 1\n\nTotal: {sum(mm2_rolls) + 4}")
        return mm2_str

def mm2():
        result = magic_missile_2()
        spell_output_label.configure(text=result)
        if spell_slots_2_1.get() == 0:
                spell_slots_2_1.select()
        elif spell_slots_2_2.get() == 0:
                spell_slots_2_2.select()
        elif spell_slots_2_3.get() == 0:
                spell_slots_2_3.select()
        elif all(slot.get() == 1 for slot in [spell_slots_2_1, spell_slots_2_2, spell_slots_2_3]):
                spell_output_label.configure(text='You are out of Level 2 Spell Slots')


def shatter2():
        shatter2_str = ''
        shatter2_rolls = []
        for i in range(3):
                y = random.randint(1, 8)
                shatter2_rolls.append(y)
        shatter2_str = (f"Your Shatter damage is:\n\n{shatter2_rolls[0]}\n{shatter2_rolls[1]}\n{shatter2_rolls[2]}\n\nTotal: {sum(shatter2_rolls)}")
        return shatter2_str

def shat2():
        result = shatter2()
        spell_output_label.configure(text=result)
        if spell_slots_2_1.get() == 0:
                spell_slots_2_1.select()
        elif spell_slots_2_2.get() == 0:
                spell_slots_2_2.select()
        elif spell_slots_2_3.get() == 0:
                spell_slots_2_3.select()
        elif all(slot.get() == 1 for slot in [spell_slots_2_1, spell_slots_2_2, spell_slots_2_3]):
                spell_output_label.configure(text='You are out of Level 2 Spell Slots')

def snowball2():
        snowball2_str = ''
        snowball2_rolls = []
        for i in range(3):
                y = random.randint(1, 6)
                snowball2_rolls.append(y)
        snowball2_str = (f"Your Snilloc's Snowball Swarm damage is:\n\n{snowball2_rolls[0]}\n{snowball2_rolls[1]}\n{snowball2_rolls[2]}\n\nTotal: {sum(snowball2_rolls)}")
        return snowball2_str

def sss2():
        result = snowball2()
        spell_output_label.configure(text=result)
        if spell_slots_2_1.get() == 0:
                spell_slots_2_1.select()
        elif spell_slots_2_2.get() == 0:
                spell_slots_2_2.select()
        elif spell_slots_2_3.get() == 0:
                spell_slots_2_3.select()
        elif all(slot.get() == 1 for slot in [spell_slots_2_1, spell_slots_2_2, spell_slots_2_3]):
                spell_output_label.configure(text='You are out of Level 2 Spell Slots')



def lv2(values):
        description = lv2_descriptions.get(values)
        damage = lv2_damages.get(values)
        range = lv2_ranges.get(values)
        hit = lv2_hit.get(values)
        roll = lv2_roll.get(values)
        spell_descr_label.configure(anchor="center", text=description)
        spell_damage_label.configure(anchor="center", text=damage)
        spell_range_label.configure(anchor="center", text=range)
        spell_hit_label.configure(anchor="center", text=hit)
        spell_roll_button.configure(text=roll)
        spell_output_label.configure(text='')
        cantrip_button.set(None)
        lv1_button.set(None)
        lv3_button.set(None)
        if values == 'Aganazzar\'s\nScorcher':
                spell_roll_button.configure(command=ag2)
        if values == 'Magic\nMissile':
                spell_roll_button.configure(command=mm2)
        if values == 'Shatter':
                spell_roll_button.configure(command=shat2)
        if values == 'Snilloc\'s\nSnowball Swarm':
                spell_roll_button.configure(command=sss2)


lv2_spells = ['Aganazzar\'s\nScorcher', 'Magic\nMissile', 'Shatter', 'Snilloc\'s\nSnowball Swarm', 'Suggestion']


lv2_descriptions = {
        'Aganazzar\'s\nScorcher': 'A line of roaring flame 30 feet long and 5 feet wide emanates from you in a direction you choose.',
        'Magic\nMissile': 'You create four glowing darts of magical force.\nEach dart hits a creature of your choice that you can see within range.',
        'Shatter': 'A sudden loud ringing noise, painfully intense, erupts from a point of your choice within range.',
        'Snilloc\'s\nSnowball Swarm': 'A flurry of magic snowballs erupts from a point you choose within range.',
        'Suggestion': 'You suggest a course of activity (a sentence or two) and magically influence a creature you can see within range that can hear and understand you.'


}


lv2_damages = {
        'Aganazzar\'s\nScorcher': '3d8 fire damage on a failed save,\nor half as much damage on a successful one.',
        'Magic\nMissile': 'A dart deals 1d4 + 1 force damage to its target.',
        'Shatter': 'A creature takes 3d8 thunder damage on a failed save, or half as much damage on a successful one.',
        'Snilloc\'s\nSnowball Swarm': 'A creature takes 3d6 cold damage on a failed save, or half as much damage on a successful one.',
        'Suggestion': 'The target must make a Wisdom saving throw. On a failed save, it pursues the course of action you described to the best of its ability.'
}


lv2_ranges = {
        'Aganazzar\'s\nScorcher': 'Range:\n30 ft.',
        'Magic\nMissile': 'Range:\n120 ft.',
        'Shatter': 'Range:\n60 ft.',
        'Snilloc\'s\nSnowball Swarm': 'Range:\n90 ft.',
        'Suggestion': 'Range:\n30 ft.'
}

lv2_hit = {
        'Aganazzar\'s\nScorcher': 'To Hit:\nDEX 16',
        'Magic\nMissile': 'To Hit:\n-',
        'Shatter': 'To Hit:\nCON 16',
        'Snilloc\'s\nSnowball Swarm': 'To Hit:\nDEX 16',
        'Suggestion': 'To Hit:\nWIS 16'
}


lv2_roll = {
        'Aganazzar\'s\nScorcher': '3d8',
        'Magic\nMissile': '1d4 + 1',
        'Shatter': '3d8',
        'Snilloc\'s\nSnowball Swarm': '3d6',
        'Suggestion': ''
}

lv2_button = customtkinter.CTkSegmentedButton(tab2, values=lv2_spells,
                                                  command=lv2,
                                                  font=('Engravers MT', 14),
                                                  selected_color="#8c100d",
                                                  selected_hover_color="#8c100d",
                                                  unselected_hover_color="#520907",
                                                  unselected_color="#520907", 
                                                  fg_color="#8c100d",
                                                  text_color="white")
lv2_button.grid(row=8, column=1, pady=15)




##Level 3 Spells, Label, Buttons, and Functions

lv3_label = customtkinter.CTkLabel(tab2, text="Level 3", font=('Engravers MT', 20))
lv3_label.grid(row=10, column=1, pady=15,)


def a_scorcher3():
        scorcher3_str = ''
        scorcher3_rolls = []
        for i in range(4):
                y = random.randint(1, 8)
                scorcher3_rolls.append(y)
        scorcher3_str = (f"Your Aganazzar's Scorcher damage is:\n\n{scorcher3_rolls[0]}\t{scorcher3_rolls[1]}\n{scorcher3_rolls[2]}\t{scorcher3_rolls[3]}\n\nTotal: {sum(scorcher3_rolls)}")
        return scorcher3_str

def ag3():
        result = a_scorcher3()
        spell_output_label.configure(text=result)
        if spell_slots_3_1.get() == 0:
                spell_slots_3_1.select()
        elif spell_slots_3_2.get() == 0:
                spell_slots_3_2.select()
        elif all(slot.get() == 1 for slot in [spell_slots_2_1, spell_slots_2_2, spell_slots_2_3]):
                spell_output_label.configure(text='You are out of Level 3 Spell Slots') 

     


def fireball3():
        fireball3_str = ''
        fireball3_rolls = []
        for i in range(8):
                y = random.randint(1, 6)
                fireball3_rolls.append(y)
        fireball3_str = (f"Your Fireball damage is:\n\n{fireball3_rolls[0]}\t{fireball3_rolls[1]}\n{fireball3_rolls[2]}\t{fireball3_rolls[3]}\n"
                         f"{fireball3_rolls[4]}\t{fireball3_rolls[5]}\n{fireball3_rolls[6]}\t{fireball3_rolls[7]}\nTotal: {sum(fireball3_rolls)}")
        return fireball3_str

def fb3():
        result = fireball3()
        spell_output_label.configure(text=result)
        if spell_slots_3_1.get() == 0:
                spell_slots_3_1.select()
        elif spell_slots_3_2.get() == 0:
                spell_slots_3_2.select()
        elif all(slot.get() == 1 for slot in [spell_slots_2_1, spell_slots_2_2, spell_slots_2_3]):
                spell_output_label.configure(text='You are out of Level 3 Spell Slots')   

def magic_missile_3():
        mm3_str = ''
        mm3_rolls = []
        for i in range(5):
                y = random.randint(1,4)
                mm3_rolls.append(y)
        mm3_str = (f"Your Magic Missile damage is:\n\n{mm3_rolls[0]} + 1\t{mm3_rolls[1]} + 1\n{mm3_rolls[2]} + 1\t{mm3_rolls[3]} + 1\n{mm3_rolls[4]} + 1\n\nTotal: {sum(mm3_rolls) + 5}")
        return mm3_str

def mm3():
        result = magic_missile_3()
        spell_output_label.configure(text=result)
        if spell_slots_3_1.get() == 0:
                spell_slots_3_1.select()
        elif spell_slots_3_2.get() == 0:
                spell_slots_3_2.select()
        elif all(slot.get() == 1 for slot in [spell_slots_2_1, spell_slots_2_2, spell_slots_2_3]):
                spell_output_label.configure(text='You are out of Level 3 Spell Slots')  

def shatter3():
        shatter3_str = ''
        shatter3_rolls = []
        for i in range(4):
                y = random.randint(1, 8)
                shatter3_rolls.append(y)
        shatter3_str = (f"Your Shatter damage is:\n\n{shatter3_rolls[0]}\t{shatter3_rolls[1]}\n{shatter3_rolls[2]}\t{shatter3_rolls[3]}\n\nTotal: {sum(shatter3_rolls)}")
        return shatter3_str

def shat3():
        result = shatter3()
        spell_output_label.configure(text=result)
        if spell_slots_3_1.get() == 0:
                spell_slots_3_1.select()
        elif spell_slots_3_2.get() == 0:
                spell_slots_3_2.select()
        elif all(slot.get() == 1 for slot in [spell_slots_2_1, spell_slots_2_2, spell_slots_2_3]):
                spell_output_label.configure(text='You are out of Level 3 Spell Slots')   

def snowball3():
        snowball3_str = ''
        snowball3_rolls = []
        for i in range(4):
                y = random.randint(1, 6)
                snowball3_rolls.append(y)
        snowball3_str = (f"Your Snilloc's Snowball Swarm damage is:\n\n{snowball3_rolls[0]}\t{snowball3_rolls[1]}\n{snowball3_rolls[2]}\t{snowball3_rolls[3]}\n\nTotal: {sum(snowball3_rolls)}")
        return snowball3_str

def sss3():
        result = snowball3()
        spell_output_label.configure(text=result)
        if spell_slots_3_1.get() == 0:
                spell_slots_3_1.select()
        elif spell_slots_3_2.get() == 0:
                spell_slots_3_2.select()
        elif all(slot.get() == 1 for slot in [spell_slots_2_1, spell_slots_2_2, spell_slots_2_3]):
                spell_output_label.configure(text='You are out of Level 3 Spell Slots')   

def lv3(values):
        description = lv3_descriptions.get(values)
        damage = lv3_damages.get(values)
        range = lv3_ranges.get(values)
        hit = lv3_hits.get(values)
        roll = lv3_roll.get(values)
        spell_descr_label.configure(anchor="center", text=description)
        spell_damage_label.configure(anchor="center", text=damage)
        spell_range_label.configure(anchor="center", text=range)
        spell_hit_label.configure(anchor="center", text=hit)
        spell_roll_button.configure(text=roll)
        spell_output_label.configure(text='')
        cantrip_button.set(None)
        lv1_button.set(None)
        lv2_button.set(None)
        if values == 'Aganazzar\'s\nScorcher':
                spell_roll_button.configure(command=ag3)
        if values == 'Fireball':
                spell_roll_button.configure(command=fb3)
        if values == 'Magic\nMissile':
                spell_roll_button.configure(command=mm3)
        if values == 'Shatter':
                spell_roll_button.configure(command=shat3)
        if values == 'Snilloc\'s\nSnowball Swarm':
                spell_roll_button.configure(command=sss3)


lv3_spells = ['Aganazzar\'s\nScorcher', 'Fireball', 'Magic\nMissile', 'Shatter', 'Snilloc\'s\nSnowball Swarm']


lv3_descriptions = {
        'Aganazzar\'s\nScorcher': 'A line of roaring flame 30 feet long and 5 feet wide emanates from you in a direction you choose.',
        'Fireball': 'A bright streak flashes from your pointing finger to a point you choose within range and then blossoms with a low roar into an explosion of flame.',
        'Magic\nMissile': 'You create five glowing darts of magical force.\nEach dart hits a creature of your choice that you can see within range. ',
        'Shatter': 'A sudden loud ringing noise, painfully intense, erupts from a point of your choice within range.',
        'Snilloc\'s\nSnowball Swarm': 'A flurry of magic snowballs erupts from a point you choose within range.'
}


lv3_damages = {
        'Aganazzar\'s\nScorcher': '4d8 fire damage on a failed save, or half as much damage on a successful one.',
        'Fireball': 'A target takes 8d6 fire damage on a failed save, or half as much damage on a successful one.',
        'Magic\nMissile': 'A dart deals 1d4 + 1 force damage to its target.',
        'Shatter': 'A creature takes 4d8 thunder damage on a failed save, or half as much damage on a successful one.',
        'Snilloc\'s\nSnowball Swarm': 'A creature takes 4d6 cold damage on a failed save, or half as much damage on a successful one.',
        
}


lv3_ranges = {
        'Aganazzar\'s\nScorcher': 'Range:\n30 ft.',
        'Fireball': 'Range:\n150 ft.',
        'Magic\nMissile': 'Range:\n120 ft.',
        'Shatter': 'Range:\n60 ft.',
        'Snilloc\'s\nSnowball Swarm': 'Range:\n90 ft.',
        
}

lv3_hits = {
        'Aganazzar\'s\nScorcher': 'To Hit:\nDEX 16',
        'Fireball': 'To Hit:\nDEX 16',
        'Magic\nMissile': 'To Hit:\n-',
        'Shatter': 'To Hit:\nCON 16',
        'Snilloc\'s\nSnowball Swarm': 'To Hit:\nDEX 16',
        
}


lv3_roll = {
        'Aganazzar\'s\nScorcher': '4d8',
        'Fireball': '8d6',
        'Magic\nMissile': '1d4 + 1',
        'Shatter': '4d8',
        'Snilloc\'s\nSnowball Swarm': '4d6',
        
}

lv3_button = customtkinter.CTkSegmentedButton(tab2, values=lv3_spells,
                                                  command=lv3,
                                                  font=('Engravers MT', 14),
                                                  selected_color="#8c100d",
                                                  selected_hover_color="#8c100d",
                                                  unselected_hover_color="#520907",
                                                  unselected_color="#520907", 
                                                  fg_color="#8c100d",
                                                  text_color="white",)
lv3_button.grid(row=11, column=1, pady=15)




#Spell Slot Check Boxes and Labels

spell_slots_1_1 = customtkinter.CTkCheckBox(tab2, text='Lvl 1',border_color="#8c100d", 
                                         fg_color="#8c100d", hover_color="#8c100d",
                                         variable=checkbox_toggle, onvalue=1, offvalue=0,
                                         )
spell_slots_1_1.grid(row=13, column=1, pady=(0,5), sticky='w', padx=15)

spell_slots_1_2 = customtkinter.CTkCheckBox(tab2, text='',border_color="#8c100d", 
                                         fg_color="#8c100d", hover_color="#8c100d")
spell_slots_1_2.grid(row=14, column=1, pady=(0,5), sticky='w', padx=15)

spell_slots_1_3 = customtkinter.CTkCheckBox(tab2, text='',border_color="#8c100d", 
                                         fg_color="#8c100d", hover_color="#8c100d")
spell_slots_1_3.grid(row=15, column=1, pady=(0,5), sticky='w', padx=15)

spell_slots_1_4 = customtkinter.CTkCheckBox(tab2, text='',border_color="#8c100d",
                                          fg_color="#8c100d", hover_color="#8c100d")
spell_slots_1_4.grid(row=16, column=1, pady=(0,5), sticky='w', padx=15)




spell_slots_2_1 = customtkinter.CTkCheckBox(tab2, text='Lvl 2',border_color="#8c100d", 
                                         fg_color="#8c100d", hover_color="#8c100d")
spell_slots_2_1.grid(row=13, column=1, pady=(0,5))

spell_slots_2_2 = customtkinter.CTkCheckBox(tab2, text='',border_color="#8c100d", 
                                         fg_color="#8c100d", hover_color="#8c100d")
spell_slots_2_2.grid(row=14, column=1, pady=(0,5), padx=15)

spell_slots_2_3 = customtkinter.CTkCheckBox(tab2, text='',border_color="#8c100d", 
                                         fg_color="#8c100d", hover_color="#8c100d")
spell_slots_2_3.grid(row=15, column=1, pady=(0,5), padx=15)




spell_slots_3_1 = customtkinter.CTkCheckBox(tab2, text='Lvl 3',border_color="#8c100d", 
                                         fg_color="#8c100d", hover_color="#8c100d")
spell_slots_3_1.grid(row=13, column=1, pady=(0,5), sticky='e', padx=15)

spell_slots_3_2 = customtkinter.CTkCheckBox(tab2, text='',border_color="#8c100d", 
                                         fg_color="#8c100d", hover_color="#8c100d")
spell_slots_3_2.grid(row=14, column=1, pady=(0,5), sticky='e', padx=15)








#Tab3 - Metamagic

tab3.grid_columnconfigure(2, weight=0)  
tab3.grid_columnconfigure(5, weight=1) 




sorcery_points_label = customtkinter.CTkLabel(tab3, text='Sorcery\nPoints', font=('Engravers MT', 20))
sorcery_points_label.grid(row=1, column=2, pady=(15,0), rowspan=1, columnspan=1, sticky='w')



sorcery_point_1 = customtkinter.CTkCheckBox(tab3, text='', border_color="#8c100d", 
                                         fg_color="#8c100d", hover_color="#8c100d")
sorcery_point_1.grid(row=2, column=2, pady=(0,5), sticky='es')


sorcery_point_2 = customtkinter.CTkCheckBox(tab3, text='', border_color="#8c100d", 
                                         fg_color="#8c100d", hover_color="#8c100d")
sorcery_point_2.grid(row=3, column=2, pady=(0,5), sticky='en')

sorcery_point_3 = customtkinter.CTkCheckBox(tab3, text='', border_color="#8c100d", 
                                         fg_color="#8c100d", hover_color="#8c100d")
sorcery_point_3.grid(row=4, column=2, pady=(0,5), sticky='en')


sorcery_point_4 = customtkinter.CTkCheckBox(tab3, text='', border_color="#8c100d", 
                                         fg_color="#8c100d", hover_color="#8c100d")
sorcery_point_4.grid(row=5, column=2, pady=(0,5), sticky='en')

sorcery_point_5 = customtkinter.CTkCheckBox(tab3, text='', border_color="#8c100d", 
                                         fg_color="#8c100d", hover_color="#8c100d")
sorcery_point_5.grid(row=6, column=2, pady=(0,5), sticky='en')


sorcery_point_6 = customtkinter.CTkCheckBox(tab3, text='', border_color="#8c100d", 
                                         fg_color="#8c100d", hover_color="#8c100d")
sorcery_point_6.grid(row=7, column=2, pady=(0,5), sticky='en')




meta_spells = ['Careful', 'Quickened', 'Distant', 'Empowered']

meta_descriptions = {
        'Careful': 'Allow up to 5 creatures to automatically succeed on the\n saving throw of a spell you cast',
        'Quickened': 'Change casting time of spell from Action to Bonus Action',
        'Distant': 'Double Spell Distance',
        'Empowered': 'Reroll a number of damage dice up to your charisma modifyer.\nMust use new rolls'

}


meta_points = {
        'Careful': 'Sorcery Points: 1',
        'Quickened': 'Sorcery Points: 2',
        'Distant': 'Sorcery Points: 1',
        'Empowered': 'Sorcery Points: 1'

}
def meta(values):
        description = meta_descriptions.get(values)
        points = meta_points.get(values)
        meta_desc_label.configure(text=description)
        meta_points_label.configure(text=points)
        meta_button.configure(text=f'Cast {values} Spell')

meta_desc_label = customtkinter.CTkLabel(tab3, text='',
                                            font=('Engravers MT', 14),
                                            )
meta_desc_label.grid(row=5, column=5, padx=220)


meta_points_label = customtkinter.CTkLabel(tab3, text='',
                                            font=('Engravers MT', 14),
                                            )
meta_points_label.grid(row=7, column=5,pady=20, padx=220)


meta_button = customtkinter.CTkButton(tab3, text='',
                                           font=('Engravers MT', 14),
                                           command='',
                                           border_color="black", 
                                           fg_color="#8c100d",
                                           text_color="white", 
                                           hover_color="#4b0303")
meta_button.grid(row=12, column=5,pady=40,padx=220)
        

metamagic_label = customtkinter.CTkLabel(tab3, text='Metamagic Spells', font=('Engravers MT', 20))
metamagic_label.grid(row=1, column=5, pady=(20,0))

metamagic_buttons = customtkinter.CTkSegmentedButton(tab3, values=meta_spells,
                                                  command=meta,
                                                  font=('Engravers MT', 14),
                                                  selected_color="#8c100d",
                                                  selected_hover_color="#8c100d",
                                                  unselected_hover_color="#520907",
                                                  unselected_color="#520907", 
                                                  fg_color="#8c100d",
                                                  text_color="white", 
                                                  
                                                  )
metamagic_buttons.grid(row=2, column=5, pady=20, padx=170)





##Tab4 - Inventory

inventory = customtkinter.CTkTextbox(tab4, width=850, height=600, font=('Engravers MT', 18))
inventory.grid(row=2, column=1, padx=50, pady=50)



data_file = '/Users/frater47/Documents/cyberSec/fall2024/programming/python/personal_projects/dnd_dice_roller/inventory.txt'



def save_data():
        with open(data_file, 'w') as file:
                file.write(inventory.get("1.0", "end-1c"))

def load_data():
        if os.path.exists(data_file):
                with open(data_file, 'r') as file:
                        data = file.read()
                        inventory.insert("1.0", data)


















load_data()
root.protocol("WM_DELETE_WINDOW", lambda: [save_data(), root.destroy()])
tab1.mainloop()