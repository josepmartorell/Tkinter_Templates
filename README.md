# Tkinter_Templates :clown_face:
This project is based on the serialization of files based on the Tkinter framework which, based on a preliminary file, publishes a following file, increasing its complexity and usefulness. Each file is listed in the same file name (template1, template2, template3 ...) so that individually they can be useful as templates for different projects.

## Description

I must say that my interest in this wonderful miniframework called Tkinter (_**better known as the surprise Kinder Eggs**_), started with a project that had in common with the teachings of the Cisco Networking Academy.
Said GitHub project to which I have marked the star is dedicated to Cisco Systems APIC-EM drivers, I have the same drivers but this one unlike mine incorporates Tkinter. I think it's from a German engineer if I'm not mistaken: [click right here to see it](https://github.com/CiscoDevNet/APIC-EM-REST-API-GUI-based-demos). 
I really liked the idea of incorporating an interface to a networking program, which as we know usually works normally with the command line. So I started creating a small collection of templates Tk or Tkk or Tkkk or Tkkkk or ... :nauseated_face: only to obtain guidelines and to be able to flexibilize and share knowledge with you if you decide to cooperate in my templates project, where you are welcome.
  
Here is an example of template number 10, which is a small data entry interface of an IBAN validator, based on my first GitHub project, which had no interface:  [click right here if you are curious to see it](https://github.com/josepmartorell/IBAN_Checker). 
  
```javascript
import tkinter as tkk
import json

with open('iban.json', 'r') as json_file:
    data = json.load(json_file)


class Application(tkk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.check = tkk.Button(self)
        self.exit = tkk.Button(self)
        self.parameter = tkk.StringVar()
        self.entry = tkk.Entry(textvariable=self.parameter)
        self.entry.pack(side=tkk.RIGHT)
        self.pack(side="left")
        self.create_widgets()
        self.length = 0
        self.country = ""
        master.title("IBAN_Checker")
        master.configure(background="white")
        master.geometry("600x64")

    def create_widgets(self):
        self.check.place(x=0, y=0)
        self.check["text"] = "CHECK IBAN NUMBER"
        self.check["command"] = self.check_iban
        self.check["fg"] = "red"
        self.check.pack(side="top")
        self.exit.config(text="exit iban validator", command=self.master.destroy)
        self.exit.pack(side="left", expand=50, fill="x")
        self.entry.pack(side="right", ipadx=131, fill="x")

    def check_iban(self):
        iban = self.parameter.get()
        # let's eliminate the empty spaces
        iban = iban.replace(' ', '')
        # let's control the input data type
        if not iban.isalnum():
            print("Invalid characters inside IBAN - sorry!")
        # (step 1) Check that the total IBAN length is correct
        code2 = (iban[0:2].upper())
        length2 = self.registry_length(code2)
        name_country = self.registry_country(code2)

        if not code2.isalpha():
            print("Invalid country code")
        elif len(iban) < int(length2):
            print("IBAN too short")
            print("the length for ", name_country, " IBAN is: ", length2)
        elif len(iban) > int(length2):
            print("IBAN too long")
            print("the length for ", name_country, " IBAN is: ", length2)
        # (step 2) Move the four initial characters to the end of the string
        else:
            iban_rearranged = (iban[4:] + iban[0:4]).upper()
            # (step 3) Replace each letter in the string with two digits, thereby expanding the string, where A = 10,
            # B = 11 .. Z = 35;
            iban2 = ''
            for ch in iban_rearranged:
                if ch.isdigit():
                    iban2 += ch
                else:
                    iban2 += str(10 + ord(ch) - ord('A'))
            # (step 4) Interpret the string as a decimal integer and compute the remainder of that number on division
            # by 97; If the remainder is 1, the check digit test is passed and the IBAN might be valid.
            ibann = int(iban2)
            if ibann % 97 == 1:
                print("Seems legit!")
                print('\nIban number: ', self.iban_formatted(iban).upper())
            else:
                print("Fake account!")
                print('\nIban number: ', self.iban_formatted(iban).upper())

    def registry_length(self, code):
        for p in data['values']:
            if p['code'] == code:
                self.length = p['length']
        return self.length

    def registry_country(self, code):
        for p in data['values']:
            if p['code'] == code:
                self.country = p['country']
        return self.country

    def iban_formatted(self, iban):
        return ' '.join(iban[i:i + 4] for i in range(0, len(iban), 4))


if __name__ == '__main__':
    root = tkk.Tk()
    app = Application(master=root)
    app.mainloop()
```
Ideal as a starting point for a bank Api!




