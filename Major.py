import subprocess, platform, random, csv, math
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

#generates user specific key 
def generate_token(points) -> str:
    keyChar = 0;
    key = "";
    average_point_coefficient = major.points/len(questions);
    while (keyChar < 8):
        keyChar += 1;
        #create random key
        rand_key = (random.randint(0,9)*average_point_coefficient*(math.factorial(major.points)/random.randint(1,5)));
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

def main():
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

main()
