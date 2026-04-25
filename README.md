# Rep Register ![dumbell](/static/images/favicon-32x32.png)
## 💻 Developer
Rehanon Mackenzie
<br>
[GitHub](https://github.com/Rehanon-Mackenzie)
<br>
![GitHub last commit](https://img.shields.io/github/last-commit/rehanon-mackenzie/rep-register?style=for-badge&color=red)
![GitHub contributors](https://img.shields.io/github/contributors/rehanon-mackenzie/rep-register?style=for-badge&color=orange)
![GitHub language count](https://img.shields.io/github/languages/count/rehanon-mackenzie/rep-register?style=for-badge&color=yellow)
![GitHub top language](https://img.shields.io/github/languages/top/rehanon-mackenzie/rep-register?style=for-badge&color=green)
![Deployment](https://img.shields.io/badge/deployment-heroku-purple)
<br>
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
    

## About

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

I used [draw.io](https://www.drawio.com/) to follow best practice and create a flow diagram for how the app would run in its entirety.  This was very helpful in clarifying the layout of the app, the functions that would need to be written and the templates that would need to be coded.

![Flow Diagram](/documentation/diagrams/rep-register-flow.png)



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
| Edit Confirmation | When the user has updated their workout they receive confirmation of the action. | ![Edit Confirmation](/documentation/features/edit-confirmation.PNG)

#### Future Features
* **Workout Analytics**: graphs and charts that users can see their progress visually.
* **Inbuilt Rest Timer**: enabling users to automatically time their rest between sets.
* **Instructional Videos**: showing users how to perform the exercise correctly.
* **Nutritional Advice**: information and advice on nutrition to support users fitness journey in parallel with their workouts.

## Tools & Technologies
| Tool/Tech | Use |
|----|----|
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (git add, git commit, git push, git pull) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=GitHub)](https://github.com/) | Secure online storage |
![VS Code](https://img.shields.io/badge/VS%20Code-grey?logo=visualstudiocode&logoColor=blue)
