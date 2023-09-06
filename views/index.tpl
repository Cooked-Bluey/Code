<!DOCTYPE html>
<html>

    <head>
        <title>My First App</title>
        <link type="text/css" href="/static/main_style.css" rel="stylesheet">

    </head>
<style>

</style>
    <body>
        <h1>Home Page</h1>
        <div class = 'topnav' style="margin-bottom: 20px;">
            <a href="/admin">Admin</a>
            <a href="/docs">Documents</a>
            <a href="/profile">Profiles</a>
            <a href="/schedule">Schedule</a>
            <a href="/job">Jobs</a>
        </div>

        <div class="querySection">
            <div class="queryForm">
                <form action="/personal" method="POST">
                    Enter personal ID for relevant information on file.<br />
                    Enter the ID: <input type="text" name="personal_id_value" required/><br />
                    <button type ="submit">Search</button>
                </form>
            </div>
        </div>

    </body>
</html>