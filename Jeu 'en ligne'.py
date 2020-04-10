import tkinter as tk    # Imports
import random

accueil = tk.Tk()                       # Mise en place de la première fenêtre
accueil.geometry("500x500+350+50")
accueil.config(bg="lightblue")
tk.Label(accueil, text="Accueil", bg="lightblue", font=("Arial",20)).place(anchor="n",x=250,y=50)

personnages = ["Donald Trump","Harry Potter","Mickey","Shrek","Pikachu","Un télétubbies","La reine des neiges","Michel Drucker","Chris Marques","Justin Bieber","Gérard Depardieu","Céline Dion","Superman","Batman","Bob l'éponge","M Pokora","Kev Adams","Black M","Hulk","Spiderman","Antoine Griezmann","Patrick Sébastien","Ta mère","Kim Kardashian","Squeezie","Kim Jong-Un","Christina Cordula","Nicolas Sarkozy","Maitre Gims","François Hollande","JUL","Nabilla"]
situations = ["fait un régime","à Fort Boyard","en boite de nuit","à la Maison Blanche","mange un kebab","bourré","en ski","à Koh-Lanta","à The Voice","sur les toilettes","en string","chez l'esthéticienne","sur un télésiège","passe son permis","dans une cave","sur un vélib","à la piscine municipale","à Pôle Emploi","fait du poney","dans une crèche","en Corée du Nord","passe son bac","chez une voyante","chez mamie","fait un dab","en parachute","à la chicha","en garde à vue","sur Meetic","en battle de rap","à l'Elysée","à la salle"]
nbparticipants = 0
tps = 0                         # Mise en place des cartes (listes) et de variables

def créer():                            # Sous-programme lorsqu'on crée un code
    def ouvrirnoms():                   # Chaque sous-programme représente une fenêtre
        def créercode():
            code = ""
            for i in range(nbparticipants):
                liste[i] = liste2[i].get()
                code = code+liste[i]+"%"+hex(random.randint(0,1023))+"%"
            codefini = tk.Tk()
            codefini.geometry("1000x500+100+50")
            codefini.configure(bg="lightblue")
            noms.destroy()
            tk.Label(codefini,text="Le code est ",font=("Arial",20),bg="lightblue").place(anchor="n",x=500,y=50)
            Code = tk.Entry(codefini,text=code, width=100)
            Code.insert(0,code)
            Code.configure(state="readonly")
            Code.place(anchor="n",x=500,y=100)
            tk.Label(codefini,text="Si deux participants ont le même code, recommencer.",font=("Arial",15),bg="lightblue").place(anchor="n",x=500,y=200)
        global nbparticipants
        nbparticipants = int(question.get())
        noms =tk.Tk()
        noms.geometry("500x500+350+50")
        noms.configure(bg="lightblue")
        création.destroy()
        liste = [""]*nbparticipants
        liste2 = [""]*nbparticipants
        tk.Label(noms, text="Donner noms :",font=("Arial",20),bg="lightblue").place(anchor="n",x=250,y=50)
        for i in range(nbparticipants):
            liste2[i] = tk.Entry(noms)
            liste2[i].place(anchor="n",x=250,y=100+50*i)
        tk.Button(noms, text="OK",font=("Arial",15),command=créercode).place(anchor="n",x=250,y=100+50*nbparticipants)
    création = tk.Tk()
    création.geometry("500x500+350+50")
    création.configure(bg="lightblue")
    accueil.destroy()
    tk.Label(création, text="Combien de partcipants ?", font=("Arial",20), bg="lightblue").place(anchor="n",x=250,y=50)
    question = tk.Entry(création)
    question.place(anchor="n",x=250,y=150)
    tk.Button(création, text="OK", font=("Arial",15), command=ouvrirnoms).place(anchor="n",x=250,y=250)


def rejoindre():                # Sous-programme lorsqu'on rejoint une partie avec un code
    def choixnom():             # Chaque sous-programme représente une fenêtre (sauf sablier)
        def affcartes(x):
            def sablier(tps):
                temps.configure(text=str(tps))
                if tps > 0:
                    jeu.after(1000,sablier,tps-1)
            jeu = tk.Tk()
            jeu.geometry("1000x500+100+50")
            jeu.configure(bg="lightblue")
            choisir.destroy()
            for j in range(int(len(code)/2)):
                if x != j:
                    tk.Label(jeu,text="Cartes de "+code[j*2]+" : "+personnages[(int(code[j*2+1],16))//32]+" "+situations[(int(code[j*2+1],16))%32],bg="lightblue",font=("Arial",20)).place(anchor="n",x=500,y=50+j*50)
                    tk.Button(jeu,text="Lancer le sablier",font=("Arial",15),command=lambda:sablier(30)).place(anchor="w",x=100,y=250)
                    temps = tk.Label(jeu,text=str(tps), bg="lightblue",font=("Arial",15))
                    temps.place(anchor="w",x=100,y=300)
        var = codeentry.get()
        code = var.split("%")
        choisir = tk.Tk()
        choisir.geometry("500x500+350+50")
        choisir.configure(bg="lightblue")
        demandecode.destroy()
        tk.Label(choisir,text="Qui êtes vous ?",bg="lightblue",font=("Arial",20)).place(anchor="n",x=250,y=50)
        for i in range(int(len(code)/2)):
            tk.Button(choisir,text=code[i*2],font=("Arial",15),command=lambda x=i:affcartes(x)).place(anchor="n",x=250,y=100+i*50)
    demandecode = tk.Tk()
    demandecode.geometry("500x500+350+50")
    demandecode.configure(bg="lightblue")
    accueil.destroy()
    tk.Label(demandecode,text="Entrer code :",bg="lightblue",font=("Arial",20)).place(anchor="n",x=250,y=50)
    codeentry = tk.Entry(demandecode)
    codeentry.place(anchor="n",x=250,y=100)
    tk.Button(demandecode,text="OK",font=("Arial",15),command=choixnom).place(anchor="n",x=250,y=150)

# Boutons de la première fenêtre et boucle principale

tk.Button(accueil, text="Créer une partie", font=("Arial",15), command=créer).place(anchor="w",x=50,y=250)
tk.Button(accueil, text="Rejoindre une partie", font=("Arial",15), command=rejoindre).place(anchor="e",x=450,y=250)

tk.mainloop()