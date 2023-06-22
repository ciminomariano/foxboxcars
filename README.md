# Foxbox Digital - Python Engineer Challenge


## Technical Requirements

- Django: 3.x
- SQLite: 3.x
- Bootstrap: 4.x
- Vanilla JS or JQuery
- Class-Based Views
- Form and Formset
- Pytest for testing


## Project Description

This project is a web application for managing cars, developed using Django as the back-end framework.

### Management Panel

The management panel is the main page of the application. It displays a list of existing cars and provides buttons to create new cars and start the update process. The columns in the panel correspond to fields in the Car model, with the exception of the Total column, which represents the sum of Production Costs and Transportation Costs.

### Add Car Page

The Add Car page allows users to create a new car. It contains several fields, as shown in the example below. All fields in the form are required, and if there are any validation errors upon saving the form, they should be displayed to the user. The Model field is an open-text field, while Brand and Main Color are choice fields. Value, Production Costs, and Transportation Costs are integer fields.

### Update Action

When the user initiates the Update action:
- The table becomes editable, with each cell transformed into an editable field for batch updating of cars (excluding the Total column).
- The Update button is hidden, while the Cancel and Save buttons are displayed.
- Clicking the Cancel button refreshes the page.
- Changing the Production Costs or Transportation Costs fields dynamically updates the Total column to display the sum of these two columns.
- Upon saving the changes, the modifications should be persisted, and the user should be redirected to the management panel in read mode.

## Local Environment Setup

1. Clone the repository:
git clone https://github.com/ciminomariano/foxboxcars



2. Create and activate a virtual environment:
python3 -m venv myenv
source myenv/bin/activate



3. Install the project dependencies:
pip install -r requirements.txt


4. Apply the database migrations:
python manage.py migrate


## Running the Project

To run the project, use the following command:
python manage.py runserver


The project will be available at `http://localhost:8000/`.

## Running Tests

To run the tests, use the following command:
Go to the project folder /carsapp/src/foxboxcars
and run the command pytest tests

This will execute all the tests defined in the `tests` directory.

If you have any further questions or need additional assistance,
please don't hesitate to ask to ciminomariano@gmail.com .