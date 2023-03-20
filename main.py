from organization import Organization
from project import Project
from activity import ActivityLog, Activity

def main() :
    organization_1 = Organization("KMITL")
    project_1 = Project("Project1", "project1", "20-03-2023", "20-03-2023")
    organization_1.add_project(project_1)
    organization_1.create_project("Sleep", "Relax", "15-03-2023", "20-03-2023")
    organization_1.show_projects()

    activity_log_1 = ActivityLog()
    activity_1 = Activity("Testing", "20-03-2023", "Adam")
    activity_log_1.save_activity(activity_1)
    activity_log_1.show_activity()

if __name__ == "__main__" :
    main()