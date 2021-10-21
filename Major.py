#Lukas Robin
#19.10.2021
#All rights retained herein
#Program helps guide choosing majors or field of study, or plays a game


import subprocess, platform, random, csv, math, time
#list of possible fields
fields=[
        'STEM', 
        'Law',
        'Medicine', 
        'Social Sciences', 
        'Business', 
        'Education', 
        'Communications'
        ];
#pre-set questions to determine major
questions = [
            "Just a typical weeknight, what are you watching? \n1. DIY videos\n2. Documentary on humanitarian issues \nResponse: ",
            "The power goes out, what do you do? \n1. Google how to restore power \n2. Check on your loved ones to see how they are doing\nResponse: ",
            "Strangers knock on your door at lunch hour, do you: \n1. Tell them you are busy and close the door\n2. Talk to them\nResponse: ",
            "Do you have a general interest in the sciences? \n1. Yes \n2. No \nResponse: ",
            "Do you have a general interest in logic and argumentation? \n1. Yes \n2. No \nResponse: ",
            "Are you curious about the natural world? \n1. Yes \n2. No \nResponse: ",
            "Do you fancy economy? \n1. Yes \n2. No\nResponse: ",
            "Do you want to focus on helping people? \n1. I wouldn't mind, but it is not my primary objective. \n2. Yes\nResponse: ",
            "Do you have an interest in how ideas are communicated? \n1. No \n2. Yes\nResponse: "
            ];

#object for the user
class Fields:
    def __init__(self, field, points):
        self.field = field;
        self.points = points;

    def get_field(self):
        return self.field;
    def set_field(self, field_name: str):
        self.field = field_name;

    def add_points(self):
        self.points += 1;
    def subt_points(self):
        self.points -= 1;
class Character:
    def __init__(self, name, health, points, characterType)->None:
        self.characterType = characterType;
        self.name = name;
        self.health = health;
        self.points = points;

    def get_characterType(self)->object:
	    return self.characterType;

    def get_health(self)->object:
        return self.damage;

    def get_points(self)->object:
        return self.points;

class Villain(Character):
	def set_characterType():
		characterType = 'villain';

	def get_characterType(self)->object:
		return self.characterType;

	def get_damage(self)->object:
		return self.damage;

	def get_health(self)->object:
		return self.health;

	def get_points(self)->object:
		return self.points;

class Hero(Character):
	def set_characterType(self)->None:
		self.characterType = 'hero';

	def get_characterType(self)->object:
		return self.characterType;

	def get_health(self)->object:
		return self.health;

	def get_points(self)->object:
		return self.points;

#Function Comparing the greater of points
def greater_points()->object:
	if characterHero.get_points()>characterVillain.get_points():
		return characterHero;

	elif characterVillain.get_points()>characterHero.get_points():
		return characterVillain;

def generate_Token() -> None:
    keyChar = 0
    key = ""
    while (keyChar < 64):
        keyChar += 1;
        randKey = random.randint(0,9)
        key = key + f"{randKey}";
    return key
#generates user specific key 
def generate_token(points) -> str:
    keyChar = 0;
    key = "";
    average_point_coefficient = major.points/len(questions);
    while (keyChar < 8):
        keyChar += 1;
        #create random key
        rand_key = (random.randint(0,9)*average_point_coefficient*(math.factorial(abs(major.points))/random.randint(1,5)));
        key = key + f"{rand_key}";
    return key;
    

#gets the number of rows in the user list
def GET_ROW_COUNT() -> int:
    with open('users.csv', 'r') as source:
        users = csv.reader(source, delimiter=',');
        row_count = sum(1 for row in users);
    return row_count;

#posts the user to the CSV file
def post_user(name: str, key: str, major: str, list_row="") -> None:
    csv_list = [];
    with open('users.csv', 'r') as source:
        users = csv.reader(source, delimiter=',');
        for row in users:
            csv_list.append(row);
        csv_list.append([f"'{name}'",f"'{key}'", f"'{major}'", f"'{list_row}'"]);
    with open('users.csv', 'w', newline='') as csvfile:
        newWrite = csv.writer(csvfile, delimiter=',');
        newWrite.writerows(csv_list);

def clear_screen() -> None:
    if (platform.system() == "Windows"):
        subprocess.Popen("cls", shell=True).communicate();
    else: 
        print("\033c", end="");

def major_calculator():
    #if the header doesnt exist at line add one
    if (not GET_ROW_COUNT()):
        post_user("Name", "Key", "Major", "Number of Entry")
    global counter;
    counter = 0;
    field = None;
    global major;
    major = Fields(field, 0);
    #clears the terminal
    clear_screen();
    name = input("Hello! What's your name? ")
    clear_screen();
    print("\n\n\nAnswer questions by providing only the number of the answer choice. \n");
    while (counter < len(questions)):
        try:
            clear_screen();
            response = int(input(questions[counter]))-1;
            counter += 1;
            if (not response):
                major.add_points();
            elif (response):
                major.subt_points();
            clear_screen();
        except:
            clear_screen();
            print("Error, please try again\n")
            

#calculate fields
    if (major.points >= (len(questions)-2)):
            major.set_field(fields[0]);
    elif ((len(questions)-4) <= major.points and major.points < (len(questions)-2)):
            major.set_field(fields[4]);
    elif ((len(questions)-6) <= major.points and major.points > (len(questions)-4)):
            major.set_field(fields[1]);
    elif ((len(questions)-8) <= major.points and major.points > (len(questions)-6)):
            major.set_field(fields[3]);
    elif ((len(questions)-16) <= major.points and major.points > (len(questions)-10)):
            major.set_field(fields[2]);
    elif ((len(questions)-17) <= major.points and major.points > (len(questions)-16)):
            major.set_field(fields[6]);
    elif ((len(questions)*(-1)) <= major.points and major.points > (len(questions)-17)):
            major.set_field(fields[5]);
    print(f"Based on your input, a suitable major for you is {major.get_field()}.");
    post_user(name, generate_token(major.points), major.get_field(), GET_ROW_COUNT());


#Main Game body
def game_body()->None:
	rounds = 0;
	print("Welcome to the game! ");
	print("-----------------------------------");
	key = generate_Token();
	print(f"Your unique ID is: {key}");
	print("-----------------------------------");
	global characterHero;
	characterHero = Hero("", 0, 0, 'hero');
	characterHero.health = 100;
	nameHero = input(f"Enter your {characterHero.characterType}'s name: ");
	characterHero.name = nameHero;
	global characterVillain;
	characterVillain = Villain("", 0, 0, 'villain');
	characterVillain.health = 100;
	nameVillain = input(f"Enter your {characterVillain.characterType}'s name: ");
	characterVillain.name = nameVillain;
	moveEffectNum = {"punch": 10, "cast spell": 2, "siege": 1};
#Game loop for 20 rounds
	while (rounds<20):
		rounds += 1;
		heroMove = input(f"What is {characterHero.name}'s move? (Punch, Cast spell, or Siege?) ");
		if (heroMove.lower() == "punch"):
			characterVillain.health -= moveEffectNum[heroMove.lower()];
			characterHero.points += 5;
			print(f"The character stats changed are:\n {characterHero.name}'s points: {characterHero.points}\n {characterVillain.name}'s health: {characterVillain.health}");
			
		elif (heroMove.lower() == "cast spell" or heroMove.lower() == "spell"):
			characterVillain.health -= moveEffectNum[heroMove.lower()];
			characterHero.health += 2;
			print(f"The character stats changed are:\n {characterHero.name}'s points: {characterHero.points}\n {characterVillain.name}'s health: {characterVillain.health}");
			
		elif (heroMove.lower() == "siege"):
			if (characterVillain.get_points()>=1):
				characterVillain.points -= moveEffectNum[heroMove.lower()];
			characterHero.points += 1;
			print(f"The character stats changed are:\n {characterHero.name}'s points: {characterHero.points}\n {characterVillain.name}'s points: {characterVillain.points}");

		if (characterVillain.get_health() <= 0):
			print(f"Hero wins because {characterVillain.name}'s health fell below 0");
			break;
			
		villainMove = input(f"What is {characterVillain.name}'s move? (Punch, Cast spell, or Siege?) ");
		if (villainMove.lower() == "punch"):
			characterHero.health -= moveEffectNum[villainMove.lower()];
			characterVillain.points += 5;
			print(f"The character stats changed are:\n {characterHero.name}'s points: {characterVillain.points}\n {characterHero.name}'s health: {characterHero.health}");
			
		elif (villainMove.lower() == "cast spell" or villainMove.lower() == "spell"):
			characterHero.health -= moveEffectNum[villainMove.lower()];
			characterVillain.health += 2;
			print(f"The character stats changed are:\n {characterHero.name}'s points: {characterHero.points}\n {characterVillain.name}'s health: {characterVillain.health}");
			
		elif (villainMove.lower() == "siege"):
			if (characterHero.get_points() >= 1):
				characterHero.points -= moveEffectNum[villainMove.lower()];
			characterVillain.points += 1;
			print(f"The character stats changed are:\n {characterHero.name}'s points: {characterHero.points}\n {characterVillain.name}'s points: {characterVillain.points}");
		if (characterHero.get_health() <= 0):
			print(f"Villain wins because {characterHero.name}'s health fell below 0");
			break;
#What to do if 20 rounds pass and both character's healths are above 0
	greaterPoints = greater_points()
	if (rounds >= 20):
		print(f"{greaterPoints.name} wins the game with {greaterPoints.points}");

def main():
    print("--------------------------------------\n");
    print("|  Welcome to the student interface  |\n");
    print("|          Do you want to:           |\n");
    print("|          1. Take the quiz          |\n");
    print("|          2. Play a game            |\n");
    print("--------------------------------------\n");
    print("Response (1 or 2): ")
    response = input();
    if ("1" == response):
        major_calculator();
    elif (response == "2"):
        game_body();
    else:
        print("Choose either 1 or 2. ")
        time.sleep(5);
        os.execv(sys.executable, ['python3'] + sys.argv);
        
if __name__ == "__main__":
    main();