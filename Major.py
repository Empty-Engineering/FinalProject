import subprocess, platform, random, csv, math




fields = ['STEM', 'Law', 'Medicine', 'Social Sciences', 'Business', 'Education', 'Communications'];
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

def generate_token() -> str:
    keyChar = 0;
    key = "";
    while (keyChar < 8):
        keyChar += 1;
        randKey = random.randint(0,9);
        key = key + f"{math.pow(randKey,random.randint(0,5))}";
    return key;
    


def GET_ROW_COUNT() -> int:
    with open('users.csv', 'r') as source:
        users = csv.reader(source, delimiter=',');
        row_count = sum(1 for row in users);return row_count;

def post_user(name: str, key: str, major: str) -> None:
    csv_list = [];
    rowCount = GET_ROW_COUNT();
    with open('users.csv', 'r') as source:
        users = csv.reader(source, delimiter=',');
        for row in users:
            csv_list.append(row);
            csv_list.append([f"'{name}'",f"'{key}'", f"'{major}'", f"'{rowCount}'"]);
    with open('users.csv', 'w', newline='') as csvfile:
        newWrite = csv.writer(csvfile, delimiter=',');
        newWrite.writerows(csv_list);

def main():
    global counter;
    counter = 0;
    field = None;
    major: object = Fields(field, 0);
    if (platform.system() == "Windows"):
        subprocess.Popen("cls", shell=True).communicate();
    else: 
        print("\033c", end="");
    name = input("Hello! What's your name? ")
    if (platform.system() == "Windows"):
        subprocess.Popen("cls", shell=True).communicate();
    else: 
        print("\033c", end="");
    print("\n\n\nAnswer questions by providing only the number of the answer choice. \n");
    while (counter < len(questions)):
        try:
            if (platform.system() == "Windows"):
                subprocess.Popen("cls", shell=True).communicate();
            else: 
                print("\033c", end="");
            response = int(input(questions[counter]))-1;
            counter += 1;
            if (not response):
                major.add_points();
            elif (response):
                major.subt_points();
            if (platform.system() == "Windows"):
                subprocess.Popen("cls", shell=True).communicate();
            else: 
                print("\033c", end="");
        except:
            if (platform.system() == "Windows"):
                subprocess.Popen("cls", shell=True).communicate();
            else: 
                print("\033c", end="");
            print("Error, please try again\n")
            


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
    post_user(name, generate_token(), major.get_field())
    
main()