# Restaurant Cubaneros 
![mockup](readme_img/amiresponsive.png)

My project is a restaurant website which represents a traditional rustic cuban cuisine. The websites main features, as 'about', 'menu', contacts' displays the 'read' part of CRUD to the user and gives the important information about the websites goal to the user, while the admin can change and update the same information from the backend. The crucial part of the project is the 'book here!'(or the booking form) and 'my bookings' which gives the user/admin the possibility for 'create', 'update' and 'delete' in CRUD, so that a reservation/booking can be created, edited or removed. As admin these bookings can be approved or rejected and the status of this action reflects in the frontend presentation, which gives the user the possibility to follow up the status themselves.

<hr>

The live deployed application can be found deployed on [Heroku](https://tribe.herokuapp.com).

The link to my Github repository's [Github Repo](https://github.com/eleanorbucke21/PP4).

<hr>

## CONTENTS

* [User Experience](#user-experience-ux)
  * [Agile](#agile)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [ElephantSQL databse](#elephantsql-database)
  * [Cloudinary API](#cloudinary-api)
  * [Heroku deployment](#heroku-deployment)
  * [Local deployment](#local-deployment)
    * [Cloning](#cloning)
    * [Forking](#forking)


* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

<hr>


## User Experience (UX)

Users visiting the restaurants website are looking for a new place to explore. We are offering a real rustic traditional experiance to excape the luxuary fancy vibe but still a place to fine dine. 

The front page provides the user with all the necessary content so they could decide if that is the place they want to explore. If not authenticated they can access almost all the content of the page until it gets to the reservation part of it, for which authentication is required.

Everyone can enjoy their visit to our website because we have adjusted it and designed for all different screen sizes.

### Agile

The project is build using the agile methodology. Link to the project board: [here](https://github.com/users/Balkaneros91/projects/13/views/1)

### User Stories

I have created user stories based on the agile methodology and I have created them using the Githubs kanban. In the upcoming images the projects build-up process can be followed up throughout different stages.

![Stage-1](readme_img/kanban/kanban_1.png)
![Stage-2](readme_img/kanban/kanban_2.png)
![Stage-3](readme_img/kanban/kanban_3.png)
![Stage-4](readme_img/kanban/kanban_4.png)
![Stage-4](readme_img/kanban/kanban_5.png)
![Stage-5](readme_img/kanban/kanban_done.png)

<hr>

## Design

### Colour Scheme

I wanted to keep it simple and light. The color palette matches the cover image and is well suited color scheme for the full website.

[Coolors.co](https://coolors.co/) was the website I've used to fetch the colour palette presented.

![Colour Palette](readme_img/coolors.png)

### Typography

After I have applied the bootstrap CND I really liked the font style which came along with it and so I decided to just stick to it.

<hr>

## Wireframes

[Balsamiq](https://balsamiq.com/wireframes) is used for wireframe design.

### Restaurant's Home Page

<details>
<summary>Click here!</summary>

#### Mobile
![screenshot](readme_img/wireframes/mobile_main.png)

#### Desktop
![screenshot](readme_img/wireframes/desktop_main_before.png)

#### Desktop
![screenshot](readme_img/wireframes/desktop_main_after.png)

</details>

### About Page

<details>
<summary>Click here!</summary>

#### Mobile
![screenshot](readme_img/wireframes/mobile_about.png)

#### Desktop
![screenshot](readme_img/wireframes/desktop_about.png)

</details>

### Menu Page

<details>
<summary>Click here!</summary>

#### Mobile
![screenshot](readme_img/wireframes/mobile_menu.png)

#### Desktop
![screenshot](readme_img/wireframes/desktop_menu.png)

</details>

### Meal details page

<details>
<summary>Click here!</summary>

#### Mobile
![screenshot](readme_img/wireframes/mobile_menu_item_detail.png)

#### Desktop
![screenshot](readme_img/wireframes/desktop_menu_item_detail.png)

</details>

### Booking form

<details>
<summary>Click here!</summary>

#### Mobile
![screenshot](readme_img/wireframes/mobile_booking_form.png)

#### Desktop
![screenshot](readme_img/wireframes/desktop_booking_form.png)

</details>

### Booking confirmation

<details>
<summary>Click here!</summary>

#### Mobile
![screenshot](readme_img/wireframes/mobile_booking_confirmation.png)

#### Desktop
![screenshot](readme_img/wireframes/desktop_booking_confirmation.png)

</details>

### Contacts page

<details>
<summary>Click here!</summary>

#### Mobile
![screenshot](readme_img/wireframes/mobile_contacts.png)

#### Desktop
![screenshot](readme_img/wireframes/desktop_contacts.png)

</details>

### Bookings list

<details>
<summary>Click here!</summary>

#### Mobile
![screenshot](readme_img/wireframes/mobile_my_bookings.png)

#### Desktop
![screenshot](readme_img/wireframes/desktop_my_bookings.png)

</details>

### Edit bookings

<details>
<summary>Click here!</summary>

#### Mobile
![screenshot](readme_img/wireframes/mobile_edit_booking.png)

#### Desktop
![screenshot](readme_img/wireframes/desktop_edit_booking.png)

</details>

### Delete bookings

<details>
<summary>Click here!</summary>

#### Mobile
![screenshot](readme_img/wireframes/mobile_delete_booking.png)

#### Desktop
![screenshot](readme_img/wireframes/desktop_delete_booking.png)

</details>

### Sign in Page

<details>
<summary>Click here!</summary>

#### Mobile
![screenshot](readme_img/wireframes/mobile_sign_in.png)

#### Desktop
![screenshot](readme_img/wireframes/desktop_sign_in.png)

</details>

### Sign out Page

<details>
<summary>Click here!</summary>

#### Mobile
![screenshot](readme_img/wireframes/mobile_sign_out.png)

#### Desktop
![screenshot](readme_img/wireframes/desktop_sign_out.png)

</details>

### Sign up Page

<details>
<summary>Click here!</summary>

#### Mobile
![screenshot](readme_img/wireframes/mobile_sign_up.png)

#### Desktop
![screenshot](readme_img/wireframes/desktop_sign_up.png)

</details>

### Error Pages

<details>
<summary>Click here!</summary>

#### Mobile
![screenshot](readme_img/wireframes/mobile_404_error.png)

#### Desktop
![screenshot](readme_img/wireframes/desktop_404_error.png)

</details>

<hr>

## Features

My website includes the base.html and the rest of the pages are build using templating. 

### Final look of the Home page
![Home Page](readme_img/features/home_1.png)
![Home Page](readme_img/features/home_2.png)

### Final look of the About page
![About Page](readme_img/features/about.png)

### Final look of the Menu page
![Menu Page](readme_img/features/menu_1.png)
![Menu Page](readme_img/features/menu_2.png)
![Menu Page](readme_img/features/menu_3.png)

### Final look of the Meal detail page
![Meal Page](readme_img/features/meal_details.png)

### Final look of the Booking form page
![Form Page](readme_img/features/booking_form.png)

### Final look of the Booking confirmation page
![Confirmation Page](readme_img/features/booking_confirmation.png)

### Final look of the Contacts page
![Contacts Page](readme_img/features/contacts.png)

### Final look of the Bookings list page
![Bookings Page](readme_img/features/bookings_list.png)

### Final look of the Edit booking page
![Edit Page](readme_img/features/edit_booking.png)

### Final look of the Delete booking page
![Delete Page](readme_img/features/delete_booking.png)

### Final look of the Sign in page
![Sign in Page](readme_img/features/sign_in.png)

### Final look of the Sign out page
![Sign out Page](readme_img/features/sign_out.png)

### Final look of the Sign up page
![Sign up Page](readme_img/features/sign_up.png)

### Final look of the Error pages
![Error 404 Page](readme_img/features/error_404.png)
![Error 500 Page](readme_img/features/error_500.png)

### Footer
![Footer](readme_img/features/footer.png)

### Success messages
![Booking success messages](readme_img/success_message/booking_success_message.png)
![Sign in success messages](readme_img/success_message/sign_in_success_message.png)


### General features on each page

The navigation menu and footer is continiously the same throughout all the pages of my website.

### Future Implementations

This page has a potential to grow bigger. There is open space for many possible future implementations, like email automation, adding tables and available time slots to the booking form and so on.

<hr>

## Technologies Used

### Languages Used

<ul>
<li>Python</li>
<li>HTML/CSS</li>
<li>JavaScript</li>
</ul>

### Frameworks, Libraries & Programs Used

<ul>
<li>Django</li>
<li>Bootstrap</li>
<li>Cloudinary-storage</li>
<li>PostgreSQL</li>
<li>Github</li>
<li>Gitpod</li>
<li>Balsamic</li>
</ul>

<hr>

## Deployment & Local Development

### Deployment

The live deployed application can be found deployed on [Heroku](https://tribe.herokuapp.com).


### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: tribe).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.


### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.
- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.


### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | insert your own Cloudinary API key here |
| `DATABASE_URL` | insert your own ElephantSQL database URL here |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | this can be any random secret key |

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "insert your own Cloudinary API key here")
os.environ.setdefault("DATABASE_URL", "insert your own ElephantSQL database URL here")
os.environ.setdefault("SECRET_KEY", "this can be any random secret key")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/adamgilroy22/tribe) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/adamgilroy22/tribe.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/adamgilroy22/tribe)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/adamgilroy22/tribe)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Testing

All the links in the navigation bar and in the footer has been tested and works. The logo link always brings us back to the main page,

while the About and Contact links are only index.html local links so avoid scrolling up and down on the page. The rest as Gallery and Sign Up links opens a new tab in the browser for easier navigation between pages. And the deployed website has been tested in Chrome, Safari, Internet Explorer (Opera) and Firefox. Media queries looks good and been tested throughout different screen sizes.

<hr>

<ul>Manual Testing:
<li>Booking data model tested: all of its CRUD functionality for the admin and users</li>
<li>Tested confirm bookings by admin.</li>
<li>Menu data model tested: create and read functionality for admin, and only view for users</li>
<li>Announcements data model: tested create and read functionality for the admin and only view for users</li>
<li>Sign-up/ Sign-in forms and links all tested to confirm working as intended</li>
<li>Tested Booking page links and all its functionality</li>
<li>Tested User Authorisations to ensure role-based functions such as Booking page access, edit or deleting bookings</li>
</ul>

Browser Compatibility:

Browser | Pass/Fail 
 --- | --- | ---
Google Chrome | Pass
Safari | Pass
Microsoft Edge | Pass
Firefox | Pass

### Responsiveness

I used both of these to check the responsivness across different screen sizes.

- [Am I Responsive?](http://ami.responsivedesign.is/#) 
- [Responsinator](http://www.responsinator.com/)

### Lighthouse

For mobile: 
![Lighthouse](assets/readme/lighthouse-mobile.png)
For desktop: 
![Lighthouse](assets/readme/lighthouse-desktop.png)

### <u>Lighthouse</u>
|Page | Mobile  | Computer|
| ------------- | ------------- |------------- |
| Index | <img src="markdown/Mindex.png" width="250">| <img src="markdown/cindex.png" width="250">
| Register |<img src="markdown/mregister.png" width="250">| <img src="markdown/cregister.png" width="250">
|

### W3C HTML Validator
![W3C HTML Validator](assets/readme/w3c-markup-validation.png)

### W3C CSS Validator
![W3C CSS Validator](assets/readme/w3c-css-validation.png)

### W3C CSS Validator
No errors were recieved on the pages. <br>
<img src="markdown/css.png" width="400">

### W3C Markup Validation Serice
No errors were recieved on the pages except for the post detail page which recieved one error.
|Error |Error explanation| Code |
| ------------- | ------------- |------------- |
| <img src="markdown/error.png" width="400"> | <img src="markdown/errorexplain.png" width="400"> |<img src="markdown/errorcode.png" width="400">|

### JShint
I did not perform any validation on javascript as all the javascript was imported in from [clean blog](https://github.com/StartBootstrap/startbootstrap-clean-blog).

### Code Institute Python Linter

- bawarchikhana/settings.py <br>
<img src="markdown/bawarchikhana-settings-py.png" width="250">

- bawarchikhana/urls.py <br>
<img src="markdown/bawarchikhana-urls-py.png" width="250">

- blog/admin.py , blog/forms.py, blog/models.py, blog/views.py.<br>
<img src="markdown/blog-admin-forms-models-views.png" width="250">

- blog/urls.py. <br>
<img src="markdown/blog-urls.png" width="250">

## Testing
- [W3C Markup Validation Serice](https://validator.w3.org/) was used to test for error codes in the HTML.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)  was used to test for error codes in the CSS.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to detect errors and potential problems in Python code.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    was used during the development process to test, debug, explore and modify HTML elements, and to test responsiveness in different screen sizes.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used for improving the quality of web page. It has audits for performance, accessibility, progressive web apps, SEO, and more.

### Known bugs

No known bugs detected

- The navigation bar continues to move around the screen even with it being set to absolute. I have been unable to solve the issue. 

### Solved Bugs

Some of the bugs I came accross and fixed: 

+ Background images
  + Description: Diffrent size throughout differet screen sizes
  + Expected behaviour: Full image with no missing sides all the time covering its own content
  + Actual behaviour: The image was too small or too big or missing a part of it
  + Fix: Add code background-size: 100%; or background-size: cover; plus adjusting the media queries

  + Quotation
  + Description: Wrong positioning on the logo image and throughtout different screens changing its place
  + Expected behaviour: To not disturb nor overflow the logo image
  + Actual behaviour: Running over the logo image and due to color choice text can't be read
  + Fix: Adjusting the media queries to different screen sizes

+ Footer
  + Description: Footer wrongly positioned on the small screen
  + Expected behaviour: Footer at all times should be horizontal
  + Actual behaviour: Footer vertical positioning on small screen
  + Fix: Adding the correct class attribute col-s-4.

  ### Solved Bugs
- When adding success messages I found that there was a bug on the DeletePost view.
- With this view I had to add different code than the others to correct it.
- I corrected this by adding this code from [stack overflow](https://stackoverflow.com/questions/48777015/djangos-successmessagemixin-not-working-with-deleteview)

<img src="markdown/DeleteBug.png">

<hr>

## Credits

Code Institue projects: 'Hello Django' and 'I think therefore I blog' has helped me a lot during the project planning for my websites design.
Extra help I've used for this project, please see links below.

### Code Used

- [w3schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [CSS Media Queries](https://www.w3schools.com/css/css3_mediaqueries.asp)
- [Grid-View](https://www.w3schools.com/css/css_rwd_grid.asp)
- [emmet.io](https://docs.emmet.io/cheat-sheet/)

- [Start Bootstrap](https://startbootstrap.com/theme/clean-blog)
- [Django documentation](https://docs.djangoproject.com/en/3.2/)

### Content

- The code is mostly created by me and I was inspired by the traditional cuban cuisine.

- For the deployment section I got expired by my colleague here at CI,Adam Gilroy.

###  Media

- [Favicon](https://favicon.io/emoji-favicons/fork-and-knife/) The fork and knife emoji. <br>
<img src="static/site_static/favicon_io1/favicon.ico">

All images are downloaded from internet and used only for purposes of this project.
  
###  Acknowledgments

- And last but not least a big thanks to my mentor Antonio Rodriguez and to the CI tutor support who help a few times during the process.
