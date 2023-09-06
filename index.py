# Import necessary modules
from bottle import *
import sqlite3
import Queries  # Import custom queries module
import DB_Builder as DBB  # Import custom database builder module
import insert_data as ID  # Import custom data inserter module

# Define the database file name
database_name = 'Leader_Cabling_DB.db'
DATABASE_FILE = 'Leader_Cabling_DB.db'

# Create the database and insert initial data
DBB.create_db(database_name)
ID.insert_table_data(database_name)

# Establish a connection to the SQLite database
conn = sqlite3.connect(database_name)
cursor = conn.cursor()

# Function to handle updating the staff schedule
def Update_Schedule():
    # Get form data
    Editing_staff_id = request.forms.get('Editing_staff_id')        
    Monday_Update = request.forms.get('Monday_Update')
    Tuesday_Update = request.forms.get('Tuesday_Update')
    Wednesday_Update = request.forms.get('Wednesday_Update')
    Thursday_Update = request.forms.get('Thursday_Update')
    Friday_Update = request.forms.get('Friday_Update')
    Saturday_Update = request.forms.get('Saturday_Update')
    Sunday_Update = request.forms.get('Sunday_Update')

    # Prepare query parameters
    values = {
        'Editing_staff_id': Editing_staff_id,
        'Monday_Update': Monday_Update,
        'Tuesday_Update': Tuesday_Update,
        'Wednesday_Update': Wednesday_Update,
        'Thursday_Update': Thursday_Update,
        'Friday_Update': Friday_Update,
        'Saturday_Update': Saturday_Update,
        'Sunday_Update': Sunday_Update
    }
    query = Queries.EDIT_STAFF_AVAILABILITY  # Get the SQL query for updating availability
    return query  # Return the SQL query

# Define routes for different pages
@route('/docs')
def docs(): 
    return template('docs') 

@route('/')
def index():
    return template('index') 

@route('/profile')
def profile():
    return template('profile') 

@route('/schedule')
def schedule():
    return template('schedule') 

@route('/currentDocs')
def select_CurrentDocs():
    title = 'All Current Documents'
    description = 'All Documents that are currently relevant to ongoing projects.'
    query = Queries.SELECT_ALL_FROM_CURRENTDOC  # Get the SQL query for selecting current documents
    return get_template(query, title, description)

@route('/PastDocs')
def select_PastDocs():
    title = 'All Past Documents'
    description = 'These are documents from previous projects that can be used for reference.'
    query = Queries.SELECT_ALL_FROM_PASTDOC  # Get the SQL query for selecting past documents
    return get_template(query, title, description)

@route('/admin')
def select_MainOffice():
    title = 'Admin'
    description = 'This is where all ongoing and potential clients are kept track of.'
    query = Queries.SELECT_REQU_FROM_MAINOFFICE  # Get the SQL query for selecting main office data
    return get_template(query, title, description)

@route('/profile')
def select_profile():
    title = 'Profiles'
    description = 'This is a repository of all current staff.'
    query = Queries.SELECT_REQU_FROM_EMPLOYEE  # Get the SQL query for selecting employee profiles
    return get_template(query, title, description)

@route('/job')
def select_job():
    title = 'Jobs'
    description = 'These are all the ongoing jobs and their related teams.'
    query = Queries.SELECT_REQU_FROM_JOB  # Get the SQL query for selecting job data
    return get_template(query, title, description)

@route('/schedule')
def select_schedule():
    title = 'Schedule'
    description = 'This is the broader work schedule with all the staff with color coordination.'
    query = Queries.SELECT_REQU_FROM_SCHEDULE  # Get the SQL query for selecting the schedule
    return get_template(query, title, description)

# Route for updating the schedule (GET and POST)
@route('/scheduleUpdate', method=['GET', 'POST'])
def Show_Update():
    # Call the Update_Schedule function to get the SQL query
    Update_Schedule()
    title = 'Updated schedule'
    description = 'Stuff.'
    query = Queries.SHOW_EDITED_SCHEDULE  # Get the SQL query for showing the edited schedule
    return get_template(query, title, description)

# Route for selecting personal information (POST)
@route('/personal', method= 'POST')
def select_personal():
    personal_id_value = request.forms.get('personal_id_value')
    values = {'personal_id_value': personal_id_value }
    title = f'Personal ID: {personal_id_value}'
    description = f'This shows you all relevant information for staff member: {personal_id_value}.'
    query = Queries.SELECT_PERSONAL_INFO  # Get the SQL query for selecting personal information
    return get_template_with_parameters(query, values, title, description)

# Route for serving static files
@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='./static')

# Function to establish a database connection
def get_db_connection():
    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.Row
    return connection

# Function to run a query
def run_query(query):
    return run_query_with_parameters(query, {})

# Function to run a query with parameters
def run_query_with_parameters(query, values):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(query, values)
    result = cursor.fetchall()

    connection.close()

    return result

# Function to get a template
def get_template(query, title='Query Results', description='This page shows the results of a query'):
    return get_template_with_parameters(query, {}, title, description)

# Function to get a template with parameters
def get_template_with_parameters(query, values, title='Query Results', description='This page shows the results of a query'):
    result = run_query_with_parameters(query, values)
    if title == 'Schedule':
        page = template('schedule', title=title, description=description, records=result)
    elif title == 'personal':
        page = template('personal', title=title, description=description, records=result)
    elif len(result) > 0:
        page = template('results', title=title, description=description, records=result)
    else:
        page = template('no_results', title=title, description=description)

    return page

# Run the Bottle web application
run(host='localhost', port=8081, debug=True, reloader=True)
