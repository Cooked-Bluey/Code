# These are SQL queries written in Python. Each query is a string that represents a specific SQL
# statement.

# Query to select all documents from the 'CurrentDoc' table and alias the columns for clarity.
SELECT_ALL_FROM_CURRENTDOC = '''SELECT CurrentDoc_id as Number, text as Documents FROM CurrentDoc
'''

# Query to select all documents from the 'PastDoc' table and alias the columns for clarity.
SELECT_ALL_FROM_PASTDOC = '''SELECT PastDoc_id as Number, text2 as Documents FROM PastDoc'''

# Query to select relevant data from the 'MainOffice' table, including information from related tables 'CurrentDoc' and 'PastDoc'.
SELECT_REQU_FROM_MAINOFFICE = '''SELECT MainOffice.Current_Client_First_Name as Name, 
                                    MainOffice.Current_Client_Last_Name as Lastname, 
                                    PastDoc.text2 as Documents, 
                                    MainOffice.Potential_Jobs as Contenders, 
                                    CurrentDoc.text as Documents 
                                FROM MainOffice 
                                INNER JOIN CurrentDoc ON MainOffice.CurrentDoc_id = CurrentDoc.CurrentDoc_id
                                INNER JOIN PastDoc ON MainOffice.PastDoc_id = PastDoc.PastDoc_id'''

# Query to select all records from the 'Employee' table.
SELECT_REQU_FROM_EMPLOYEE = '''SELECT * FROM Employee
'''

# Query to select schedule data for all staff members from the 'Employee' table.
SELECT_REQU_FROM_SCHEDULE = '''SELECT employee_id as StaffID, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday FROM Employee'''

# Query to select job-related data from the 'Job' and 'Team' tables, joining them based on team_id.
SELECT_REQU_FROM_JOB = '''SELECT Job.Job_id as Number, Job.Name, Job.Cost as Cost$, Job.Description, 
                            Team.Name as Team, Team.Size, Team.Description 
                        FROM Job
                        INNER JOIN Team ON Job.team_id = Team.Team_id'''

# Query to select personal information for a staff member based on their 'employee_id'.
SELECT_PERSONAL_INFO = '''SELECT employee_id as StaffID, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday 
                        FROM Employee 
                        WHERE Employee.employee_id = :personal_id_value
'''

# Query to update staff availability in the 'Employee' table based on 'employee_id'.
EDIT_STAFF_AVAILABILITY = '''   
UPDATE Employee
SET Monday = :Monday_Update,
    Tuesday = :Tuesday_Update,
    Wednesday = :Wednesday_Update,
    Thursday = :Thursday_Update,
    Friday = :Friday_Update,
    Saturday = :Saturday_Update,
    Sunday = :Sunday_Update
WHERE Employee.employee_id = :Editing_staff_id;'''

# Query to show the updated schedule for a specific staff member based on 'employee_id'.
SHOW_EDITED_SCHEDULE ='''SELECT employee_id as StaffID, 
                            Monday, 
                            Tuesday, 
                            Wednesday, 
                            Thursday, 
                            Friday, 
                            Saturday, 
                            Sunday 
                        FROM Employee
                        WHERE Employee.employee_id = :Editing_staff_id;
'''
