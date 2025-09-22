#DL 1st, user signin

users = {
"recentlybasil": "~%H62&nSl014
"gothicextreme": "I'wp3Kk84amY
"hardallege": "87u7>=+gEl^B
"knowmealy": "25Cs7AZ|6DE:
"promotepossibly": "|fetI0j?139~
"clockworkconvocation": "lON(7Tp'13`3
"jackstaffcollards": "T7uae(&*5ZD9
"effectheadline": "(36Y4NvEHN.@
"worthwhilethank": "\9>T~Tu44_c.
"fiberdevoted": "w^,9k/]Y8j1F
"tonicrapidly": "m/$+O37i23#+
"debatethat": "
"floweryresult": "
"differencethrough": "
"quixoticblind": "
"netherpleasant": "
"generousstockings": "
"spanielhotdog": "
"webbedfossil": "
"tholeshrouds": "
"harmoniousfun": "
"rookeryuniversity": "
"concernciabata": "
"ultrafaculty": "
"spawnerregarding": "
"sablechair": "
"underclotheszippy": "
"absorbingexistence": "
"jumpjumping": "
"junkypricey": "
"sugarabject": "
"thankwash": "
"frybreadperturbed": "
"irasciblefocused": "
"describepreshrunk": "
"paintballbecause": "
"detailedenunciate": "
"annoyfisherman": "
"wedgeasian": "
"confirmsoon": "
"christiannutmeg": "
"dunbirdribbit": "
"fulfilledclunk": "
"curlinggrey": "
"dimensionjib": "
"hardtofindpallograph": "
"detailgoofy": "
"falterabsorbed": "
"guardianhandsome": "
"hyenaseafowls}
end = False

while True:
    if end == True:
                break
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
        break
    else:
        print("That user does not exist, please try again.")