#This is a Python web application that uses the Bottle framework to create routes and templates for
#different pages, and interacts with a SQLite database to retrieve and update data.
#:return: The code is returning a web application that uses the Bottle framework. It sets up routes
#or different pages such as '/docs', '/', '/profile', '/schedule', '/currentDocs', '/PastDocs',
#'/admin', '/profile', '/job', '/scheduleUpdate', '/personal', and '/static/<filename>'. It also
#includes functions to run SQL queries and retrieve data from the database. The application runs

from bottle import *
import sqlite3
import Queries

import DB_Builder as DBB
import insert_data as ID

database_name = 'Leader_Cabling_DB.db'
DATABASE_FILE = 'Leader_Cabling_DB.db'

DBB.create_db(database_name)
ID.insert_table_data(database_name)

conn = sqlite3.connect(database_name)
cursor = conn.cursor()

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
    query = Queries.SELECT_ALL_FROM_CURRENTDOC
    return get_template(query, title, description)

@route('/PastDocs')
def select_PastDocs():
    title = 'All Past Documents'
    description = 'These are documents from previous projects that can be used fro reference.'
    query = Queries.SELECT_ALL_FROM_PASTDOC
    return get_template(query, title, description)

@route('/admin')
def select_MainOffice():
    title = 'Admin'
    description = 'This where all ongoing and potential clients are kept track of.'
    query = Queries.SELECT_REQU_FROM_MAINOFFICE
    return get_template(query, title, description)

@route('/profile')
def select_profile():
    title = 'Profiles'
    description = 'This is a repository of all current staff.'
    query = Queries.SELECT_REQU_FROM_EMPLOYEE
    return get_template(query, title, description)

@route('/job')
def select_job():
    title = 'Jobs'
    description = 'These are all the ongoing jobs and their related teams.'
    query = Queries.SELECT_REQU_FROM_JOB
    return get_template(query, title, description)

@route('/schedule')
def select_schedule():
    title = 'Schedule'
    description = 'This is the boarder work schedule with all the staff with colour coordination.'
    query = Queries.SELECT_REQU_FROM_SCHEDULE
    return get_template(query, title, description)

@route('/scheduleUpdate', method=['GET', 'POST'])
def Show_Update():
    title = 'Updated schedule'
    description = 'Stuff.'
    query = Queries.SHOW_EDITED_SCHEDULE
    return get_template(query, title, description)

def Update_Schedule():
    if request.method == 'POST':
        Editing_staff_id = request.forms.get('Editing_staff_id')        
        Monday_Update = request.forms.get('Monday_Update')
        Tuesday_Update = request.forms.get('Tuesday_Update')
        Wednesday_Update = request.forms.get('Wednesday_Update')
        Thursday_Update = request.forms.get('Thursday_Update')
        Friday_Update = request.forms.get('Friday_Update')
        Saturday_Update = request.forms.get('Saturday_Update')
        Sunday_Update = request.forms.get('Sunday_Update')

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

        title = f"Updating {Editing_staff_id}'s availability."
        description = f'Updating the availability for staff member: {Editing_staff_id}'
        query = Queries.EDIT_STAFF_AVAILABILITY

        # Update the availability
        run_query_with_parameters(query, values)

        # After updating, show the updated schedule
        updated_schedule = Show_Update()

        return updated_schedule, title, description

    elif request.method == 'GET':
        return 'This is a GET request'
    else:
        return "This route only accepts POST requests."

@route('/personal', method= 'POST')
def select_personal():
    personal_id_value = request.forms.get('personal_id_value')
    values = {'personal_id_value': personal_id_value }
    title = f'Personal ID: {personal_id_value}'
    description = f'This shows you all relevant information for staff member: {personal_id_value}.'
    query = Queries.SELECT_PERSONAL_INFO
    return get_template_with_parameters(query, values, title, description)
    


@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='./static')

def get_db_connection():
    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.Row
    return connection

def run_query(query):
    return run_query_with_parameters(query, {})

def run_query_with_parameters(query, values):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(query, values)
    result = cursor.fetchall()

    connection.close()

    return result

def get_template(query, title='Query Results', description='This page shows the results of a query'):
    return get_template_with_parameters(query, {}, title, description)

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



run(host='localhost', port=8081, debug=True, reloader=True)





