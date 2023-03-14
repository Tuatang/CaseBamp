from organization import Organization
from user import User

def main() :
    organization_1 = Organization("KMITL")
    user_1 = User("koonmartza123@gmail.com", "thanathat p.", "092xxxxxxx")
    user_1.create_project("Testing", "test", "26-03-2023", "30-03-2023")
    organization_1.show_projects()

if __name__ == "__main__" :
    main()