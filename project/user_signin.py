#DL 1st, user signin

users = {
"recentlybasil": "~%H62&nSl014",
"gothicextreme": "I'wp3Kk84amY",
"hardallege": "87u7>=+gEl^B",
"knowmealy": "25Cs7AZ|6DE:",
"promotepossibly": "|fetI0j?139~",
"clockworkconvocation": "lON(7Tp'13`3",
"jackstaffcollards": "T7uae(&*5ZD9",
"effectheadline": "(36Y4NvEHN.@",
"worthwhilethank": "i9>T~Tu44_c.",
"fiberdevoted": "w^,9k/]Y8j1F",
"tonicrapidly": "m/$+O37i23#+",
"debatethat": "nn8[B0D6~6£7",
"floweryresult": ";70d(3+/3TBt",
"differencethrough": "a2hL7nrF7zA$",
"quixoticblind": "c63;3?J'=/Aj",
"netherpleasant": "F0I5jRvZ3}6'",
"generousstockings": "zSr149X=Z*Tn",
"spanielhotdog": ":R'R60tq9t28",
"webbedfossil": "M|9tQS1h+31£",
"tholeshrouds": "682ZnmLJIj=%",
"harmoniousfun": "oG746>RadYr'",
"rookeryuniversity": "Vr6AcK=29(93",
"concernciabata": ".39=V9ZF0yaJ",
"ultrafaculty": "7<G9EO3El!Km",
"spawnerregarding": "hKq78kq0`3R]",
"sablechair": "GlEs(;]829>7",
"underclotheszippy": "c0uFFZs6f4@t",
"absorbingexistence": "N[Lofk19+q7Q",
"jumpjumping": "8/p/nI9^X821",
"junkypricey": "#Gx3O!31gV1D",
"sugarabject": "8}q3cW50*+,)",
"thankwash": "7I1)12I!7oFT",
"frybreadperturbed": "51]£4:y5dKL`",
"irasciblefocused": ")u6£vA6*8:&7",
"describepreshrunk": "8O{#I1`tr8'#",
"paintballbecause": "}Z2H<Ea|47E!",
"detailedenunciate": "_2w0@Awn1~/~"}
end = False

while True:
    name_input = input("What is your username?\n").strip()
    if name_input in users:
        correct_pass = users[name_input]
        while True:
            pass_input = input("What is your password?\n").strip()
            if pass_input == correct_pass:
                print(f"You are now logged in as {name_input}.")
                break
            else: 
                print("That password is incorrect, please try again.")
        break
    else:
        print("That user does not exist, please try again.")