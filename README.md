# Restaurant Cubaneros

## [Sea Side](https://seaside-rest.herokuapp.com/)

<img src="readme_img/amiresponsive.png">

<br>

This is a restaurant app that allows users to book a table at a certain time,
the site owner or admin can approve or dismiss the bookings. <br>
The site also has a menu page where Admin can add, edit, or delete menu items for visitors to see. <br>

<ul>
Technologies and libraries used:
<li>Python</li>
<li>Django</li>
<li>Bootstrap</li>
<li>HTML/CSS</li>
<li>JavaScript</li>
<li>Cloudinary-storage</li>
<li>PostgreSQL</li>
</ul>
Sea Side consists of 3 separated apps: reservation, menu and announcement
<hr>
Additionally, the admin can use the admin panel to publish new events and announcements wish then displayed in a section called announcements on the home page. <br>
Provided with Django's built-in user model, the app requires users to register or log in in order to create a booking, edit their own existing booking, or even delete their bookings. Bookings are only available to see for the user that created them.

The application is fully responsive on all devices.
<img>

Sea Side Restaurant is a full-stack application developed using agile methodology.
below are the issues that were defined before starting the applications with acceptance criteria

### mock up
I created a mock up of the home page using [Figma.com](https://www.figma.com/)
<img src="readme-images/mockup.png">
Worth to know that changes made to the homepage design while developing.

## Features <hr>
Through out development, I followed the issues' acceptance criteria on every issue

### stage 1
<img src="readme-images/1.png">

#### User Story View booking
<img src="readme-images/issue13.png">

#### User Story Add a booking
<img src="readme-images/issue1.png">

#### User Story Booking confirmation
<img src="readme-images/issue14.png">

#### User Story Authorization
<img src="readme-images/issue2.png">
<hr>

### stage 2
<img src="readme-images/2.png">

#### User Story Booking page
<img src="readme-images/issue7.png">

#### User Story Booking Authentication
<img src="readme-images/issue5.png">

#### User Story Authenticate to edit a booking
<img src="readme-images/issue6.png">
<hr>

### stage 3
<img src="readme-images/3.png">

#### User Story Delete Booking
<img src="readme-images/issue4.png">

#### User Story Edit booking
<img src="readme-images/issue3.png">

#### User Story Oppening Hours
<img src="readme-images/issue9.png">

<hr>

### stage 4
<img src="readme-images/4.png">

#### User Story Menu
<img src="readme-images/issue8.png">

#### User Story Address 
<img src="readme-images/issue10.png">

#### User Story Announcements
<img src="readme-images/issue12.png">

#### User Story Map
<img src="readme-images/issue11.png">

<hr>

### Other Features

<ul>
<li>Navbar contains a restaurant's logo and links to all relevant pages, Booking only appears for logged-in users, instead, a none logged-in user would see a sign-up and sign-in links</li>
<img src="readme-images/navbar.png"> <br>
<img src="readme-images/navbar2.png">

<li>The hero image on the home page contains 2 buttons 1 for creating a booking, that redirects non logged-in users to log in first in order to book.</li>
<br>
<img src="readme-images/hero-btn.png">
<br>

<li>View menu button available to all visitors.</li>

<li>About us section on the home page showcase the restaurant's services.</li>

<li>Google map API provided on the home page showing the location of the restaurant.</li>

<li>Menu page provided with an introduction of Kitchen chefs with social media links for each chef.</li>
<br>

<img src="readme-images/chefs.png">
<br>

<li>Feedback provided to all users actions in the form of messages, messages will disappear after 3 seconds of appearing.</li>

<li>Responsive footer at the bottom of every page, provided with social media links.</li>
<br>
<img src="readme-images/footer.png">
<br>
</ul>
<hr>

### Potential features to implement:
<ul>
<li>Ability for admin to change opening hours.</li>
<li>Check availability of tables and auto accept bookings according to it.</li>
</ul>

## Testing
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

### Validator Testing
<ul>
<li>All Python code ran through PEOP8 checker succesfully without any problem.</li>

<li>All CSS files ran through CSS jigsaw validator with no errors</li>

[CSS JIGSAW](https://jigsaw.w3.org/css-validator/) passed with no erros.
<img src="readme-images/css-jigsaw.png">

<li>All HTML files ran through W3C validator with no errors</li>

[HTML W3C validator](https://validator.w3.org/)
</ul>

<hr>

## Deployment
At the start of making the project I the made the first deployment to Heroku after setting up the environment by doing the following steps:
<ol>
<li>Installing Django and supporting libraries</li>
    <ul>
        <li>Installed Django and gunicorn</li>
        <li>Installed supporting libraries</li>
        <li>Installed Cloudinary Libraries</li>
        <li>Created project and app</li>
        <li>Ran server to test</li>
    </ul>
<li>Deploying an app to Heroku</li>
    <ul>
    <li>Created an app on Heroku</li>
    <li>Attached the database</li>
    <li>Prepared environment and settings.py file</li>
    <li>Got my statc and media files stored on Cloudinary</li>
    <li>Deplyed the app (empty) by linking my Github and chose deploy branch.</li>
    </ul>
<li>Final deployment after finishing the project:</li>
    <ul>
    <li>Installed heroku in gitpod using the command: npm install -g heroku</li>
    <li>Logged in to heroku in the terminal window used command: login -i</li>
    <li>Entred command heroku git:remote -a seaside-rest to select the heroku app I created before remotly</li>
    <li>Added and commited all changes to github</li>
    <li>pushed to github and heroku using commands:
    <ul>
        <li>git push origin main</li>
        <li>git push heroku main</li>
    </ul>
    </li>
    </ul>
</ol>
End of deployment

## Credits
<hr>

Hero Image was taken by a google search, Original site owner is:
https://www.ahusseaside.com/

Images of chefs and hero sections buttons style are taken from a boot strap template:

[Bootstrapmade](https://bootstrapmade.com/delicious-free-restaurant-bootstrap-theme/)

Html elemnts main responsivenes are [Bootstrap](https://getbootstrap.com/)

all icons used in the projects are [FontAwsome](https://fontawesome.com/)

Fonts from by [Google Fonts](https://fonts.google.com/)

Map API from [Google map platform](https://mapsplatform.google.com/)

Used the lessons videos of (I think therefore I blog) for reference on deployment and creating a model.

Recived help from Daniel_c_5p on slack in :
<ul>
<li>restrict booking views to the user that owns the booking</li>
<li>Help with menu view function to view menu items in 4 seperate categories</li>
</ul>

Code institute tutor support helped me get back on track on several occasions when I had errors or any problems throughout the project.

Happy coding!
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

<img src="markdown/amiresponsive.png" width="100%">

# Bawarchi Khana # 
A Pakistani recipe blog. Bawarchi khana means kitchen in Urdu. This website is deigned to showcase pakistani recipes that can be added by either admin or by a user who has registered to the website. Each user has the ability to like and dislike a recipe post. If the user is also the author of the recipe post they have the option to delete or edit the post. As admin for this blog, they have the option to approve or deny all posts and comments to be published on the website.

:desktop_computer: [Live Website] (https://pp4.herokuapp.com/)

:open_file_folder: [Github Repository] (https://github.com/eleanorbucke21/PP4)

# User Experience

### Agile

I implemented agile methodology when creating this website. The link to the project board can be found [here](https://github.com/users/eleanorbucke21/projects/9)

### User Stories

HomePage <strong><u>(Not logged in)</u></strong>

- As a user I want to be able to tell what the website is about.
- As a user I want to see the posts.
- As a user I want to be able to register.
- As a user I want to be able to login. 
- As a user I want to be able to see the likes and dislikes.
    
Homepage <strong><u>(Logged in) </u></strong>
- As a user I want to be able to add recipes.
- As a user I want to be able to logout.

Admin Page

<i>To access the admin page type <strong>/admin</strong> at the end of the address bar</i>
- As an admin I want to be able to add posts.
- As an admin I want to be able to approve or not approve posts.
- As an admin I want to be able to approve or not approve comments. 

Register

- As a user I want to be able to register.

Login Page

- As a user I want to be able to login with username and password.
- As a user I want to have the option of remembering me indtead of having to login.

Logout Page

- As a user I want to be able to logout.

# Features 
## Navigation
- Featured at the top of the page with the name of the website on the left.
- The navigation bar also has a register, login, add recipe and logout depending on if user is logged in. 
- The navigation is also responsive to smaller screens with a toggle option on the navbar, which hides the links till tapped.
## Header
- The header shows the name of the website <i>Bawarchi Khana</i>.
- The header has a colorful background which is why I used an opac background with dark text to display the name of the website.
- The image used as the background represents what the website is about.
## Footer
- The footer has a link to facebook.
- The footer has a link to Twitter.
- The footer has a link to my github.

## Register
- The register page has a form.
- The form displays the details needed.
- If username is already in use it will ask you to fill out form again.
<img src="markdown/username.png" width="300">

- If a user does not put in same password in both password fields they will get a warning to fill out form again.
- If a user uses a common password they will get a warning to choose another.
<img src="markdown/password.png" width="300">

- Once you register you are re-directed to home page.
## Login
- The login page has a form.
- The form displays where to type name and password.
- The form also has an option to tick ✔️ remember me so they won't need to login the next time they visit the page.
- If a user enters the incorrect username they will recieve an error.
- If a user enters the incorrect password they will recieve an error.
<img src="markdown/loginerror.png">

## Logout
- A user is asked if they are sure they want to logout.
- After clicking <i>signout</i> they are redirected to the home page.
<img src="markdown/signout.png" width="200">

## <u>Posts</u>
- The post page displays the recipe.
- The post has an image that the author of the post chooses to upload.

<u><strong>When user is logged in:</strong></u>
- The post has two buttons underneath displaying the likes and dislikes. <br>
<img src="markdown/likedislike1.png" width="200" height="150"> <img src="markdown/likedislike2.png" width="100" height="150">

<u><strong> When user is author of the post: </strong></u>
- Two buttons display if the user is the author of the post.
- An edit button is displayed if the user is the author of the post.
- A delete button is displayed if the user is the author of the post.
<img src="markdown/editdelete.png">

## <u>Future Features</u>

- In the future I would like to add an option to download the recipe posts as a pdf to view offline.
- In the future I would like to add a search option for the website to allow users to search.
- In the future I would like to enable editing comments. 

# Typography and Color Scheme

## <u>Font</u>
- The font used was from an imported bootstrap template.
- The fonts used in this template are <i>Open Sans</i> and <i>Lora</i>.
- The Font used for the website brand is <i>Sassy Frass</i>.
- The <i>Sassy Frass</i> font was used as it most resembled Urdu, the language of Pakistan.

## <u>Color Scheme</u>
- The colors used were grey and white.
- These colors where chosen to emphasize the images of the recipes.

## <strong>Wireframes</strong>
### Home Page
<img src="markdown/homepage.png" width="400">

### Registration Page
<img src="markdown/registration.png" width="400">

### Login Page
<img src="markdown/login.png" width="400">

### Logout Page
<img src="markdown/signoutpage.png" width="400">

### Postdetail Page
<img src="markdown/postdetail.png" width="400">

### Add A Post
<img src="markdown/addapost.png" width="400">

<br>

# <strong>Technologies</strong>
### <u>Languages used</u>
- [HTML](https://en.wikipedia.org/wiki/HTML5) - Add content and formatting to web page.
- [CSS](https://en.wikipedia.org/wiki/CSS) - Add styling and colours to web page.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Add interactive features to web page.
- [Django](https://en.wikipedia.org/wiki/Django_(web_framework)) - A Python-based web framework that follows the model–template–views (MTV) architectural pattern. 

### <u>Frameworks, Libraries and Programs Used</u>

- [Gitpod](https://gitpod.io/) - web-based editor optimised for debugging, testing, syntax highlighting and extension support.
- [Git](https://git-scm.com/) - used to allow for tracking of any changes in the code and for the version control.
- [Github](https://github.com/) - used to host the project files and host webpage onto the internet.
- [Heroku](https://www.heroku.com/) - A cloud platform service that supports several programming languages.
- [ElephantSQL](https://www.elephantsql.com/) - Also known as postgres, is a free and open-source relational database management system (RDBMS) emphasizing extensibility and SQL compliance.
- [Fontawesome](https://fontawesome.com/) - to insert icons in the website to make site more visually appealing and easy to navigate.
- [Google Fonts](https://fonts.google.com/) - used to import fonts in the style.css stylesheet.
- [Favicon](https://favicon.io/) - to insert icons in the website to make site more visually appealing.
- [bootstrap-clean-blog](https://github.com/StartBootstrap/startbootstrap-clean-blog) - A bootstrap blog template imported in for CSS.

## <strong>Testing</strong>
- [W3C Markup Validation Serice](https://validator.w3.org/) was used to test for error codes in the HTML.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)  was used to test for error codes in the CSS.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to detect errors and potential problems in Python code.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    was used during the development process to test, debug, explore and modify HTML elements, and to test responsiveness in different screen sizes.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used for improving the quality of web page. It has audits for performance, accessibility, progressive web apps, SEO, and more.

### <u>Website validation testing</u>

### <u>JShint</u>
I did not perform any validation on javascript as all the javascript was imported in from [clean blog](https://github.com/StartBootstrap/startbootstrap-clean-blog).

### <u>W3C Markup Validation Serice</u>
No errors were recieved on the pages except for the post detail page which recieved one error.
|Error |Error explanation| Code |
| ------------- | ------------- |------------- |
| <img src="markdown/error.png" width="400"> | <img src="markdown/errorexplain.png" width="400"> |<img src="markdown/errorcode.png" width="400">|

### <u>W3C CSS Validator</u>
No errors were recieved on the pages. <br>
<img src="markdown/css.png" width="400">

### <u>Code Institute Python Linter</u>

- bawarchikhana/settings.py <br>
<img src="markdown/bawarchikhana-settings-py.png" width="250">

- bawarchikhana/urls.py <br>
<img src="markdown/bawarchikhana-urls-py.png" width="250">

- blog/admin.py , blog/forms.py, blog/models.py, blog/views.py.<br>
<img src="markdown/blog-admin-forms-models-views.png" width="250">

- blog/urls.py. <br>
<img src="markdown/blog-urls.png" width="250">

### <u>Lighthouse</u>
|Page | Mobile  | Computer|
| ------------- | ------------- |------------- |
| Index | <img src="markdown/Mindex.png" width="250">| <img src="markdown/cindex.png" width="250">
| Register |<img src="markdown/mregister.png" width="250">| <img src="markdown/cregister.png" width="250">
| Sign In |<img src="markdown/msignnin.png" width="250">| <img src="markdown/csignin.png" width="250">
| Logout |<img src="markdown/mlogout.png" width="250">|<img src="markdown/clogout.png" width="250">
| Add A Post |<img src="markdown/maddapost.png" width="250"> |<img src="markdown/caddapost.png" width="250">
| Post Detail |<img src="markdown/mpostdetail.png" width="250"> | <img src="markdown/cpostdetail.png" width="250">

### <u>Responsiveness</u>
[Am I Responsive?](http://ami.responsivedesign.is/#) was used to check responsiveness of the site pages across different devices.
 
 The site has been tested on various sizes such as those listed below.
 
 <strong>Mobile:</strong>
 375x667 / 360x740 / 412x915 / 414x896
 
 <strong>Tablet:</strong>
 768x1024 / 820x1180 / 912x1368 
 
<strong>Monitor:</strong>
 1280x1024 / 1600x900 / 2560x1440 / 3440x1440

### <u>Manual Testing</u>
Browser Compatibility:

Browser | Outcome | Pass/Fail 
 --- | --- | ---
Google Chrome | No appearance, responsiveness nor functionality issues.| Pass
Safari | No appearance, responsiveness nor functionality issues. | Pass
Microsoft Edge | No appearance, responsiveness nor functionality issues. | Pass
Firefox | No appearance, responsiveness nor functionality issues. | Pass

Device compatibility:

Device | Outcome | Pass/Fail
--- | --- | ---
Laptop | No appearance, responsiveness nor functionality issues. | Pass
ipad mini | No appearance, responsiveness nor functionality issues. | Pass
Lenovo M1 Tab | No appearance, responsiveness nor functionality issues. | Pass
Samsung s20 | No appearance, responsiveness nor functionality issues. | Pass
iphone 12 pro | No appearance, responsiveness nor functionality issues. | Pass

 ## Test cases
 ### Navigation Bar<strong> (Not logged in)</strong>
 
| Input | Output | Pass/Fail |
|--- | --- | --- |
|  Clicked on Home in navigation bar. | It refreshed the page. | Pass
|  Clicked on the navbrand in navigation bar. | It refreshed the page. | Pass
| Clicked on register in navigation bar. | It went to the registration page. | Pass
| Clicked on Login in navigation bar.  | It went to the login page.| Pass

 ### Navigation Bar<strong> (Logged in)</strong>
 
| Input | Output | Pass/Fail |
|--- | --- | --- |
|  Clicked on Home in navigation bar. | It refreshed the page. | Pass
|  Clicked on the navbrand in navigation bar. | It refreshed the page. | Pass
| Clicked on Add a Recipe in navigation bar. | It went to the add a recipe page. | Pass
| Clicked on Logout in navigation bar.  | It went to the logout page.| Pass

 ### Footer Bar
 
| Input | Output | Pass/Fail |
|--- | --- | --- |
|  Clicked on Twitter icon. | It opened twitter in a new page.| Pass
|  Clicked on Facebook icon. | It opened facebook in a new page.| Pass
|  Clicked on Github icon. | It opened my [github](https://github.com/eleanorbucke21). | Pass

 ### Index Page
 
| Input | Output | Pass/Fail |
|--- | --- | --- |
|  Clicked on Post on index page. | It went to the Post page | Pass
|  On Login. | recieves notification that I was signed in. | Pass
|  On Logout. | recieves notification that I was signed out. | Pass

 ### Add a Post Page <strong>(Logged in)</strong>
 
| Input | Output | Pass/Fail |
|--- | --- | --- |
|  Added a post on add a post page. | Recived notification that post is submitted for approval.  | Pass

 ### Post Page <strong>(Logged in)</strong>
 
| Input | Output | Pass/Fail |
|--- | --- | --- |
|  Clicked on like(heart icon). | The number of the likes went up.  | Pass
|  Clicked on dislike(thumbs down icon). | The number of the dislikes went up.  | Pass
|  Wrote a comment. | Recieved notification of comment is awaiting approval.  | Pass

## <strong>Bugs</strong>

### <u>Unsolved Bugs</u>
- The navigation bar continues to move around the screen even with it being set to absolute. I have been unable to solve the issue. 

### <u>Solved Bugs</u>
- When adding success messages I found that there was a bug on the DeletePost view.
- With this view I had to add different code than the others to correct it.
- I corrected this by adding this code from [stack overflow](https://stackoverflow.com/questions/48777015/djangos-successmessagemixin-not-working-with-deleteview)

<img src="markdown/DeleteBug.png">

## <strong>Deployment</strong>
 
 ### <u>Github</u>

This website was published using GitHub Pages.

- Navigate to [GitHub](https://github.com/) and log in.

- Navigate to your repositories and find the project you want to deploy

- Under the name of your chosen Repository you will see a ribbon of selections, click on 'Settings' located on the right hand side.

- Scroll down till you see 'Pages' heading on the left hand side

- Under the 'Source' click on the dropdown and select 'master' or 'main' branch and click save

- The page will reload and you'll see the link of your published page displayed under 'GitHub' pages.

- It takes a few minutes for the site to be published, wait until the background of your link changes to a green color before trying to open it.

- Congratulations you have deployed your project!
 
 This website was written on Gitpod.
 
 ### <u>Gitpod</u>
 - Navigate to [Gitpod] through [GitHub](https://github.com/), [GitLab](https://www.gitlab.com/).
- In the browser’s address bar, prefix the entire URL with gitpod.io/# and press Enter.
- For example, gitpod.io/#https://github.com/gitpod-io/website
- We recommend you install the Gitpod browser extension to make this a one-click operation.
- Sign in with one of the listed providers and let the workspace start up.
- Congratulations, you have started your first of many ephemeral developer environments!

### <u>ElephantSQL</u>
This website was hosted on elephantSQL.
- Create a new app.
- Add a name of the app. This name should be a name that helps you identify which application the instance is used by.
- Select a plan: The plan you would like to have. I used <strong>Tiny Turtle Plan</strong>
- Select tags: I left this field blank.
- Select Region: I selected EU-West-1 (IRELAND).
- Then click review.
- Check that the details are correct tthen click <strong>"Create Instance"</strong>.
- Return to the ElephantSQL dashboard and click on the database instance name for this project.
- In the URL section, click the copy icon to copy the database URL which will then be put into the envy.py file in gitpod.

### <u>Heroku</u>
This website was deployed on Heroku. 
* When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

    1. `heroku/python`
    2. `heroku/nodejs`

* You must then create a _Config Var_ called `PORT`. Set this to `8000`
* If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.
* Connect your GitHub repository and deploy as normal.

## <strong>Credits</strong>
### <u>Content</u>
- [startbootstrap.com Clean Blog](https://startbootstrap.com/theme/clean-blog) A bootstrap blog template used for CSS.
- [Clean Blog Github repository](https://github.com/StartBootstrap/startbootstrap-clean-blog) A bootstrap blog template used for CSS.
- [Cloudinary](https://cloudinary.com/) Online library. Cloudinary provides an enterprise-grade, media experience platform for all rich media types. Using AI, automation, and advanced image and video processing capabilities, we remove the hassle of manual digital media requirements and provide a clear path for companies to deliver amazing visuals at scale.
- [Balsamiq](https://balsamiq.com/) used to create the wireframes.
- [Pexels](https://www.pexels.com/) Online free images. These were used throughout the website.
- Code Institute tutors. Helped when I was struggling with some aspects of the website and code not working. 

### <u>Code & Tutorials</u>
- [Building A blog with application Django](https://djangocentral.com/building-a-blog-application-with-django/)
- Mentor helped with bootstrap in positioning the post detail image and the post on smaller screens. Also with issue where the white background on the side heading was gray instead of white by usinf z-index in the css file. 

### <u>Media</u>
- [Favicon](https://favicon.io/emoji-favicons/curry-rice/) The curry and Rice emoji. <br>
<img src="static/favicon/favicon.ico">

<strong><u>Images Used:</u></strong>
- [Spice market](https://www.pexels.com/photo/clear-glass-jars-with-assorted-foods-618491/)
- [Spinach](https://www.pexels.com/photo/green-spinach-in-the-colander-6824476/)
- [Chana masala](https://www.pexels.com/photo/cooked-food-in-bow-2679501/)
- [Gulab jamuns](https://www.pexels.com/photo/sweet-crisp-snacks-served-in-brass-cup-8887055/)
- [Chipatti](https://www.pexels.com/photo/chapati-bread-on-a-woven-basket-9797029/)
- [Meal laid out](https://www.pexels.com/photo/white-and-brown-cooked-dish-on-white-ceramic-bowls-958545/)
- [Biryani](https://www.pexels.com/photo/close-up-photo-of-biryani-dish-1624487/)


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------




# __Tribe - Portfolio Project 4__
![mockup](documentation/mockup.png)

Tribe is a social media app built with Django where users can sign up, create posts, view other people's posts, follow other users, message other users, like and comment on posts and delete their posts.

The aim of this project was to build a site that allows users to easily sign up and connect with their friends.

Developed by Adam Gilroy

[Live link to website](https://tribe.herokuapp.com/)

## UX

I wanted to keep the design quite simple on this site so as to not distract the user. I used the main purple colour throughout the site to establish a brand with Tribe. The off-white colour I used for my background looks well with the purple on my nav menu.

### Colour Scheme

- `#5122b4` used as the primary site colour.
- `#f5f5f5` used for the site background and button text.
- `#333333` used for the site text and footer background.
- `#bf87f7` used for footer links against the dark grey colour and for the background of images on the homepage/login/sign up/logout pages.
- `#d9534f` used for the trash icon, notification icon and warning buttons.

I used [coolors.co](https://coolors.co/5122b4-f5f5f5-333333-bf87f7-d9534f) to generate my colour palette.

![screenshot](documentation/tribe-colour-scheme.png)

I've used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

```css
:root {
    --main-purple: #5122b4;
    --light-purple: #bf87f7;
    --accent-red: #d9534f;
    --dark-grey: #333333;
    --off-white: #f5f5f5;
}
```

### Typography

- [Fredoka One](https://fonts.google.com/specimen/Fredoka+One) was used for the site logo and header elements in the landing page, login, sign up, logout, password reset pages

- [Roboto](https://fonts.google.com/specimen/Roboto) was used for the site text

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## User Stories

### New Site Users

- As a new site user, I would like to clearly see the site's purpose, so that I can decide whether or not to sign up. `(MUST HAVE)`
- As a new site user, I would like to sign up for the site and create an account, so that I can create my profile and start using the site. `(MUST HAVE)`

### Registered Users

- As a registered user, I would like to log in to my account, so that I can access the site. `(MUST HAVE)`
- As a registered user, I would like to log out of my account, so that I can end my session on my current device. `(MUST HAVE)`
- As a registered user, I would like to reset my password if I forget it, so that I can regain access to my account. `(MUST HAVE)`
- As a registered user, I would like to update my profile picture and cover photo, so that I can help other users identify me. `(MUST HAVE)`
- As a registered user, I would like to edit my profile bio, so that I can further personalize my profile. `(MUST HAVE)`
- As a registered user, I would like to follow other users, so that I can view their posts on my feed. `(MUST HAVE)`
- As a registered user, I would like to unfollow other users, so that I can remove their posts from my feed. `(MUST HAVE)`
- As a registered user, I would like to create new posts, so that I can share my thoughts with my followers. `(MUST HAVE)`
- As a registered user, I would like to delete my posts, so that I can remove content that I no longer want published. `(MUST HAVE)`
- As a registered user, I would like to view posts from people I follow, so that I can keep up to date with them. `(MUST HAVE)`
- As a registered user, I would like to easily navigate the site, so that I can access what I need at the click of a button. `(MUST HAVE)`
- As a registered user, I would like to like other people's posts, so that I can let them know I enjoyed their post. `(SHOULD HAVE)`
- As a registered user, I would like to comment on other people's posts, so that I can further engage with the user and open a discussion. `(SHOULD HAVE)`
- As a registered user, I would like to delete my comments on other people's posts, so that I can remove comments I no longer want published. `(SHOULD HAVE)`
- As a registered user, I would like to click on a post to expand it and see the comments, so that I can further engage with posts. `(SHOULD HAVE)`
- As a registered user, I would like to see what time and date a post was created, so that I can take in the post content in full context based on how new or old it is. `(SHOULD HAVE)`
- As a registered user, I would like to search for users and posts, so that I can find content I want to see and people I want to follow. `(SHOULD HAVE)`
- As a registered user, I would like to delete other people's comments on my posts, so that I can remove comments I don't want on my posts. `(SHOULD HAVE)`
- As a registered user, I would like to be notified when someone follows me, interacts with my posts, or messages me, so that I can interact back with them and keep up to date with my content. `(SHOULD HAVE)`
- As a registered user, I would like to like other people's comments on posts, so that I can let them know I enjoyed their comment. `(SHOULD HAVE)`
- As a registered user, I would like to message other users, so that I can communicate with them privately. `(COULD HAVE)`
- As a registered user, I would like to report or flag posts, so that I can notify the admins of content that might not be allowed on the site. `(COULD HAVE)`
- As a registered user I want to be able to put the site into dark mode so that I can make the website easier to see at night. `(WONT HAVE)`
- As a registered user I want to be able to make my profile private so that I can hide my content from people who don't follow me. `(WONT HAVE)`
- As a registered user I want to be able to see suggestions of who my friends are following so that I can find profiles I might want to follow instead of manually searching every time. `(WONT HAVE)`
- As a registered user I want to be able to video call my friends so that I can communicate with them more efficiently than instant messaging. `(WONT HAVE)`
- As a registered user I want to be able to create group chats with my friends so that I can message multiple friends simultaneously. `(WONT HAVE)`
- As a registered user I want to be able to reshare other people's posts so that I can share them with my followers. `(WONT HAVE)`

### Site Admin

- As a site administrator, I should be able to delete posts and comments from any user, so that I can moderate the site's content. `(SHOULD HAVE)`
- As a site administrator, I should be able to access a page only for admins to see flagged user posts, so that I can see a list of posts that possibly need to be deleted. `(COULD HAVE)`
- As a site administrator, I should be able to unflag a post if deemed not needed for deletion, so that I can remove it from the list of flagged posts. `(COULD HAVE)`
- As a site administrator, I should be able to suspend user accounts who violate site guidelines, so that I can prevent users from constantly breaking the site rules. `(WONT HAVE)`

## Wireframes

I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Home Page Wireframes

<details>
<summary>Click to View Home Page wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/mobile-home.png)

#### Tablet
![screenshot](documentation/wireframes/tablet-home.png)

#### Desktop
![screenshot](documentation/wireframes/desktop-home.png)

</details>

### Sign Up Page Wireframes

<details>
<summary>Click to View Sign Up Page wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/mobile-sign-up.png)

#### Tablet
![screenshot](documentation/wireframes/tablet-sign-up.png)

#### Desktop
![screenshot](documentation/wireframes/desktop-sign-up.png)

</details>

### Sign In Page Wireframes

<details>
<summary>Click to View Sign In Page wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/mobile-sign-in.png)

#### Tablet
![screenshot](documentation/wireframes/tablet-sign-in.png)

#### Desktop
![screenshot](documentation/wireframes/desktop-sign-in.png)

</details>

### Following Feed Wireframes

<details>
<summary>Click to View Following Feed wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/mobile-feed.png)

#### Tablet
![screenshot](documentation/wireframes/tablet-feed.png)

#### Desktop
![screenshot](documentation/wireframes/desktop-feed.png)

</details>

### All Posts Feed Wireframes

<details>
<summary>Click to View All Posts Feed wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/mobile-all-posts-feed.png)

#### Tablet
![screenshot](documentation/wireframes/tablet-all-posts-feed.png)

#### Desktop
![screenshot](documentation/wireframes/desktop-all-posts-feed.png)

</details>

### User Profile Wireframes

<details>
<summary>Click to View User Profile wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/mobile-user-profile.png)

#### Tablet
![screenshot](documentation/wireframes/tablet-user-profile.png)

#### Desktop
![screenshot](documentation/wireframes/desktop-user-profile.png)

</details>

### Other Profile Wireframes

<details>
<summary>Click to View Other Profile wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/mobile-other-profile.png)

#### Tablet
![screenshot](documentation/wireframes/tablet-other-profile.png)

#### Desktop
![screenshot](documentation/wireframes/desktop-other-profile.png)

</details>

### Inbox Wireframes

<details>
<summary>Click to View Inbox wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/mobile-inbox.png)

#### Tablet
![screenshot](documentation/wireframes/tablet-inbox.png)

#### Desktop
![screenshot](documentation/wireframes/desktop-inbox.png)

</details>

### Create Thread Wireframes

<details>
<summary>Click to View Create Thread wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/mobile-create-thread.png)

#### Tablet
![screenshot](documentation/wireframes/tablet-create-thread.png)

#### Desktop
![screenshot](documentation/wireframes/desktop-create-thread.png)

</details>

### Message Thread Wireframes

<details>
<summary>Click to View Message Thread wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/mobile-message-thread.png)

#### Tablet
![screenshot](documentation/wireframes/tablet-message-thread.png)

#### Desktop
![screenshot](documentation/wireframes/desktop-message-thread.png)

</details>

### Search Page Wireframes

<details>
<summary>Click to View Search Page wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/mobile-search.png)

#### Tablet
![screenshot](documentation/wireframes/tablet-search.png)

#### Desktop
![screenshot](documentation/wireframes/desktop-search.png)

</details>

### Notifications Wireframes

<details>
<summary>Click to View Notifications wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/mobile-notifications.png)

#### Tablet
![screenshot](documentation/wireframes/tablet-notifications.png)

#### Desktop
![screenshot](documentation/wireframes/desktop-notifications.png)

</details>

### Admin Panel Wireframes

<details>
<summary>Click to View Admin Panel wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/mobile-admin-panel.png)

#### Tablet
![screenshot](documentation/wireframes/tablet-admin-panel.png)

#### Desktop
![screenshot](documentation/wireframes/desktop-admin-panel.png)

</details>

### Sign Out Page Wireframes

<details>
<summary>Click to View Sign Out Page wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/mobile-sign-out.png)

#### Tablet
![screenshot](documentation/wireframes/tablet-sign-out.png)

#### Desktop
![screenshot](documentation/wireframes/desktop-sign-out.png)

</details>

## Features

### Existing Features

- **Landing Page**

    - This is the page a user lands on when arriving at the site for the first time or before they've logged in if they don't have an active session. It welcomes them to the site and gives them the option to either sign up for an account or log in to an existing account.

    ![screenshot](documentation/testing/landing-page.png)

- **Sign Up Page**

    - This is where the user can create an account for themselves by entering their e-mail address, desired username and password twice to confirm. If the user accidentally comes to this page instead of the login page they can get to the right page using the link in the card text.

    ![screenshot](documentation/testing/sign-up-page.png)

- **Login Page**

    - This is where users with existing accounts can log in with either their username or e-mail and password. They can choose to let their browser remember them if they plan on returning to the site on the same device to avoid having to log in again. There's a link to the sign up page too if the user accidentally navigated to this page instead of trying to create an account. If the user forgets their password they can click the link to reset it.

    ![screenshot](documentation/testing/login-page.png)

- **Reset Password**

    - If a user forgets their password, they can reset it by entering the e-mail address they used to sign up. They will then receive an email with a link to set a new password.

    ![screenshot](documentation/testing/forgot-password-page.png)

    ![screenshot](documentation/testing/forgot-password-confirmation-page.png)

    ![screenshot](documentation/testing/password-reset-image.png)

    ![screenshot](documentation/testing/change-password-page.png)

- **Nav Menu**

    - The nav menu contains everything the user will need to navigate the site. The site logo always appears on the site menu with the other items only showing for logged in users. The menu contains an admin panel that only shows up if the logged in user is an admin. From the nav menu, user's can go to their feed, their message inbox, their profile, view their notifications if they have any, search the site for posts and users using the search bar and log out.

    ![screenshot](documentation/testing/nav-menu.png)

    ![screenshot](documentation/testing/nav-menu-regular.png)

    ![screenshot](documentation/testing/nav-menu-mobile.png)

- **Footer**

    - The footer appears across the website and includes information about me as the developer with links to my Twitter, Linkedin and GitHub pages. This lets the user get to know me as the developer and connect on these platforms if they wish.

    ![screenshot](documentation/testing/footer.png)

- **Following Feed**

    - This is the user's main feed containing posts only from users they have followed. At the top of the feed there's an area for the user to create a post. There's buttons to switch between the user's following feed and the all posts feed containing every post from every site user. Posts are displayed in chronological order from newest to oldest. If the user isn't following anyone or the people they're following has no posts, a message will appear saying "It's very quiet here..." which will prompt the user to follow more users to start seeing posts in this feed.

    ![screenshot](documentation/testing/following-feed.png)

    ![screenshot](documentation/testing/empty-following-feed.png)

- **Add Post Form**

    - This is where the user will create their posts. It appears in both the following and all posts feed along with the user's own profile. There's a prompt in the form for the user to "Share with your tribe...".

    ![screenshot](documentation/testing/new-post-form.png)

- **Feed Switcher**

    - This appears on both the following feed and the all posts feed. It allows the user to switch between both feeds with ease. The feed that the user is currently viewing will have a purple background to let the user know what feed they're on.

    ![screenshot](documentation/testing/feed-switcher.png)

- **All Posts Feed**

    - This feed shows every single post on the website from all users. It allows the user to find new users to follow and connect with.

    ![screenshot](documentation/testing/all-posts-feed.png)

- **Pagination**

    - Both following and all posts feeds as well as profiles have pagination implemented so if more than 10 posts appear in the feed then buttons appear at the bottom to split the feed into individual pages with a maximum of 10 posts on a page. This is to increase the user experience and make the site content easier to digest. If the user is on the first page of pagination then only one button will appear saying "Older Posts" and if they're on the last page then a single button will appear and say "Newer Posts" if there's more than 2 pages of posts then anything in between with contain both buttons to change between pages.

    ![screenshot](documentation/testing/pagination-buttons.png)

- **Posts**

    - The site wouldn't be much without user posts. Posts are found in the users feeds. From here, users can like posts, report/flag posts, see when the post was created or delete a post if they're the original author. The number of times a post has been liked is displayed next to the like button and when a user has liked a post it's filled with colour to let the user know they've already liked it. It returns to an outline if the user unlikes it.

    ![screenshot](documentation/testing/individual-post.png)

    ![screenshot](documentation/testing/unliked-post.png)

    ![screenshot](documentation/testing/liked-post.png)

    ![screenshot](documentation/testing/delete-icon.png)

- **Individual Posts Page**

    - When a user clicks on a post in their feed, they're brought to the individual post page. Here they have the same options as in the feed in being able to like and flag/report a post. Under the post a user can see a list of comments on the post and a form to add their own comment to the post.

    ![screenshot](documentation/testing/post-detail-page.png)

    ![screenshot](documentation/testing/report-button.png)

- **Delete Post**

    - Posts can be deleted by the post author by clicking on the delete icon. When deleting a post, the user is brought to a confirmation page to avoid posts being deleted accidentally. There's a button to bring them back to the post if the user changes their mind about deleting their post.

    ![screenshot](documentation/testing/post-delete.png)

- **Comments**

    - Post comments are viewed under a post and similar to posts, can be liked. Comments can be deleted by the comment author or post author and edited by the comment author.

- **Edit Comment**

    - Comments can be edited by the user that created it. Clicking the edit icon brings them to a page where they can see their comment and make changes before hitting a button to save it. There's also a button to bring them back to the post where the comment was made if they hit the edit button by mistake.

    ![screenshot](documentation/testing/edit-comment.png)

- **Delete Comment**

    - Comments can be deleted by the comment author or the original posts author by clicking on the delete icon. Similar to when deleting a post, users are brought to a confirmation page to avoid comments being deleted accidentally. There's a button to bring them back to the post they commented on if the user changes their mind about deleting the comment.

    ![screenshot](documentation/testing/comment-delete.png)

- **Profile**

    - The profile contains a card with the user's information including profile picture, background image, display name, username, bio, number of posts and number of followers. If the user is viewing their own profile then they'll have an icon to edit their profile. If they're viewing another user's profile then they'll have a button to follow or unfollow that user. The profile also includes a list of posts and a form to create a new post if the user is on their own profile.

    ![screenshot](documentation/testing/user-profile.png)

    ![screenshot](documentation/testing/other-profile.png)

    ![screenshot](documentation/testing/other-profile-following.png)

- **Edit Profile**

    - This is where the user can edit their profile details including their display name, bio, profile and background pictures. The user can also remove their profile picture or background image and revert back to the default from here. There's a button to bring them back to their profile if they decide not to make any edits.

    ![screenshot](documentation/testing/edit-profile.png)

- **Follower List**

    - If the user has followers, you can click on the follower count on their profile to see a list of their followers. You can click on the profiles in the list to view them and follow them if you want.

    ![screenshot](documentation/testing/followers-list.png)

- **Message Inbox**

    - Users can access their message inbox from the nav menu. Here a list of users they have messaged/received messages from appears. There's a button to start a new conversation if they have no threads or want to start a new one. 

    ![screenshot](documentation/testing/inbox.png)

- **Create Message Thread**

    - If the user clicks on the "New Conversation" button in their inbox, they will be brought to a page to create a message thread with a user. When they type a username into the form and click Continue, a new thread is created if the users haven't messaged before and they're brought to their thread if one exists already. If the user enters a username that doesn't exist then an error message pops up letting them know that the user doesn't exist.

    ![screenshot](documentation/testing/create-thread.png)

    ![screenshot](documentation/testing/create-thread-error.png)

- **Message Thread**

    - This is where users can message back and forward between each other. User messages appear on the left in purple and the person they're talking to's messages appear on the right in black. Each message contains the date and time is was sent.

    ![screenshot](documentation/testing/message-thread.png)

- **Search**

    - Users can search people and posts on the site. If their search matches then a list of both users and posts containing their search will appear. If the search has no results in either then both lists will let the user know there was no match. If there's a user but no post matching the query then the user list will contain matching queries and the post one will let them know there's no posts for their search and the same for the opposite. The page also contains a button to bring the user back to the feed.

    ![screenshot](documentation/testing/search-page.png)

    ![screenshot](documentation/testing/full-empty-search.png)

    ![screenshot](documentation/testing/empty-post-search.png)

    ![screenshot](documentation/testing/empty-user-search.png)

- **Logout**

    - When the user wants to finish their session and logout, they can do so from the nav menu. When a user clicks the logout button they're met with a page asking them to confirm they want to log out. They're redirected to the landing page if they click the confirmation button and a message pops up confirming that they've logged out.

    ![screenshot](documentation/testing/sign-out-page.png)

- **Notifications**

    - Whenever a user follows someone, likes a post or comment, comments on a post, or messages someone, the other user receives a notification. The notifications tab on the nav menu shows a red dot with the number of unread notifications and when a user clicks it a dropdown will appear with a list of their notifications. If a user clicks on the notification it will bring them to the user, post, or message thread to do with the notification. If they want to remove a notification without going to the associated page, they can click the red x to delete it.

    ![screenshot](documentation/testing/empty-notifications.png)

    ![screenshot](documentation/testing/notifications.png)

    ![screenshot](documentation/testing/notifications-dropdown.png)

- **Admin Panel**

    - If the logged in user is an admin, an extra icon will appear on their nav menu to view an admin panel page. This page contains a list of all the posts that have been flagged by users. Admins can then decide if the post is to be deleted or unflagged. If there is no flagged posts then the page will let the admin know with a short message.

    ![screenshot](documentation/testing/admin-panel.png)

    ![screenshot](documentation/testing/flagged-posts-list.png)

    ![screenshot](documentation/testing/admin-page-empty.png)

- **Error Pages**

    - If a user ends up on a page that either doesn't exist or that they shouldn't be on (regular user using admin panel link or trying to delete other user's post through a link) then they'll be shown an error page with a button to bring them back to their feed.

    ![screenshot](documentation/testing/403-screenshot.png)

    ![screenshot](documentation/testing/404-screenshot.png)

    ![screenshot](documentation/testing/500-screenshot.png)

### Future Features

This is definitely a project I want to revisit in the future and add some extra features to. These features have been logged as Won't Have in my MoSCoW prioritization.

- Reshare Posts
    - I'd like to be able to add a feature that allows users to reshare other posts with their followers.
- Follow Suggestions
    - I'd like to create a section that suggests people for users to follow based on who they already follow and the posts that they interact with.
- Group Messaging
    - I'd like to add a feature that allows users to create groups for messaging and message between multiple users at once.
- Voice and Video Calling
    - I'd like to extend the messaging feature further by including voice and video calls between users.
- Private Profiles
    - I'd like to add a feature that allows a user to set their profile to private to only be viewed by followers that the user must accept.
- Dark Mode
    - I'd like to implement a feature that allows the user to change the site's colour scheme to one with a dark background with lighter text to allow the site to be viewed easily in darker settings.
- User Suspension
    - I'd like to further increase the admin's ability to moderate the website by allowing them to suspend users if they post inappropriate content. This will disable the user from posting or interacting with other users for a set amount of time or permanently for severe incidents.

## Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS :root variables](https://www.w3schools.com/css/css3_variables.asp) used for reusable styles throughout the site.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [JavaScript](https://www.javascript.com) used for user interaction on the site for automatically closing Django Messages and to handle the notification dropdown and notification delete functions.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Markdown Builder by Tim Nelson](https://traveltimn.github.io/markdown-builder) used to help generate the Markdown files.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.
- [Canva](https://www.canva.com/) used to create the images seen on the landing page, login, sign-up, logout and password reset pages. Also used to create the default user profile and background images.
- [Techsini](https://techsini.com/) used to create the mockup image used in my readme.
- [Gmail](https://www.google.com/gmail/about/) used to create an email address to send password reset emails from.
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) used to check contrast between colours on the site
- [Balsamiq](https://balsamiq.com/wireframes) used to design my site wireframes.
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) used to check for typos in my README and TESTING files.

## Database Design

I created an entity relationship diagram using [Diagrams.net](https://www.diagrams.net/). This helped me to visualize the relationships between my data structures and made the development process easier as I had everything mapped out in front of me for reference to avoid having to reference each models.py file individually.

### Entity Relationship Diagram

![screenshot](documentation/tribe-entity-relationship-diagram.png)

### Models

The following are the models created for Tribe

- **Allauth User Model**
    - The User model was built using [Django's Allauth library](https://django-allauth.readthedocs.io/en/latest/overview.html)
    - When a user is created, they're automatically assigned a profile through the Profile model.

- **Profile**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | user | OneToOne | FK to **User** model |
    | | display_name | CharField | |
    | | bio | TextField | |
    | | profile_pic | CloudinaryField | |
    | | bg_pic | CloudinaryField | |
    | | followers | ManyToMany | M2M to **User** model |

- **Post**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | author | ForeignKey | FK to **User** model |
    | | content | TextField | |
    | | posted_on | DateTimeField | |
    | | likes | ManyToMany | M2M to **User** model |
    | | is_flagged | BooleanField | |

- **Comment**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | author | ForeignKey | FK to **User** model |
    | | comment | TextField | |
    | | posted_on | DateTimeField | |
    | | likes | ManyToMany | M2M to **User** model |
    | **FK** | post | ForeignKey | FK to **Post** model |

- **MessageThread**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | sender | ForeignKey | FK to **User** model |
    | **FK** | recipient | ForeignKey | FK to **User** model |

- **MessageModel**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | thread | ForeignKey | FK to **MessageThread** model |
    | **FK** | message_sender | ForeignKey | FK to **User** model |
    | **FK** | message_receiver | ForeignKey | FK to **User** model |
    | | message_content | CharField | |
    | | sent_at | DateTimeField | |

- **Notification**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | | notification_type | IntegerField | |
    | **FK** | to_user | ForeignKey | FK to **User** model |
    | **FK** | from_user | ForeignKey | FK to **User** model |
    | **FK** | post | ForeignKey | FK to **Post** model |
    | **FK** | comment | ForeignKey | FK to **Comment** model |
    | **FK** | thread | ForeignKey | FK to **MessageThread** model |
    | | date | DateTimeField | |
    | | user_has_seen | BooleanField | |

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/adamgilroy22/tribe/projects) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it was made to work.

Through it, user stories were used to map out the development progress of the project using the basic Kanban board. It helped me to see the backlog of work I needed to complete and move tasks across as I worked on them before testing and signing off to finish them.

![screenshot](documentation/tribe-project-board.png)

### GitHub Issues

[GitHub Issues](https://github.com/adamgilroy22/tribe/issues) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories and created a *Bug* tag to track and monitor issues on the site to be worked on.

- [Open Issues](https://github.com/adamgilroy22/tribe/issues)

    ![screenshot](documentation/tribe-open-issues.png)

- [Closed Issues](https://github.com/adamgilroy22/tribe/issues?q=is%3Aissue+is%3Aclosed)

    ![screenshot](documentation/tribe-closed-issues-1.png)

    ![screenshot](documentation/tribe-closed-issues-2.png)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

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

#### Cloning

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

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/adamgilroy22/tribe)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder by Tim Nelson](https://traveltimn.github.io/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Dev Handbook](https://www.devhandbook.com/django/user-profile/) | user profile creation | creating a user profile that extends Django's User model |
| [YouTube](https://www.youtube.com/watch?v=_JKWYkz597c&t=1s&ab_channel=LegionScript) | notifications | tutorial for setting up notifications to be sent on the site |
| [YouTube](https://www.youtube.com/watch?v=oxrQdZ5KqW0&ab_channel=LegionScript) | messages | tutorial for setting up messaging between users on the site |
| [YouTube](https://www.youtube.com/watch?v=sF7go6tcKbc&t=1s&ab_channel=LegionScript) | messages | part 2 of tutorial for setting up messaging between users on the site |
| [bbbootstrap](https://bbbootstrap.com/snippets/user-profile-sidebar-12290681) | profile card | inspiration for the profile card design |
| [Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+2021_T1/courseware/eb05f06e62c64ac89823cc956fcd8191/39dfbd4ba6ac42168b5df88d69c32f02/) | password reset email | Boutique ado project section on emails |
| [Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/c6a89f138afe4b209ee4fa6d6f1251a3/?child=first) | pagination & inbox layout | Django blog section on displaying content in rows |
| [Stack Overflow](https://stackoverflow.com/questions/36940384/how-do-i-setup-a-unit-test-user-for-django-app-the-unit-test-cant-login) | automated tests | how to create a user in tests that require user to be logged in |
| [Django Docs](https://docs.djangoproject.com/en/4.1/topics/auth/default/) | post feed views, post/comment delete views, admin panel | only letting logged in users access main site and admins access certain pages |
| [Stack Overflow](https://stackoverflow.com/questions/5235142/how-do-i-disable-the-resizable-property-of-a-textarea) | new post forms | how to disable the resizable property of a textarea |
| [GitHub Gist](https://gist.github.com/niksumeiko/360164708c3b326bd1c8) | message form | how to disable autocomplete in a form field |

### Media

All media files on the website including default profile/background images and images used on landing page and signup/login forms were designed by me using [Canva](https://www.canva.com/).

### Acknowledgements

This project tested me to my limits at times and I could not have seen it to completion without the support of the following people.

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his belief, support, and words of encouragement throughout the development of both this project and all my projects to date.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support that kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my parents, for their constant support and belief throughout this course and project.
- I would like to thank my partner Cayanne, for believing in me, and encouraging me as I make this transition into software development.
- I would like to thank everyone who tested Tribe during development, for their feedback and words of encouragement.