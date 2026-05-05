# Rep Register ![dumbell](/static/images/favicon-32x32.png)
## 💻 Developer
[Rehanon Mackenzie](https://github.com/Rehanon-Mackenzie)
<br>
![GitHub last commit](https://img.shields.io/github/last-commit/rehanon-mackenzie/rep-register?style=for-badge&color=red) ![GitHub contributors](https://img.shields.io/github/contributors/rehanon-mackenzie/rep-register?style=for-badge&color=orange) ![GitHub language count](https://img.shields.io/github/languages/count/rehanon-mackenzie/rep-register?style=for-badge&color=yellow) ![GitHub top language](https://img.shields.io/github/languages/top/rehanon-mackenzie/rep-register?style=for-badge&color=green) ![Deployment](https://img.shields.io/badge/deployment-heroku-purple)
Rep Register is a full-stack web application designed to allow users to store, track and manage weight training workouts over time.  It provides users full CRUD functionality, user authentication and a structured relational database to support workout progression tracking.

![Rep Register responsive image](/static/images/rep-register-responsive.PNG)
Visit the deployed site: [Rep Register](https://rep-register-0917d4849eb9.herokuapp.com/)

## Instructions
**User:**
* You will be asked to register with a username and password.
* You will then be taken through to your workouts dashboard where you can add your workouts.
* You will be asked to enter the name of the exercise you are adding, the weight you have lifted,  the number of reps of the exercise you have done and the number of sets you have completed.  The app will automatically calculate the volume you have lifted and input the date are adding the workout.
* You can edit or delete a workout by clicking on the action buttons for that workout.

## Table of Contents
* [Rep Register](#rep-register)
    * [Instructions](#instructions)
    * [Table of Contents](#table-of-contents)
    * [About](#about)
    * [User Experience](#user-experience-ux)
    * [Design](#design)
    * [Testing](#testing)
    * [Deployment & Local Development](#deployment--local-development)
    * [Credits](#credits)
    * [Acknowledgements](#acknowledgements)
    

## About
Rep Register was developed to provide users an automated way to track their workouts and enhance their fitness journey.  Care was taken to ensure that the input of data was simple to make sure users aren't disturbed during their workouts.

The current iteration has been developed to allow users to manage their workout data with full CRUD functionality.  Future iterations will expand user experience by developing programmable rest timers, user designed workout templates, fitness analytics etc.

It's commonly understood when progress is tracked improvement occurs and Rep Register enables ever users just beginning on their fitness journey to see how they are improving.

## User Experience (UX)
This section documents the decisions made in the planning phase of the build.  I applied Agile methodology to plan this build.  Specifically, I used GitHub Issues and a Kanban board to plan out the requirements and worked with MoSCoW prioritisation method to create a minimum viable product.  This allowed me to think of what was absolute necessary in this iteration of the app and what could be developed in future versions.

![Project Board](/documentation/planning/project-board.PNG)

### User Stories
| Target | Expectation | Outcome | Classification|
| ---- | ----| ---- | ---- |
| As a user | I want to register and login | so that I can securely access my workouts | ![Must Have](https://img.shields.io/badge/Must_Have-brightgreen) |
| As a logged-in user | I want to add a workout | so that I can track my progress | ![Must Have](https://img.shields.io/badge/Must_Have-brightgreen) |
| As a user | I want to edit my workouts | so that I can correct or update data | ![Must Have](https://img.shields.io/badge/Must_Have-brightgreen) |
| As a user | I want to delete my workout | so that I can remove incorrect entries | ![Must Have](https://img.shields.io/badge/Must_Have-brightgreen) |
| As a returning user | I want to view all my workouts | so I can assess my progress over time | ![Must Have](https://img.shields.io/badge/Must_Have-brightgreen) |
| As a user | I want feedback messages after actions | so I know that my actions were successful | ![Should Have](https://img.shields.io/badge/Should_Have-9e0ae0) |
| As a user | I want confirmation before deleting | so that I don't accidentally lose data |  ![Should Have](https://img.shields.io/badge/Should_Have-9e0ae0) |
| As a frequent user | I want better UI styling | so that the app feels more polished | ![Could Have](https://img.shields.io/badge/Could_Have-fa1f7b)
| As a frequent user | I want workout analytics | so that I can visualise my progress | ![Won't Have](https://img.shields.io/badge/Wont_Have-390820) |
| As a frequent user | I want an inbuilt rest timer | so that I can automate my rest between sets | ![Won't Have](https://img.shields.io/badge/Wont_Have-390820) |
| As a frequent user | I want videos of exercises | so that I can see how to perform them correctly | ![Won't Have](https://img.shields.io/badge/Wont_Have-390820) |
| As a user | I want nutrition advice | so that I can track my diet alongside my exercise | ![won't Have](https://img.shields.io/badge/Wont_Have-390820) |

### User Story Testing
Each user story was tested manually and where appropriate with automated testing using Django tests.  This is documented in [Testing](#Testing)

## Design

Taking the app's requirements from the planning stage I then started to design the build.  This included capturing what data would be stored in the back-end of the app and how it would be organised in an Entity Relationship (ERD).

Once I had clarified this I then documented the flow of the app and used this to design the user interface.

### Database Model

Rep-Register uses a single model, Workout, which stores the individual exercise entries logged by a user.  Each workout is linked to Django's inbuilt User model.  The database uses a one-to-many relationship i.e. one user can have many workouts.

![Database ERD](/documentation/diagrams/database-ERD.png)

**User Model**
| Field | Type | Notes |
|----|----|----|
| id | AutoField | Primary key, auto-generated |
| username | CharField | Unique, required |
| email | CharField | Optional |
| password | CharField | Stored as a hash |

**Workout Model**
| Field | Type | Notes |
|----|----|----|
| id | AutoField | Primary key, auto-generated |
| user_id | ForeignKey| Links to the User model, cascades on delete |
| exercise | CharField | Name of exercise (max 100 characters) |
| weight | IntegerField | Weight used (kg) |
| sets | IntegerField | Number of sets performed |
| reps | IntegerField | Reps per set |
| date | DateField | Auto-set to today on creation |
| volume| computed | weight x sets x reps - not stored in DB

### App Cycle Flowchart
I used [draw.io](https://www.drawio.com/) to follow best practice and create a flow diagram for how the app would run in its entirety.  This was very helpful in clarifying the layout of the app, the functions that would need to be written and the templates that would need to be coded.

![Flow Diagram](/documentation/diagrams/rep-register-flow.png)

### Wireframes
Finally, I used [Balsamiq](https://balsamiq.cloud/) to plan out the layout of the GUI and determine what templates were needed.

| Page | Layout |
|----|----|
| Home | ![Home page wireframe](/documentation/wireframes/home-page.png) |
| Dashboard | ![Dashboard wireframe](/documentation/wireframes/dashboard.PNG) |
| Login | ![Login wireframe](/documentation/wireframes/login.PNG) |
| Workout form | ![Workout form wireframe](/documentation/wireframes/workout-form.PNG) |

Just to note the app was designed in this iteration for a desktop layout but is able to be used on smaller devices with the use of horizontal scroll.  Future implementation would include developing an improved user experience across all devices.

### Features

#### Existing Features
| Feature | Notes | Screenshot |
|----|----|----|
| Favicon | The favicon is a small image that displays in the browser tab. The intention is to enhance the user experience for those who have multiple tabs open and cannot read the text in the tabs.  A calendar and dumbell was chosen as it was relevant to the function of the app. | ![favicon](/documentation/features/favicon.png) |
| Login | Secure login allows users to save their workouts.  There is an option to remember user's details to speedup login. | ![Login](/documentation/features/login.PNG) |
| Logout | Secure logout allows users to safely protect their data. There is also an option to cancel and return to workouts if logging out was requested accidentally. | ![Logout](/documentation/features/logout.png) |
| Dashboard | The dashboard displays all the user's workout data including the volume of workout and the date it was entered which is calculated by the app.  Here the user can click the appropriate buttons to add, edit or delete a workout. | ![Dashboard](/documentation/features/dashboard.PNG) |
| Add Workout | On clicking the add workout button the user is directed to the add workout form where they can enter their data and save it.  If they decide they don't want to enter data they can click the cancel button and are redirected back to the dashboard. | ![Add Workout](/documentation/features/add-workout.PNG) |
| Delete Modal | On clicking delete a modal pops to check that the user definitely wants to delete their workout because the action can't be undone. This is to provide an improved user experience. | ![Delete Modal](/documentation/features/delete-modal.PNG) |
| Delete Confirmation | On confirming delete the user is redirected to the dashboard and a confirmation of the action is displayed. | ![Delete Confirmation](/documentation/features/delete-confirmation.PNG) |
| Edit Workout | On clicking edit workout the user is taken to the workout form where they can update the data for the workout.  If they decide they don't want to update they can click cancel and will be redirected to the dashboard. | ![Edit Workout](/documentation/features/edit-workout.PNG) |
| Edit Confirmation | When the user has updated their workout they receive confirmation of the action. | ![Edit Confirmation](/documentation/features/edit-confirmation.PNG) |
| 404 Error Page | Explains to the player there's been an error. Provides a link to take them back to the home page. | ![404-error](/documentation/features/404-error.PNG) |

#### Future Features
* **Workout Analytics**: graphs and charts that users can see their progress visually.
* **Inbuilt Rest Timer**: enabling users to automatically time their rest between sets.
* **Instructional Videos**: showing users how to perform the exercise correctly.
* **Nutritional Advice**: information and advice on nutrition to support users fitness journey in parallel with their workouts.

### Functions
The primary functions used on this application are:

- `home(request)`
    - Renders the home page
- `index(request)`
    - Retrieves and displays all the workouts logged by the logged-in user
- `add_workout(request)`
    - Handles the form to create and save a new workout entry
- `edit_workout(request, workout_id)`
    - Retrieves an existing workout by its ID and handles the form to update it
- `delete_workout(request, workout_id)`
    - Retrieves an existing workout by its ID and deletes it from the database
- `volume(self)`
    - Computed property that calculates total volume by multiplying weight x sets x reps
- `__str__(self)`
    - Returns the exercise name as the string representation of the workout object
- `setUp(self)`
    - Initialises a test user and sample workout to be used across the test cases
- `test_workout_page_loads_for_logged_in_user(self)`
    - Check that the workout index page returns a 200 status for an authenticated user
- `test_redirect_if_not_logged_in(self)`
    - Checks that unauthenticated users are redirected away from protected pages
- `test_correct_template_used(self)`
    - Verifies that the correct HTML template is used when rendering the workout page
- `test_edit_workout(self)`
    - Tests that an existing workout can be successfully updated with new data
- `test_delete_workout(self)`
    - Tests that a workout is correctly removed from the database when deleted
- `test_form_valid_data(self)`
    - Tests that the workout form is valid when all required fields are provided
- `test_form_missing_fields(self)`
    - Tests that the workout form fails validation when required fields are missing


## Tools & Technologies
| Tool/Tech | Use |
|----|----|
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (git add, git commit, git push, git pull) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=GitHub)](https://github.com/) | Secure online storage |
[![Badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=blue)](https://code.visualstudio.com/) | Local IDE for development |
[![Badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript)](https://www.javascript.com/) | User interaction on the site |
[![Badge](https://img.shields.io/badge/HTML-grey?logo=html5)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout |
[![Badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=rebeccapurple)](https://www.python.org/) |Design and layout |
[![Badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap)](https://getbootstrap.com/) | Front-end CSS framework for modern responsiveness and pre-built components|
[![Badge](https://img.shields.io/badge/Balsamiq-grey?)](https://balsamiq.cloud/) | For creating wireframes |
[![Badge](https://img.shields.io/badge/FREEP!K-grey?)](https://www.freepik.com/) | Icons |
[![Badge](https://img.shields.io/badge/favicon.io-grey?)](https://favicon.io/) | Favicon generator |
[![Badge](https://img.shields.io/badge/Python-grey?logo=python)](https://www.python.org/) | Back end programming |
[![Badge](https://img.shields.io/badge/Django-grey?logo=django)](https://www.djangoproject.com/) | Python framework for web application development|
[![Badge](https://img.shields.io/badge/Heroku-grey?logo=heroku)](https://www.heroku.com/) | Hosting the deployed site |
[![Badge](https://img.shields.io/badge/PostgreSQL-grey?logo=PostgreSQL)](https://www.postgresql.org/) | Relational database management |
[![Badge](https://img.shields.io/badge/draw.io-grey?logo=diagrams.net)](https://www.postgresql.org/) | Flow diagrams for mapping app logic |
[![Badge](https://img.shields.io/badge/chatGPT-grey?logo=chatgpt)](https://chatgpt.com/) | Used to help initial planning |
[![Badge](https://img.shields.io/badge/Claude-grey?logo=claude)](https://claude.ai/) | Used to help initial planning |
[![Badge](https://img.shields.io/badge/youtube-grey?logo=youtube&)](https://youtube.com/) | Tutorials and explanations of Django features |

## Testing
> [!Note]
> Please see the separate [TESTING.md](Testing.md) file for all the tests carried out.

### Known Bugs and Fixes
Although I kept notes of bugs during development in a notebook, for future projects I will use GitHub Issues to track bugs.  This will allow for easier writing of documentation throughout the development process.

| Issue | Fix | Status | Learning |
|----|----|----|----|
|  NoReverseMatch error causing automated test fail | Changed `workouts` to `workout:index` | Fixed | Clarity on how urls function withing Django |
| Login redirect not working correctly after authentication | corrected the `LOGIN_REDIRECT_URL` in `settings.py` to point to the correct view | Fixed | Django allauth redirect settings must match the app's URL configuration |
| `IntegrityError` on `user_id` field when saving workout |  Fixed by ensuring the logged-in user was correctly assigned to the workout instance before saving | Fixed | ForeignKey fields must be populated before calling `.save()` otherwise the database constraint is violated |
| Heading hierarchy error in HTML Validator | Changed h3 to h2 | Fixed | Important to check how individual templates interact with base html |
| Styling not applying on the sign out template | Linked the custom stylesheet in base html | Fixed | Add the CSS link as soon as created and view source code on the rendered page to insure it is linked |
| Delete button required confirmation step to prevent accidental data loss | Implemented a Bootstrap modal to prompt the user to confirm before deleting a workout | fixed | Defensive UX design is important for destructive actions - always confirm before delete |
| Form validation is not working correctly in tests | Passed data correctly into the form constructor using the `data={}` keyword argument | Fixed | Django test forms require data to be passed explicitly as a dictionary |

As far as I am aware, all the bugs listed above have been functionally fixed and the application is working as expected in the deployed version.

### Known Issues
The allauth signup validations errors remain as they come from the allauth package itself and are outside the developer's control.

The project is designed to be responsive from 375px and upwards, in line with the material taught on the course LMS. Minor layout inconsistencies may occur on extra-wide (e.g. 4k/8k monitors), or smart-display devices (e.g. Nest Hub, Smart Watches, Game Boy Color, etc.), as these resolutions are outside the project's scope, as taught by Code Institute.

## Deployment & Local Development

The live deployed applied can be found at [Rep Register](https://rep-register-0917d4849eb9.herokuapp.com/)

### Heroku Deployment
This project uses [Heroku](https://www.heroku.com/) as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployments steps are as follows after account setup:
- Select **New** in the top right-hand corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

>[!Important]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value|
|----|----|
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC | 1(*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |

Heroku needs some additional files in order to deploy properly.
- [requirements.txt](/requirements.txt)
- [Procfile](/Procfile)
- [.python-version](/.python-version)

You can install this project's [requirements.txt](/requirements.txt) (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updating using:
- `pip3 freeze --local > requirements.txt`

The [Procfile](/Procfile) can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located

The [.python-version](/.python-version) file tells Heroku the specific version of Python to use when running your application.
- `3.12` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
    - `git push heroku main`

The Python terminal window should now be connected and deployed to Heroku.  

### PostgreSQL
This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net/) for the Relational Database with Django.

>[!Caution]
>- PostgreSQL databases by Code Institute are only available to CI students.
>- You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
>- Code Institute students are allowed a maximum of 8 databases.
>- Databases are subject to deletion after 18 months.

To obtain my Postgres Database from Code Institute, I followed these steps:
- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

## WhiteNoise
This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:
- Install the WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteHoise to the `MIDDLEWARE` list, above all other middleware (apart from Django's "SecurityMiddleware"):

```` Python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middlware
]
````

### Local Development
This project can be cloned or forked to make a local copy on your own system.

For either method, you will need to install any applicable packages found withing the [requirements.txt](requirements.txt) file.

- `pip3 install -r  requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

>[!Important]
>This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```` Python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
````

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you would like to backup your database models, use the following command for each model you'd like to create a fixture for:
- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the repository for this project [Rehanon-Mackenzie/rep-register](https://github.com/Rehanon-Mackenzie/rep-register).
2.  Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
    - `git clone https://www.github.com/Rehanon-Mackenzie/rep-register.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Ona (formerly Gitpod), you can click below to create your own workspace using this repository.

[![Open in Ona-Gitpod](https://ona.com/run-in-ona.svg)](https://gitpod.io/#https://www.github.com/Rehanon-Mackenzie/rep-register)

**Please Note**: in order to directly open the project in Ona(Gitpod)m, you should have the browser extension installed.  A tutorial on how to do that can be found [here](https://ona.com/docs/classic/user/configure/user-settings/browser-extension).

#### Forking
By forking the GitHub Repository, you make a copy of the original repository on your GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log into GitHub and locate [Rehanon-Mackenzie/rep-register](https://github.com/Rehanon-Mackenzie/rep-register).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" button.
3. Once clicked, you should now have copy of the original repository in your own GitHub account.

### Local VS Deployment
There are no remaining major differences between the local version when compared to the deployed version online.


## Credits

### Content
| Source | Notes|
|----|----|
| [Claude](https://claude.ai/login) | Explaining code logic and planning documentation. |
| [Youtube](https://www.youtube.com/watch?v=rI95wyHD_6k)  | Further learning on how to create models and also a function to render the landing page `def home(request):return render(request, 'home.html')` |
| [freeCodeCamp](https://www.freecodecamp.org/news/build-and-deploy-a-fitness-tracker-using-python-django-and-pythonanywhere/) | I read the blog on creating a fitness tracker for clarity on the flow I would need in the app |


### Media
| Source | Note |
|----|----|
| [Freepik](https://www.magnific.com/icon/dumbell_12572002#fromView=search&page=1&position=16&uuid=cf21ed36-4c8a-4f70-9600-7f0e55b88b9c) | Dumbell icon used for the logo and favicon |
| [favicon.io]() | Used to create the favicon from the dumbell logo | 

## Acknowledgements
- I would like to thank the [Code Insitute](https://codeinstitute.net/) for the module on Django which really helped me get my head round using the framework.
- I would like to thank my tutor, Manu who is always very helpful and offers support when I meet with him.
- I would like to thank my friends and family who are alway super supportive especially when I think I can't do something. Their belief is such a gift.
- I would like to thank Aorthi & Lola, who created the [Hot Girls Code](https://hot-girls-code.com/home) podcast that has been so helpful on my coding journey.
- Finally, I would like to thank the team at [codebar Brighton](https://codebar.io/brighton) who are such a supportive community and make me excited to be involved in tech. 
