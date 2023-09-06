<!DOCTYPE html>
<html>

<head>
    <title>Leader Cabling DB</title>
    <!-- The 'head' section of the HTML document defines metadata about the page. -->
    <!-- It sets the title of the page and includes an external CSS stylesheet. -->

    <link type="text/css" href="/static/main_style.css" rel="stylesheet">
    <!-- This line links an external CSS file named 'main_style.css' to style the page. -->
</head>

<body>
    <!-- The 'body' section contains the visible content of the web page. -->

    <h1>Home Page</h1>
    <!-- This is a top-level heading, displaying "Home Page" on the web page. -->

    <div class='topnav' style="margin-bottom: 20px;">
        <!-- This is a navigation menu with links to different sections of the website. -->
        <a href="/admin">Admin</a>
        <!-- A link to the "Admin" section of the website. -->
        <a href="/docs">Documents</a>
        <!-- A link to the "Documents" section of the website. -->
        <a href="/profile">Profiles</a>
        <!-- A link to the "Profiles" section of the website. -->
        <a href="/schedule">Schedule</a>
        <!-- A link to the "Schedule" section of the website. -->
        <a href="/job">Jobs</a>
        <!-- A link to the "Jobs" section of the website. -->
    </div>

    <div class="querySection">
        <!-- This section contains a query form for user interaction. -->
        <div class="queryForm">
            <!-- This is a form element where users can input data and submit it. -->
            <form action="/personal" method="POST">
                <!-- The form is configured to send a POST request to the "/personal" route. -->

                Enter personal ID for relevant information on file.<br />
                <!-- This is an instruction to the user. -->
                Enter the ID: <input type="text" name="personal_id_value" required/><br />
                <!-- This is an input field where users can enter a personal ID. -->
                <button type="submit">Search</button>
                <!-- This is a button that, when clicked, submits the form data. -->
            </form>
        </div>
    </div>

</body>

</html>
