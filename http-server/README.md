# Simple python server

## Test task

Client side provided in the form of HTML template with a form, comprising:

- text input
- 1-file input
- multi-file input
- css and js naturally

Necessary to implement the server part, which would:

- correctly displays the client side
- was able to accept the AJAX request sent by the form
- correctly parse it
- and save data to disk

The backend needs to be implemented on the standard http.server library.

## Usage

Make sure you have Python3 installed.

Run `main.py` file in the top folder.

Open `localhost:8000` in a web browser, fill out the form and submit.

The content of the form will be written in your storage in the temp folder of this project.

Submitting the form with the same data will result in overwriting previous data.
