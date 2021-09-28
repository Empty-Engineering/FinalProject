

class Fields:
    def __init__(self, field: str, specialty: str):
        self.field = field;
        self.specialty = specialty;

    def get_field(self):
        return self.field;

    def set_field(self, field_name: str):
         setattr(self.field, 'field', field_name);

def main():
    newMajor = Fields('stem', 'engineering');
    newMajor.set_field('law');
    print(newMajor.field);
main()