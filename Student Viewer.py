#Lukas Robin
#19.10.2021
#All rights retained herein
#Program views student information
import ctypes, csv, hashlib, os, platform, sys, time
class User:
    def __init__(self, password):
        self.password = password;

    def get_password():
        return self.password;

def set_password(new_pass):
    password = [SHA512(new_pass)];
    with open('useraccess.csv', 'w', newline='') as csvfile:
        newWrite = csv.writer(csvfile, delimiter=',');
        newWrite.writerow(password);
def SHA512(io):
    encode_pass = io.encode();
    return hashlib.sha512(encode_pass).hexdigest();

def verification(user):
    csv_list = []
    with open('useraccess.csv', 'r') as source:
        useraccess = csv.reader(source, delimiter=',')
        for row in useraccess:
            csv_list.append(row)
    return any(user in x for x in csv_list)

def show_results() -> None:
    data = []
    with open('users.csv', 'r') as source:
        users = csv.reader(source, delimiter=',')
        for row in users:
            print(row)

def clear_screen():
    if (platform.system() == "Windows"):
        subprocess.Popen("cls", shell=True).communicate();
    else: 
        print("\033c", end="");

def main():
    clear_screen();
    user = User(
        input("Enter your password: ")
        );
    hash = SHA512(user.password)
    if (verification(hash)):
        if (SHA512(user.password) == "b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86"):
            clear_screen();
            print("You are currently using the default password, please change the password. \n");
            new_pass1 = input("Enter your new password: ");
            new_pass2 = input("Please re-enter your new password. \n");
            if (new_pass1 == new_pass2):
                set_password(new_pass1);
                os.execv(sys.executable, ['python3'] + sys.argv);
            else: 
                print("Passwords do not match, try again. ");
                time.sleep(5);
                os.execv(sys.executable, ['python3'] + sys.argv);
        else:
            clear_screen();
            print("--------------------------------------\n");
            print("|   Welcome to the admin interface   |\n");
            print("|  Do you want to view quiz results? |\n");
            print("--------------------------------------\n");
            response = input("Y/n: ");
            if (response.lower() == 'y' or response.lower() == 'yes'):
                clear_screen();
                show_results();
            else:
                exit();
    else:
        os.execv(sys.executable, ['python3'] + sys.argv);
main()