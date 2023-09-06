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
        <header style = "margin-bottom: 20px;">
            <p><a href="/">Return to Home Page</a></p>
            <button onclick="history.back()">Back</button>
        </header>


        <div class="querySection">
            <div class="queryForm">
                <form action="/scheduleUpdate" method="POST">

                    <div class="container">
                        <p>Monday</p>
                        <p>Tuesday</p>
                        <p>Wednesday</p>
                        <p>Thursday</p>
                        <p>Friday</p>
                        <p>Saturday</p>
                        <p>Sunday</p>
                    
                    <select name="Monday_Update" required>
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                    <select name="Tuesday_Update" required>
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                    <select name="Wednesday_Update" required>
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                    <select name="Thursday_Update" required>
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                    <select name="Friday_Update" required>
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                    <select name="Saturday_Update" required>
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                    <select name="Sunday_Update" required>
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                    </div>
                    Enter the staff ID to update the availability for an employee.<br />
                    Enter ID: <input type="text" name="Editing_staff_id" required/><br />
                    <button type ="submit">Enter</button>
                </form>
            </div>
        </div>
        
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

<script>
        function changeTextColors(node) {
            if (node.nodeType === Node.TEXT_NODE) {
                const text = node.textContent;
                const replacedText = text
                    .replace(/Yes/gi, '<span style="color: green;">Yes</span>')
                    .replace(/No/gi, '<span style="color: red;">No</span>');

                const tempElement = document.createElement('div');
                tempElement.innerHTML = replacedText;

                node.parentNode.replaceChild(tempElement.firstChild, node);
            } else if (node.nodeType === Node.ELEMENT_NODE) {
                // Recursively process child nodes
                node.childNodes.forEach(changeTextColors);
            }
        }
        const body = document.body;
        changeTextColors(body);
    </script>


        <footer>
            <button onclick="history.back()">Back</button>
            <p><a href="/">Return to Home Page</a></p>
        </footer>
    </body>
</html>