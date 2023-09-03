print(__file__)
import os
print(os.getcwd())
from tkinter import*
from sys import version_info
if version_info.major == 2:
    import Tk as tk
elif version_info.major == 3:
    import tkinter as tk
def revenir():
    global fenetre1
    fenetre1.destroy()
    fenetre1=Tk()
    fenetre1.title("LOSC")
    label = Label(fenetre1, text="choissisez le joueur dont vous voulez des informations")
    #leojardim=tk.Button(fenetre1, text="Léo Jardim",command=leo_jardim,bg="black",fg='red',activebackground='cyan',width=60)
    adamjakubech = tk.Button(fenetre1, text="Adam Jakubech", command=adam_jakubech, bg="black", fg='red',activebackground='cyan', width=60)
    lucaschevalier = tk.Button(fenetre1, text="Lucas Chevalier", command=lucas_chevalier, bg="black", fg='red',activebackground='cyan', width=60)
    vitomannone = tk.Button(fenetre1, text="Vito Mannone", command=vito_mannone, bg="black", fg='red',activebackground='cyan', width=60)
    # benoitcostil=tk.Button(fenetre1, text="Benoît Costil",command=benoit_costil,bg="black",fg='red',activebackground='cyan',width=60)
    #svenbotman = tk.Button(fenetre1, text="Sven Botman", command=sven_botman, bg="black", fg='red',activebackground='cyan', width=60)
    tiagodjalo = tk.Button(fenetre1, text="Tiago Djaló", command=tiago_djalo, bg="black", fg='red',activebackground='cyan', width=60)
    #josefonte = tk.Button(fenetre1, text="José Fonte", command=jose_fonte, bg="black", fg='red',activebackground='cyan', width=60)
    alexsandro = tk.Button(fenetre1, text="Alexsandro", command=alexandro_, bg="black", fg='red',activebackground='cyan', width=60)
    samuelumtiti = tk.Button(fenetre1, text="Samuel Umtiti", command=samuel_umtiti, bg="black", fg='red',activebackground='cyan', width=60)
    lenyyoro = tk.Button(fenetre1, text="Leny Yoro", command=leny_yoro, bg="black", fg='red', activebackground='cyan',width=60)
    gabrielgudmudsson = tk.Button(fenetre1, text="Gabriel Gudmudsson", command=gabriel_gudmudsson, bg="black", fg='red',activebackground='cyan', width=60)
    akimzedadka = tk.Button(fenetre1, text="Akim Zedadka", command=akim_zedadka, bg="black", fg='red',activebackground='cyan', width=60)
    bafodediakate = tk.Button(fenetre1, text="Bafodé Diakité", command=bafode_diakate, bg="black", fg='red',activebackground='cyan', width=60)
    tiagosantos = tk.Button(fenetre1, text="Tiago Santos", command=tiago_santos, bg="black", fg='red',activebackground='cyan', width=60)
    ismaily = tk.Button(fenetre1, text="Ismaily", command=is_maily, bg="black", fg='red', activebackground='cyan',width=60)
    benjaminandre = tk.Button(fenetre1, text="Benjamin André", command=benjamin_andre, bg="black", fg='red',activebackground='cyan', width=60)
    #jonasmartin = tk.Button(fenetre1, text="Jonas Martin", command=jonas_martin, bg="black", fg='red',activebackground='cyan', width=60)
    #andregomes = tk.Button(fenetre1, text="André Gomes", command=andre_gomes, bg="black", fg='red',activebackground='cyan', width=60)
    #carlosbaleba = tk.Button(fenetre1, text="Carlos Baleba", command=carlos_baleba, bg="black", fg='red',activebackground='cyan', width=60)
    ignaciomiramon = tk.Button(fenetre1, text="Ignacio Miramón", command=ignacio_miramon, bg="black", fg='red',activebackground='cyan', width=60)
    yusufyazici = tk.Button(fenetre1, text="Yusuf Yazici", command=yusuf_yazici, bg="black", fg='red',activebackground='cyan', width=60)
    angelgomes = tk.Button(fenetre1, text="Angel Gomes", command=angel_gomes, bg="black", fg='red',activebackground='cyan', width=60)
    nabilbentaleb = tk.Button(fenetre1, text="Nabil Bentaleb", command=nabil_bentaleb, bg="black", fg='red',activebackground='cyan', width=60)
    remycabella = tk.Button(fenetre1, text="Remy Cabella", command=remy_cabella, bg="black", fg='red',activebackground='cyan', width=60)
    #jonathanbamba = tk.Button(fenetre1, text="Jonathan Bamba", command=jonathan_bamba, bg="black", fg='red',activebackground='cyan', width=60)
    hakonharaldsson = tk.Button(fenetre1, text="Hákon Arnar Haraldsson", command=hakon_haraldsson, bg="black", fg='red',activebackground='cyan', width=60)
    alanvirginius = tk.Button(fenetre1, text=" Alan Virginius", command=alan_virginius, bg="black", fg='red',activebackground='cyan', width=60)
    ivancavaleiro = tk.Button(fenetre1, text=" Ivan Cavaleiro", command=ivan_cavaleiro, bg="black", fg='red',activebackground='cyan', width=60)
    adamounas = tk.Button(fenetre1, text="Adam Ounas", command=adam_ounas, bg="black", fg='red',activebackground='cyan', width=60)
    edonzhegrova = tk.Button(fenetre1, text="Edon Zhegrova", command=edon_zhegrova, bg="black", fg='red',activebackground='cyan', width=60)
    #isaaclihadji = tk.Button(fenetre1, text="Isaac Lihadji", command=isaac_lihadji, bg="black", fg='red',activebackground='cyan', width=60)
    jonathandavid = tk.Button(fenetre1, text="Jonathan David", command=jonathan_david, bg="black", fg='red',activebackground='cyan', width=60)
    #timothyweah = tk.Button(fenetre1, text="Timothy Weah", command=timothy_weah, bg="black", fg='red',activebackground='cyan', width=60)
    #mohamedbayo = tk.Button(fenetre1, text="Mohamed Bayo", command=mohamed_bayo, bg="black", fg='red',activebackground='cyan', width=60)
    label.pack()
    #leojardim.pack()
    adamjakubech.pack()
    lucaschevalier.pack()
    vitomannone.pack()
    #svenbotman.pack()
    tiagodjalo.pack()
    #josefonte.pack()
    alexsandro.pack()
    samuelumtiti.pack()
    lenyyoro.pack()
    gabrielgudmudsson.pack()
    #benoitcostil.pack()
    akimzedadka.pack()
    bafodediakate.pack()
    tiagosantos.pack()
    ismaily.pack()
    benjaminandre.pack()
    #jonasmartin.pack()
    #andregomes.pack()
    #carlosbaleba.pack()
    ignaciomiramon.pack()
    yusufyazici.pack()
    angelgomes.pack()
    nabilbentaleb.pack()
    remycabella.pack()
    #jonathanbamba.pack()
    hakonharaldsson.pack()
    alanvirginius.pack()
    ivancavaleiro.pack()
    adamounas.pack()
    edonzhegrova.pack()
    #isaaclihadji.pack()
    jonathandavid.pack()
    #timothyweah.pack()
    #mohamedbayo.pack()
    fenetre1.mainloop()
def mohamed_bayo():
    mohamed = Tk()
    mohamed.title("Mohamed Bayo")
    img = PhotoImage(file='mohamed.PNG', master=mohamed)
    texte = Label(mohamed, text="""
                        Poste: Avant-centre
                        Pied:droit
                        Valeur Marchande: 6M€
                        Age:25ans 
                        Pays:Guinée France
                        Numéro: 27
                        Taille: 1,88M
                        Info: transfertmarket et onefootball""")
    label1 = Label(mohamed, image=img, )
    retour = tk.Button(mohamed, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    mohamed.mainloop()
def timothy_weah():
    timothy = Tk()
    timothy.title ("Timothy Weah")
    img = PhotoImage(file='timothy.PNG', master=timothy)
    texte = Label(timothy, text="""
                        Poste: Avant-centre
                        Pied:droit
                        Valeur Marchande: 12M€
                        Age:22ans 
                        Pays:Etats-Unis France
                        Numéro: 22
                        Taille: 1,85M
                        Info: transfertmarket et onefootball""")
    label1 = Label(timothy, image=img, )
    retour = tk.Button(timothy, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    timothy.mainloop()
def jonathan_david():
    jonathan = Tk()
    jonathan.title("Jonathan David")
    img = PhotoImage(file='jonathan.PNG', master=jonathan)
    texte = Label(jonathan, text="""
                        Poste: Avant-centre
                        Pied:ambidextre
                        Valeur Marchande: 60M€
                        Age:23ans 
                        Pays:Canada Etats-Unis
                        Numéro: 9
                        Taille: 1,75M
                        Info: transfertmarket et onefootball""")
    label1 = Label(jonathan, image=img, )
    retour = tk.Button(jonathan, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    jonathan.mainloop()
def isaac_lihadji():
    isaac = Tk()
    isaac.title("Isaac Lihadji")
    img = PhotoImage(file='isaac.PNG', master=isaac)
    texte = Label(isaac, text="""
                        Poste: Ailier droit
                        Pied:gauche
                        Valeur Marchande: 3,5M€
                        Age:20ans 
                        Pays:France Comores
                        Numéro: 19
                        Taille: 1,77M
                        Info: transfertmarket et onefootball""")
    label1 = Label(isaac, image=img, )
    retour = tk.Button(isaac, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    isaac.mainloop()
def edon_zhegrova():
    edon = Tk()
    edon.title("Edon Zhegrova")
    img = PhotoImage(file='edon.PNG', master=edon)
    texte = Label(edon, text="""
                        Poste: Ailier droit
                        Pied:gauche
                        Valeur Marchande: 8M€
                        Age:23ans 
                        Pays:Kosovo Allemagne
                        Numéro: 23
                        Taille: 1,81M
                        Info: transfertmarket et onefootball""")
    label1 = Label(edon, image=img, )
    retour = tk.Button(edon, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    edon.mainloop()
def adam_ounas():
    adam = Tk()
    adam.title("Adam Ounas")
    img = PhotoImage(file='adam.PNG', master=adam)
    texte = Label(adam, text="""
                        Poste: Ailier droit
                        Pied:gauche
                        Valeur Marchande: 7M€
                        Age:26ans 
                        Pays:Algérie France
                        Numéro: 11
                        Taille: 1,72M
                        Info: transfertmarket et onefootball""")
    label1 = Label(adam, image=img, )
    retour = tk.Button(adam, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    adam.mainloop()
def ivan_cavaleiro():
    ivan = Tk()
    ivan.title("Ivan Cavaleiro")
    img = PhotoImage(file='ivan.PNG', master=ivan)
    texte = Label(ivan, text="""
                        Poste: Ailier gauche
                        Pied:droit
                        Valeur Marchande: 2,2M€
                        Age:29ans 
                        Pays:Angola Portugal
                        Numéro: 17
                        Taille: 1,75M
                        Info: transfertmarket et onefootball""")
    label1 = Label(ivan, image=img, )
    retour = tk.Button(ivan, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    ivan.mainloop()
def alan_virginius():
    alan = Tk()
    alan.title("Alan Virginius")
    img = PhotoImage(file='alan.PNG', master=alan)
    texte = Label(alan, text="""
                        Poste: Ailier gauche
                        Pied:droit
                        Valeur Marchande: 4M€
                        Age:20ans 
                        Pays:France
                        Numéro: 26
                        Taille: 1,75M
                        Info: transfertmarket et onefootball""")
    label1 = Label(alan, image=img, )
    retour = tk.Button(alan, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    alan.mainloop()
def hakon_haraldsson():
    hakon = Tk()
    hakon.title("Hákon Arnar Haraldsson")
    img = PhotoImage(file='hakon.png', master=hakon)
    texte = Label(hakon, text="""
                        Poste: Ailier gauche
                        Pied:droit
                        Valeur Marchande: 6M€
                        Age:20ans 
                        Pays:Islande
                        Numéro: 7
                        Taille: 1,80M
                        Info: transfertmarket et onefootball""")
    label1 = Label(hakon, image=img, )
    retour = tk.Button(hakon, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    hakon.mainloop()
def jonathan_bamba():
    jo = Tk()
    jo.title ("Jonathan Bamba")
    img = PhotoImage(file='jo.PNG', master=jo)
    texte = Label(jo, text="""
                        Poste: Ailier gauche
                        Pied:droit
                        Valeur Marchande: 20M€
                        Age:26ans 
                        Pays:France Cote d'Ivoire
                        Numéro: 7
                        Taille: 1,75M
                        Info: transfertmarket et onefootball""")
    label1 = Label(jo, image=img, )
    retour = tk.Button(jo, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    jo.mainloop()
def remy_cabella():
    remy = Tk()
    remy.title("Rémy Cabella")
    img = PhotoImage(file='remy.PNG', master=remy)
    texte = Label(remy, text="""
                        Poste: Milieu offensif
                        Pied:droit
                        Valeur Marchande: 5M€
                        Age:33ans 
                        Pays:France Italie
                        Numéro: 10
                        Taille: 1,71M
                        Info: transfertmarket et onefootball""")
    label1 = Label(remy, image=img, )
    retour = tk.Button(remy, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    remy.mainloop()
def angel_gomes():
    angel = Tk()
    angel.title("Angel Gomes")
    img = PhotoImage(file='angel.PNG', master=angel)
    texte = Label(angel, text="""
                        Poste: Milieu offensif
                        Pied:droit
                        Valeur Marchande: 18M€
                        Age:22ans 
                        Pays:Angleterre Portugal
                        Numéro: 8
                        Taille: 1,68M
                        Info: transfertmarket et onefootball""")
    label1 = Label(angel, image=img, )
    retour = tk.Button(angel, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    angel.mainloop()
def nabil_bentaleb():
    nabil = Tk()
    nabil.title("Nabil Bentaleb")
    img = PhotoImage(file='nabil.PNG', master=nabil)
    texte = Label(nabil, text="""
                        Poste: Milieu central
                        Pied:gauche
                        Valeur Marchande: 7M€
                        Age:28ans 
                        Pays:Algérie France
                        Numéro: 6
                        Taille: 1,87M
                        Info: transfertmarket et onefootball""")
    label1 = Label(nabil, image=img, )
    retour = tk.Button(nabil, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    nabil.mainloop()
def yusuf_yazici():
    yusuf = Tk()
    yusuf.title("Yusuf Yazici")
    img = PhotoImage(file='yusuf.PNG', master=yusuf)
    texte = Label(yusuf, text="""
                        Poste: Milieu offensif
                        Pied:gauche
                        Valeur Marchande: 9M€
                        Age:26ans 
                        Pays:Turquie
                        Numéro: 12
                        Taille: 1,84M
                        Info: transfertmarket et onefootball""")
    label1 = Label(yusuf, image=img, )
    retour = tk.Button(yusuf, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    yusuf.mainloop()
def ignacio_miramon():
    ignacio = Tk()
    ignacio.title("Ignacio Miramón")
    img = PhotoImage(file='ignacio.PNG', master=ignacio)
    texte = Label(ignacio, text="""
                        Poste: Milieu défensif
                        Pied:droit
                        Valeur Marchande: 4M€
                        Age:20ans 
                        Pays:Argentine
                        Numéro: 20
                        Taille: 1,73M
                        Info: transfertmarket et onefootball""")
    label1 = Label(ignacio, image=img, )
    retour = tk.Button(ignacio, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    ignacio.mainloop()
def carlos_baleba():
    carlos = Tk()
    carlos.title("Carlos Baleba")
    img = PhotoImage(file='carlos.PNG', master=carlos)
    texte = Label(carlos, text="""
                    Poste: Milieu central
                    Pied:gauche
                    Valeur Marchande: 5M€
                    Age:19ans 
                    Pays:Cameroun
                    Numéro: 35
                    Taille: 1,79m
                    Info: transfertmarket et onefootball""")
    label1 = Label(carlos, image=img, )
    retour = tk.Button(carlos, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    carlos.mainloop()
def andre_gomes():
    andre = Tk()
    andre.title("Andre Gomes")
    img = PhotoImage(file='andre.PNG', master=andre)
    texte = Label(andre, text="""
                        Poste: Milieu central
                        Pied:droit
                        Valeur Marchande: 14M€
                        Age:29ans 
                        Pays:Portugal
                        Numéro: inconnue
                        Taille: 1,88M
                        Info: transfertmarket et onefootball""")
    label1 = Label(andre, image=img, )
    retour = tk.Button(andre, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    andre.mainloop()
def jonas_martin():
    jonas = Tk()
    jonas.title("Jonas Martin")
    img = PhotoImage(file='jonas.PNG', master=jonas)
    texte = Label(jonas, text="""
                    Poste: Milieu défensif
                    Pied:droit
                    Valeur Marchande: 1,8M€
                    Age:32ans 
                    Pays:France
                    Numéro: 8
                    Taille: 1,84m
                    Info: transfertmarket et onefootball""")
    label1 = Label(jonas, image=img, )
    retour = tk.Button(jonas, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    jonas.mainloop()
def benjamin_andre():
    benjamin = Tk()
    benjamin.title("Benjamin André")
    img = PhotoImage(file='benjamin.PNG', master=benjamin)
    texte = Label(benjamin, text="""
                Poste: Milieu défensif
                Pied:droit
                Valeur Marchande: 9M€
                Age:33ans 
                Pays:France
                Numéro: 21
                Taille: 1,80m
                Info: transfertmarket et onefootball""")
    label1 = Label(benjamin, image=img, )
    retour = tk.Button(benjamin, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    benjamin.mainloop()
def tiago_santos():
    tiago1=Tk()
    tiago1.title("Tiago Santos")
    img = PhotoImage(file='tiago1.PNG', master=tiago1)
    texte = Label(tiago1, text="""
                    Poste: Arrière droit 
                    Pied:droit
                    Valeur Marchande: 3,5M€
                    Age:21ans 
                    Pays: Portugal
                    Numéro: 22
                    Taille: 1,75m
                    Info: transfertmarket et onefootball""")
    label1 = Label(tiago1, image=img, )
    retour = tk.Button(tiago1, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    tiago1.mainloop()
def bafode_diakate():
    bafode=Tk()
    bafode.title("Bafodé Diakité")
    img = PhotoImage(file='bafode.PNG', master=bafode)
    texte = Label(bafode, text="""
                    Poste: Défenseur central
                    Pied:droit
                    Valeur Marchande: 10M€
                    Age:22ans 
                    Pays: France Guinée
                    Numéro: 18
                    Taille: 1,85m
                    Info: transfertmarket et onefootball""")
    label1 = Label(bafode, image=img, )
    retour = tk.Button(bafode, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    bafode.mainloop()
def is_maily():
    ismail_y=Tk()
    ismail_y.title("Ismaily")
    img = PhotoImage(file='ismaily.PNG', master=ismail_y)
    texte = Label(ismail_y, text="""
                    Poste: Arrière gauche
                    Pied:gauche
                    Valeur Marchande: 2,5M€
                    Age:33ans 
                    Pays: Brasil
                    Numéro: 31
                    Taille: 1,77m
                    Info: transfertmarket et onefootball""")
    label1 = Label(ismail_y, image=img, )
    retour = tk.Button(ismail_y, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    ismail_y.mainloop()
def akim_zedadka():
    akim = Tk()
    akim.title("Akim Zedadka")
    img = PhotoImage(file='akim.PNG', master=akim)
    texte = Label(akim, text="""
                Poste: Arrière droit
                Pied:droit
                Valeur Marchande: 2,5M€
                Age:28ans 
                Pays: Algérie France
                Numéro: 13
                Taille: 1,73m
                Info: transfertmarket et onefootball""")
    label1 = Label(akim, image=img, )
    retour = tk.Button(akim, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    akim.mainloop()
def gabriel_gudmudsson():
    gabriel = Tk()
    gabriel.title("Gabriel Gudmudsson")
    img = PhotoImage(file='gabriel.PNG', master=gabriel)
    texte = Label(gabriel, text="""
            Poste: Arrière gauche
            Pied:gauche
            Valeur Marchande: 4,5M€
            Age:24ans 
            Pays: Suéde
            Numéro: 5
            Taille: 1,80m
            Info: transfertmarket et onefootball""")
    label1 = Label(gabriel, image=img, )
    retour = tk.Button(gabriel, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    gabriel.mainloop()
def leny_yoro():
    leny = Tk()
    leny.title("Leny Yoro")
    img = PhotoImage(file='leny.png', master=leny)
    texte = Label(leny, text="""
            Poste: Défenseur central
            Pied:droit
            Valeur Marchande: 10M€
            Age:17ans 
            Pays: France Cote d'Ivoire
            Numéro: 15
            Taille: 1,90m
            Info: transfertmarket et onefootball""")
    label1 = Label(leny, image=img, )
    retour = tk.Button(leny, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    leny.mainloop()
def samuel_umtiti():
    samuel = Tk()
    samuel.title("Samuel Umtiti")
    img = PhotoImage(file='samuel.png', master=samuel)
    texte = Label(samuel, text="""
            Poste: Défenseur central
            Pied:gauche
            Valeur Marchande: 4M€
            Age:29ans 
            Pays: France Cameroun
            Numéro: 14
            Taille: 1,82m
            Info: transfertmarket et onefootball""")
    label1 = Label(samuel, image=img, )
    retour = tk.Button(samuel, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    samuel.mainloop()
def alexandro_():
    alex = Tk()
    alex.title("Alexsandro")
    img = PhotoImage(file='alexsandro.png', master=alex)
    texte = Label(alex, text="""
        Poste: Défenseur central
        Pied:droit
        Valeur Marchande: 5M€
        Age:24ans 
        Pays: Brésil
        Numéro: 4
        Taille: 1,89m
        Info: transfertmarket et onefootball""")
    label1 = Label(alex, image=img, )
    retour = tk.Button(alex, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    alex.mainloop()
def jose_fonte():
    jose = Tk()
    jose.title("José Fonte")
    img = PhotoImage(file='jose.png', master=jose)
    texte = Label(jose, text="""Poste: Défenseur central
        Pied:droit
        Valeur Marchande: 700k€
        Age:39ans 
        Pays: Portugal
        Numéro: 6
        Taille: 1,91m
        Info: transfertmarket et onefootball""")
    label1 = Label(jose, image=img, )
    retour = tk.Button(jose, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    jose.mainloop()
def tiago_djalo():
    tiago = Tk()
    tiago.title ("Tiago Djaló")
    img = PhotoImage(file='tiago.PNG', master=tiago)
    texte = Label(tiago, text="""
        Poste: Défenseur central
        Pied:droit
        Valeur Marchande: 16M€
        Age:23ans 
        Pays: Portugal Guinée-Biseau
        Numéro: 3
        Taille:1,90m
        Info: transfertmarket et onefootball""")
    label1 = Label(tiago, image=img, )
    retour = tk.Button(tiago, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    tiago.mainloop()
def sven_botman():
    sven = Tk()
    sven.title ("Sven Botman")
    img = PhotoImage(file='sven.PNG', master=sven)
    texte = Label(sven, text="""
        Poste: defenseur central
        Pied: gauche
        Valeur Marchande: 30M€
        Age:22ans 
        Pays: Pays-Bas
        Numéro: 4
        Taille:1,95m
        Info: transfertmarket et onefootball""")
    label1 = Label(sven, image=img, )
    retour = tk.Button(sven, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    sven.mainloop()
def benoit_costil():
    benoit= Tk()
    benoit.title("Benoît Costil")
    img = PhotoImage(file='benoit.PNG', master=benoit)
    texte = Label(benoit, text="""
    Poste: gardien
    Pied:droit
    Valeur Marchande: 1,5M€
    Age:35ans 
    Pays: France
    Numéro: 25
    Taille:1,88m
    Info: transfertmarket et onefootball""")
    label1 = Label(benoit, image=img, )
    retour = tk.Button(benoit, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    benoit.mainloop()
def vito_mannone():
    vito= Tk()
    vito.title("Vito Mannone")
    img = PhotoImage(file='vito.PNG', master=vito)
    texte = Label(vito, text="""
    Poste: gardien
    Pied:droit
    Valeur Marchande: 300k€
    Age:35ans 
    Pays: Italie
    Numéro: 1
    Taille:1,89m
    Info: transfertmarket et onefootball""")
    label1 = Label(vito, image=img, )
    retour = tk.Button(vito, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    vito.mainloop()
def lucas_chevalier():
    lucas= Tk()
    lucas.title ("Lucas Chevalier")
    img = PhotoImage(file='chevalier.PNG', master=lucas)
    texte = Label(lucas, text="""
    Poste: gardien
    Pied:droit
    Valeur Marchande: 10M€
    Age:21ans 
    Pays: France
    Numéro: 30
    Taille:1,89m
    Info: transfertmarket et onefootball""")
    label1 = Label(lucas, image=img, )
    retour = tk.Button(lucas, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    lucas.mainloop()
def adam_jakubech():
    adam= Tk()
    adam.title ("Adam Jakubech")
    img = PhotoImage(file='jakubech.PNG', master=adam)
    texte = Label(adam, text="""
    Poste: gardien
    Pied:droit
    Valeur Marchande: 300k€
    Age:26ans 
    Pays: Slovaquie
    Numéro: 16
    Taille:1,88m
    Info: transfertmarket et onefootball""")
    label1 = Label(adam, image=img, )
    retour = tk.Button(adam, text="revenir au menu", command=revenir, bg="black", fg='red', activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    adam.mainloop()
def leo_jardim():
    jardim=Tk()
    jardim.title("Léo Jardim")
    img = PhotoImage(file='leo.png', master=jardim)
    texte = Label(jardim, text="""Poste: gardien
    Pied:droit
    Valeur Marchande: 4M€
    Age:27ans 
    Pays: Brésil et Italie
     Numéro: 1
     Taille: 1,88m
     Info: transfertmarket et onefootball""")
    label1=Label(jardim,image=img,)
    retour=tk.Button(jardim, text="revenir au menu",command=revenir,bg="black",fg='red',activebackground='cyan',width=78)
    label1.pack()
    texte.pack()
    retour.pack()
    jardim.mainloop()
fenetre1=Tk()
fenetre1.title("LOSC")
label = Label(fenetre1, text="choissisez le joueur dont vous voulez des informations")
#leojardim=tk.Button(fenetre1, text="Léo Jardim",command=leo_jardim,bg="black",fg='red',activebackground='cyan',width=60)
adamjakubech=tk.Button(fenetre1,text="Adam Jakubech",command=adam_jakubech,bg="black",fg='red',activebackground='cyan',width=60)
lucaschevalier=tk.Button(fenetre1, text="Lucas Chevalier",command=lucas_chevalier,bg="black",fg='red',activebackground='cyan',width=60)
vitomannone=tk.Button(fenetre1, text="Vito Manonne",command=vito_mannone,bg="black",fg='red',activebackground='cyan',width=60)
#benoitcostil=tk.Button(fenetre1, text="Benoît Costil",command=benoit_costil,bg="black",fg='red',activebackground='cyan',width=60)
#svenbotman=tk.Button(fenetre1, text="Sven Botman",command=sven_botman,bg="black",fg='red',activebackground='cyan',width=60)
tiagodjalo=tk.Button(fenetre1, text="Tiago Djaló",command=tiago_djalo,bg="black",fg='red',activebackground='cyan',width=60)
#josefonte = tk.Button(fenetre1, text="José Fonte", command=jose_fonte, bg="black", fg='red',activebackground='cyan', width=60)
alexandro = tk.Button(fenetre1, text="Alexandro", command=alexandro_, bg="black", fg='red',activebackground='cyan', width=60)
samuelumtiti = tk.Button(fenetre1, text="Samuel Umtiti", command=samuel_umtiti, bg="black", fg='red',activebackground='cyan', width=60)
lenyyoro = tk.Button(fenetre1, text="Leny Yoro", command=leny_yoro, bg="black", fg='red',activebackground='cyan', width=60)
gabrielgudmudsson = tk.Button(fenetre1, text="Gabriel Gudmudsson", command=gabriel_gudmudsson, bg="black", fg='red',activebackground='cyan', width=60)
akimzedadka = tk.Button(fenetre1, text="Akim Zedadka", command=akim_zedadka, bg="black", fg='red',activebackground='cyan', width=60)
bafodediakate = tk.Button(fenetre1, text="Bafodé Diakité", command=bafode_diakate, bg="black", fg='red',activebackground='cyan', width=60)
tiagosantos = tk.Button(fenetre1, text="Tiago Santos", command=tiago_santos, bg="black", fg='red',activebackground='cyan', width=60)
ismaily = tk.Button(fenetre1, text="Ismaily", command=is_maily, bg="black", fg='red',activebackground='cyan', width=60)
benjaminandre = tk.Button(fenetre1, text="Benjamin André", command=benjamin_andre, bg="black", fg='red',activebackground='cyan', width=60)
#jonasmartin = tk.Button(fenetre1, text="Jonas Martin", command=jonas_martin, bg="black", fg='red',activebackground='cyan', width=60)
#andregomes= tk.Button(fenetre1, text="André Gomes", command=andre_gomes, bg="black", fg='red',activebackground='cyan', width=60)
#carlosbaleba = tk.Button(fenetre1, text="Carlos Baleba", command=carlos_baleba, bg="black", fg='red',activebackground='cyan', width=60)
ignaciomiramon = tk.Button(fenetre1, text="Ignacio Miramón", command=ignacio_miramon, bg="black", fg='red',activebackground='cyan', width=60)
yusufyazici= tk.Button(fenetre1, text="Yusuf Yazici", command=yusuf_yazici, bg="black", fg='red',activebackground='cyan', width=60)
angelgomes= tk.Button(fenetre1, text="Angel Gomes", command=angel_gomes, bg="black", fg='red',activebackground='cyan', width=60)
nabilbentaleb= tk.Button(fenetre1, text="Nabil Bentaleb", command=nabil_bentaleb, bg="black", fg='red',activebackground='cyan', width=60)
remycabella= tk.Button(fenetre1, text="Remy Cabella", command=remy_cabella, bg="black", fg='red',activebackground='cyan', width=60)
#jonathanbamba= tk.Button(fenetre1, text="Jonathan Bamba", command=jonathan_bamba, bg="black", fg='red',activebackground='cyan', width=60)
hakonharaldsson= tk.Button(fenetre1, text="Hákon Arnar Haraldsson", command=hakon_haraldsson, bg="black", fg='red',activebackground='cyan', width=60)
alanvirginius= tk.Button(fenetre1, text=" Alan Virginius", command=alan_virginius, bg="black", fg='red',activebackground='cyan', width=60)
ivancavaleiro= tk.Button(fenetre1, text=" Ivan Cavaleiro", command=ivan_cavaleiro, bg="black", fg='red',activebackground='cyan', width=60)
adamounas= tk.Button(fenetre1, text="Adam Ounas", command=adam_ounas, bg="black", fg='red',activebackground='cyan', width=60)
edonzhegrova= tk.Button(fenetre1, text="Edon Zhegrova", command=edon_zhegrova, bg="black", fg='red',activebackground='cyan', width=60)
#isaaclihadji= tk.Button(fenetre1, text="Isaac Lihadji", command=isaac_lihadji, bg="black", fg='red',activebackground='cyan', width=60)
jonathandavid= tk.Button(fenetre1, text="Jonathan David", command=jonathan_david, bg="black", fg='red',activebackground='cyan', width=60)
#timothyweah= tk.Button(fenetre1, text="Timothy Weah", command=timothy_weah, bg="black", fg='red',activebackground='cyan', width=60)
#mohamedbayo= tk.Button(fenetre1, text="Mohamed Bayo", command=mohamed_bayo, bg="black", fg='red',activebackground='cyan', width=60)
label.pack()
#leojardim.pack()
adamjakubech.pack()
lucaschevalier.pack()
vitomannone.pack()
#benoitcostil.pack()
#svenbotman.pack()
tiagodjalo.pack()
#josefonte.pack()
alexandro.pack()
samuelumtiti.pack()
lenyyoro.pack()
gabrielgudmudsson.pack()
akimzedadka.pack()
bafodediakate.pack()
tiagosantos.pack()
ismaily.pack()
benjaminandre.pack()
#jonasmartin.pack()
#andregomes.pack()
#carlosbaleba.pack()
ignaciomiramon.pack()
yusufyazici.pack()
angelgomes.pack()
nabilbentaleb.pack()
remycabella.pack()
#jonathanbamba.pack()
hakonharaldsson.pack()
alanvirginius.pack()
ivancavaleiro.pack()
adamounas.pack()
edonzhegrova.pack()
#isaaclihadji.pack()
jonathandavid.pack()
#timothyweah.pack()
#mohamedbayo.pack()
fenetre1.mainloop()

# info: Poste , Pied , Valeur Marchande, Age, Pays, taille