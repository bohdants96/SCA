# SCA

To run local, set up all packages by next command:

`pip install-r requirements.txt`

Run migrations for database:

`python manage.py migrate`

And start your server with command:

`python manage.py runserver`


## API Endpoints Documentation

### SpyCat Endpoints

- List all SpyCats: `GET /spycat/` - Retrieves a list of all SpyCat records.

- Create a new SpyCat: `POST /spycat/` - Creates a new SpyCat record.

- Retrieve a single SpyCat by ID: `GET /spycat/{id}/` -Retrieves detailed information of a specific SpyCat by its ID.

- Update a SpyCat: `PUT /spycat/{id}/` - Updates the details of a specific SpyCat by its ID.

- Delete a SpyCat: `DELETE /spycat/{id}/` - Deletes a specific SpyCat by its ID.

### Mission Endpoints

- List all Missions: `GET /missions/` - Retrieves a list of all Mission records.

- Create a new Mission: `POST /missions/` - Creates a new Mission record. This can include creating multiple targets within the mission.

- Retrieve a single Mission by ID: `GET /missions/{id}/` - Retrieves detailed information of a specific Mission by its ID.

- Update a Mission: `PUT /missions/{id}/` - Updates the details of a specific Mission by its ID.

- Delete a Mission: `DELETE /missions/{id}/` - Deletes a specific Mission by its ID. A mission cannot be deleted if it is assigned to a SpyCat.

### Mission Target Endpoints

- Update Target for a Mission: `PATCH /missions/{mission_id}/update_target/{target_id}/` - Updates the specified target in a given mission. You can update notes or other details of a target, provided the mission or the target is not completed.

- Assign a SpyCat to a Mission: `PATCH /missions/{mission_id}/assign_cat/` - Assigns a SpyCat to a specific mission. You need to provide a cat_id in the request body to assign the cat.

Postman: https://www.postman.com/research-participant-34424700/workspace/sca-django