from pyscript import document

def signupcheck(eventOne):
    document.getElementById('resultU').innerHTML = "" # resets resultU id data
    
    # accessing user's answer
    username = document.getElementById("user").value
    password = document.getElementById("pass").value

    # variables for checking
    pwdMessage = "" # for password error message
    isValidUsername = False
    hasLetter = False
    hasNumber = False

    # username requirement check
    if len(username)>= 7:
        isValidUsername = True
    if not isValidUsername:
        document.getElementById("resultU").innerHTML = "Username is too short. Must be at least 7 characters long."

    # password requirement check
    for letter in password:
        if letter.lower() in "abcdefghijklmnopqrstuvwxyz": # check if there's a character present
            hasLetter = True
        if letter.isdigit(): # check if there's a number present
            hasNumber = True
    if not hasNumber:
        pwdMessage += " Password does not contain at least one number."
    if not hasLetter:
        pwdMessage += " Password does not contain at least one letter."
    if len(password)<10:
        pwdMessage += f" Password too short. Add at least {10-len(password)} more character/s to proceed."
    document.getElementById("resultP").innerHTML = pwdMessage

def check(eventTwo):
    #erasing the contents in result and team id
    document.getElementById('result').innerHTML = ""
    document.getElementById('team').innerHTML = ""

    #accessing answer of the user
    registered = document.querySelector(
        '#intramuralsForm input[name="registered"]:checked'
    ).value
    medical = document.querySelector(
        '#intramuralsForm input[name="medical"]:checked'
    ).value
    grade = int(document.getElementById("grade").value) #int - converting it to a number
    section = document.getElementById("section").value
    img = document.getElementById("image")
    img.src=""
    img.style.display = "none"
    # Nested if statements for eligibility
    if registered == "yes":
        if medical == "yes":
            img.style.display = "block"
            img.style.margin="auto"
            if 7 <= grade <= 10:
                document.getElementById('result').innerHTML = "Congratulations! You are eligible for Intramurals."
                if section == 'Emerald':
                    document.getElementById('team').innerHTML = "You are a member of the RED BULLDOGS!"
                    img.src = 'bulldogs.png'
                elif section == 'Ruby':
                    document.getElementById('team').innerHTML = "You are a member of the GREEN HORNETS!"
                    img.src = 'hornets.png'
                elif section == 'Sapphire':
                    document.getElementById('team').innerHTML = "You are a member of the YELLOW TIGERS!"
                    img.src = 'tigers.png'
                elif section == 'Topaz':
                    document.getElementById('team').innerHTML = "You are a member of the BLUE BEARS!"
                    img.src = 'bears.png'
                elif section == 'Jade':
                    document.getElementById('team').innerHTML = "You are a member of the RED BULLDOGS!"
                    img.src = 'bulldogs.png'
            else: 
                #if grade is beyond 10
                document.getElementById('result').innerHTML = "Not eligible: Only Grades 7–10 may join."
        else:
            #if no medical clearance
            document.getElementById('result').innerHTML = "Not eligible: Please secure a medical clearance."
    else:
        #if not registered
        document.getElementById('result').innerHTML = "Not eligible: Please register online."

# Players extracted from screenshots and sorted by Last Name
players = [
   "Al Hazmi, Ebtisam",
   "Alvarez, Yaniszsolt",
   "Belsa, Ethan",
   "Bernas, Giana",
   "Calaycay, Julianna",
   "Castelo, Jemilla",
   "Cruz, Francesca",
   "Defensor, Ely",
   "Dimasuhid, Dannielle",
   "Francisco, Althea",
   "Hsu, Cristina",
   "Juatchon, Denise",
   "Judge, Judah",
   "Lilagan, Francis",
   "Luna, Sam",
   "Macaranas, Enzo",
   "Mateo, Pain",
   "Mondragon, Ashley",
   "Naldoza, Lance",
   "Natividad, Gabriel",
   "Ng, Sofia",
   "Ong, Hendrich",
   "Paz, Trisha",
   "Ramos, Miguel",
   "Ramos, Queeny",
   "Ramos, Samantha",
   "Reodica, Ashlei",
   "Repolona, Vaughn"
]

def reveal_list(eventThree):
   output = document.querySelector("#player-list")
   output.innerHTML = "" # Clear area
  
   for i, name in enumerate(players, 1):
       div = document.createElement("div")
       div.innerText = f"{i}) {name}"
       output.appendChild(div)