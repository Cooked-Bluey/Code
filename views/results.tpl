<!DOCTYPE html>
<html>
    <head>
        <title>Fuel Watch Database</title>
        <link type="text/css" href="/static/main_style.css" rel="stylesheet">
    </head>

<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>

    <body>


        <h1>{{ title }}</h1>
        <p>{{ description }}</p>
        <header>
            <p><a href="/">Return to Home Page</a></p>
            <button onclick="history.back()">Back</button>
        </header>
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
            <button onclick="history.back()">Back</button>
            <p><a href="/">Return to Home Page</a></p>
        </footer>
    </body>
</html>