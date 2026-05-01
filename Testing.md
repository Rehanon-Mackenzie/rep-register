## Validation Testing
### HTML Validation
| Directory | File | URL |Screenshot | Notes|
|----|----|----|----|----|
| | [home.html](/templates/home.html) | [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Frep-register-0917d4849eb9.herokuapp.com%2F#textarea) | ![Home Page](/documentation/validation/home-page-validation.PNG) | |
| | [signup.html](/templates/account/signup.html) | [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Frep-register-0917d4849eb9.herokuapp.com%2Faccounts%2Fsignup%2F#textarea) | ![Signup Page](/documentation/validation/signup-page-errors.PNG) | HTML validation errors on the signup page originate from the aullauth package's rendered output and are not within the developer's code. |
| | 

### Python Lint Validation

| Directory | File | URL |Screenshot | Notes|
|----|----|----|----|----|
| | [admin.py](/workouts/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Rehanon-Mackenzie/rep-register/refs/heads/main/workouts/admin.py) | ![Admin Validation](/documentation/validation/workouts-admin-validation.PNG) | |
| | [apps.py](/workouts/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Rehanon-Mackenzie/rep-register/refs/heads/main/workouts/apps.py) | ![Apps Validation](/documentation/validation/workouts-apps-validation.PNG) | |
| | [forms.py](/workouts/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Rehanon-Mackenzie/rep-register/refs/heads/main/workouts/forms.py) | ![Forms Validation](/documentation/validation/workouts-form-validation.PNG) | |
| | [models.py](/workouts/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Rehanon-Mackenzie/rep-register/refs/heads/main/workouts/models.py) | ![Models Validation](/documentation/validation/workouts-models-python-linter.PNG) | |
| | [tests_forms.py](/workouts/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Rehanon-Mackenzie/rep-register/refs/heads/main/workouts/test_forms.py) | ![Tests Forms Validation](/documentation/validation/workouts-tests-forms-validation.PNG) | |
| | [test_views.py](/workouts/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Rehanon-Mackenzie/rep-register/refs/heads/main/workouts/test_views.py) | ![Test Views Validation](/documentation/validation/workouts-tests-views-validation.PNG)| |
| | [urls.py](/workouts/urls.py) | [PEP8 CI Link](https://raw.githubusercontent.com/Rehanon-Mackenzie/rep-register/refs/heads/main/workouts/urls.py) | ![Urls Validation](/documentation/validation/workouts-urls-validation.PNG) | |
| | [views.py](/workouts/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Rehanon-Mackenzie/rep-register/refs/heads/main/workouts/views.py) | ![Views Validation](/documentation/validation/workouts-views-validation.PNG)


### Lighthouse Testing

I used the Lighthouse extension within Chrome Developer Tools to test performance, accessibility, best practices and SEO of the website.

![Home page lighthouse](/documentation/lighthouse/home-page-lighthouse.PNG)
*Home: Performance 99, Accessibility 100, Best Practices 100, SEO 100*

![Login page lighthouse](/documentation/lighthouse/login-page-lighthouse.PNG)
*Login: Performance 99, Accessibility 97, Best Practices 100, SEO 100*

![Dashboard lighthouse](/documentation/lighthouse/dashboard-lighthouse.PNG)
*Dashboard: Performance 99, Accessibility 100, Best Practices 100, SEO 100*

![Add workout page lighthouse](/documentation/lighthouse/add-workout-page-lighthouse.PNG)
*Add Workout: Performance 99, Accessibility 100, Best Practices 100, SEO 100*

![Edit workout page lighthouse](/documentation/lighthouse/edit-workout-page-lighthouse.PNG)
*Edit Workout: Performance 99, Accessibility 100, Best Practices 100, SEO 100*

![404 page lighthouse](/documentation/lighthouse/404-page-lighthouse.PNG)
*404*: Performance 99, Accessibility 100, Best Practices 96, SEO 91*


### Home Page Testing

| Feature  | Expected outcome  | Testing performed  | Result  | Pass/Fail  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Hover colour change on login button to identify link | The button will change to the secondary colour to identify it's a clickable link | Hover over login button | Button changed to secondary colour | Pass|
| Hover colour change on sign up button to identify link | The button will change to the secondary colour to identify it's a clickable link | Hover over sign up button | Button changed to secondary colour | Pass|
|  Login button | To take user to login html | Click login button  | Took user to login html | Pass  |
|  Sign Up button | To take user to signup html | Click sign up button  | Took user to signup html | Pass |

### Sign Up Page Testing

| Feature  | Expected outcome  | Testing performed  | Result  | Pass/Fail  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Hover colour change on sign in link to identify link | The link will change to the secondary colour to identify it's a clickable link | Hover over sign in link | Link changed to secondary colour | Pass|
|  Sign up form | To allow new users to register their details  | New user entered their chosen username and password| Form was filled in | Pass  |
| Password required | If user does not enter a password a message pops up to advised field is required  | Password field was left blank and sign up button clicked| Form was not accepted and message displayed to advise field is required | Pass|
| Password confirmation | If user doesn not enter a password into the confirmation field a message pops up to advise field is required | Password confirmation field was left blank and sign up button clicked |  Form was not accepted and message displayed to advise field is required| Pass|
| Password check | If passwords don't match form is not accepted | Two different passwords were entered and sign up button clicked| Form was not accepted and message displayed to user to type same password twice | Pass|
|  Sign up button | To take user to index html | Click sign in button  | Took authenticated user to index html | Pass 

### Login Page Testing

| Feature  | Expected outcome  | Testing performed  | Result  | Pass/Fail  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Hover colour change on sign up link to identify link | The link will change to the secondary colour to identify it's a clickable link | Hover over sign up link | Link changed to secondary colour | Pass|
| Hover colour change on sign in button to identify link | The button will change to the secondary colour to identify it's a clickable link | Hover over sign in button | Button changed to secondary colour | Pass|
|  Login form | To allow registered users to enter their login details  | Registered user entered their login details| Form was filled in | Pass  |
| Hover colour change on sign in button to identify link | The button will change to the secondary colour to identify it's a clickable link | Hover over sign in button | Button changed to secondary colour | Pass|
|  Sign in button | To take user to index html | Click sign in button  | Took authenticated user to index html | Pass |  

### Dashboard Testing


