from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Interactive JavaScript Tasks</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            margin-bottom: 20px;
        }
        input, button {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <h1>JavaScript Interaction Tasks</h1>

    <!-- Task 4: Paragraph to update with user's message -->
    <p id="userMessage">Your message will appear here.</p>

    <!-- Task 8: Display full name -->
    <h1 id="fullNameDisplay"></h1>

    <!-- Task 6: Form to display alert with input value -->
    <form id="alertForm">
        <label for="alertInput">Enter text for alert:</label><br>
        <input type="text" id="alertInput" required>
        <button type="submit">Show Alert</button>
    </form>

    <!-- Task 7: Form to change background color -->
    <form id="colorForm">
        <label for="colorPicker">Choose background color:</label><br>
        <input type="color" id="colorPicker" value="#ffffff">
        <button type="submit">Change Background</button>
    </form>

    <!-- Task 8: Form to display full name in h1 -->
    <form id="nameForm">
        <label for="firstNameInput">First Name:</label><br>
        <input type="text" id="firstNameInput" required><br>
        <label for="lastNameInput">Last Name:</label><br>
        <input type="text" id="lastNameInput" required><br>
        <button type="submit">Display Full Name</button>
    </form>

    <script>
        // Task 2: Prompt for favorite hobby and display in alert
        const hobby = prompt("What is your favorite hobby?");
        if (hobby) {
            alert("Your favorite hobby is: " + hobby);
        }

        // Task 3: Prompt for first and last name, concatenate, and display in alert
        const firstName = prompt("Enter your first name:");
        const lastName = prompt("Enter your last name:");
        if (firstName && lastName) {
            alert("Your full name is: " + firstName + " " + lastName);
        }

        // Task 4: Prompt for a message and update a <p> element's text content
        const message = prompt("Enter a message to display on the page:");
        if (message) {
            document.getElementById("userMessage").textContent = message;
        }

        // Task 5: Prompt for favorite emoji and display in alert with thank you message
        const emoji = prompt("What's your favorite emoji?");
        if (emoji) {
            alert("Thanks! You chose: " + emoji);
        }

        // Task 5 (continued): Prompt for a word and set it as the page title
        const newTitle = prompt("Enter a word to set as the page title:");
        if (newTitle) {
            document.title = newTitle;
        }

        // Task 6: Form to display alert with input value
        document.getElementById("alertForm").addEventListener("submit", function(event) {
            event.preventDefault();
            const inputValue = document.getElementById("alertInput").value;
            alert("You entered: " + inputValue);
        });

        // Task 7: Form to change background color
        document.getElementById("colorForm").addEventListener("submit", function(event) {
            event.preventDefault();
            const selectedColor = document.getElementById("colorPicker").value;
            document.body.style.backgroundColor = selectedColor;
        });

        // Task 8: Form to display full name in h1
        document.getElementById("nameForm").addEventListener("submit", function(event) {
            event.preventDefault();
            const firstName = document.getElementById("firstNameInput").value;
            const lastName = document.getElementById("lastNameInput").value;
            document.getElementById("fullNameDisplay").textContent = firstName + " " + lastName;
        });
    </script>
</body>
</html>
''')

if __name__ == '__main__':
    app.run(debug=True)
