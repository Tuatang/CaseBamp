from organization import Organization

def main() :
    organization_1 = Organization("KMITL")
    organization_1.create_project("Sleep", "Relax", "15-03-2023", "20-03-2023")
    organization_1.get_project()
    organization_1.show_projects()

if __name__ == "__main__" :
    main()