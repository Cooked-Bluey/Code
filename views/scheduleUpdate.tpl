<!DOCTYPE html>
<html>

    <head>
        <title>My First App</title>
        <link type="text/css" href="static/style.css" rel="stylesheet">

    </head>

    <body>
        <header>
            <p><a href="/">Return to Home Page</a></p>
            <input type="button" value="Back" onclick="history.back()">
        </header>
        <h1>{{ title }}</h1>
        <p>{{ description }}</p>

        <table>
            <tr>
                % for field in records[0].keys():
                <th> {{ field }} </th>
                % end
            </tr>
            % for record in records:
            <tr>
                % for field in record:
                <td>{{ field }}</td>
                % end
            </tr>
            % end
        </table>
        <footer>
            <input type="button" value="Back" onclick="history.back()">
            <p><a href="/">Return to Home Page</a></p>
        </footer>
    </body>
</html>