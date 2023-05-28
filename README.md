# DARK CHOCOLATE FOR EVER

This is my th project for my Diploma in Software Dev Course and it’s been built for educational purposes only. 

The purpose of the e-commerce website is to sell dark chocolate to chocolate lovers offering them a various flavours of dark chocolate, some of them very unusual or exotic. 

!!! ADD MOCKUP CREATED IN https://ui.dev/amiresponsive

## Showcase

A deployed link to the website can be found [here](https://dark-chocolate-for-ever.herokuapp.com/)

To test payments you can use the following test details:

Card no: 4242 4242 4242 4242
Expiry date: 04/24
CSV: 242
ZIP: 42424

------
## Table of Contents
1. Business

2. UX
Project Goals
User Stories
Design

3. Features
Existing Features:
	- Products App
	- Home App
	- Bag App
	- Checkout App
    - Reviews App
    - Newsletter App
    - Profiles App
- Base Template
Features to be implemented

4. Database Structure
5. CRUD Operations and Defensive Design
6. Technologies Used:
    - Languages
    - Libraries and Packages
    - Tools
    - Databases
7. Testing:
    - Automated Testing:
    - Manual Testing: Feature Testing, Stripe Payment Testing, Responsivness

8. Deployment:
 - Heroku Deployment (incl AWS) 
 - Local Deployment

9. Marketing and SEO:
 - SEO: Keywords used:
 - FB page
 - Newsletter signup

10. Credits:
 - Content
 - Code 
 - Images and Media 
 - Acknowledgements

------
## 1. Business

### Business Model

My e-commerce website follows a Business to Consumer business model (B2C) which means that when consumers go online to search for dark chocolate and they find my website, they can browse through my store. When they find products they would like to purchase, they will place an order: place items into the shopping bag, add their payment details and pay for their purchase. Once order has been placed they will receive an order confirmation, and their order would be processed and despatched. Once the consumer would receive their goods, they would have an option to log in and rate the products received and leave a review if they wish. 

## 2. UX

### Project Goals

#### Target Audience
- Chocolate lovers, specifically people who enjoy eating dark chocolate
- Chocolate lovers with specific dietary needs like vegan, paleo, gluten-free, sugar-free, dairy-free
- People who would like to buy sweet and healthier gifts for their loved ones who love dark chocolate and/ or have a special dietary requirements like vegan, paleo, gluten-free, sugar-free, dairy-free

### User Goals / Site Visitor’s Goals
- Familiariaze themselves with a wide range of dark chocolate products available on the UK market by browsing this online shop and reading reviews
- Purchase products in a hassle-free, fast and secure way

### Site Owner’s Goals
- Establish a trusted brand and recognizable brand voice
- Provide their target audience with a safe e-commerce that enables them a hassle free 1st class customer experience
- Collect payments for their products and shipping services


### User Stories

**Viewing and Navigation**

1. As a Shopper I can view a list of products so that I can select some to purchase
2. As a Shopper I can view a specific category of products so that I can quickly find products I’m interested in without having to search through all products
3. As a Shopper I can view individual product details so that I can identify the price, description, product rating, product image and product weight
4. As a Shopper I can identify deals, clearance items and special offers so that I can take advantage of special savings on products I'd like to purchase
5. As a Shopper I can easily view the total of my purchases at any time so that I can avoid spending too much

**Registration and User Accounts**

6. As a Site User I can easily register for an account so that I can have a personal account and be able to view my profile
7. As a Site User I can easily login and logout so that I can access my personal account information
8. As a Site User I can easily recover my password in case I forget it so that I can recover access to my account
9. As a Site User I can receive an email confirmation after registering so that I can verify that my account registration was successful
10. As a Site User I can have a personalized user profile so that I can view my personal order history and order confirmations, and save my payment information

**Sorting and Searching**

11. As a Shopper I can sort the list of available products so that I can easily identify the best rated, best priced and categorically sorted products
12. As a Shopper I can sort a specific category of product so that I can find the best-priced or best-rated product in a specific category, or sort the products in that category by name
13. As a Shopper I can sort multiple categories of products simultaneously so that I can find the best-priced or best-rated products across broad categories, as as "chocolate bars" or "chocolate truffles"
14. As a Shopper I can search for a product by name or description so that I can find a specific product I'd like to purchase
15. As a Shopper I can easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available

**Purchasing and Checkout**

16. As a Shopper I can easily select the quantity of a product when purchasing it so that I can ensure that I don't accidentally select the wrong product and quantity
17. As a Shopper I can view items in my bag so that I can identify the total cost of my purchase and all items I will receive
18. As a Shopper I can adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout
19. As a Shopper I can easily enter my payment information so that I can check out quickly and with no hassles
20. As a Shopper I can feel my personal and payment information is safe and secure so that I can confidently provide the needed informatio to make a purchase
21. As a Shopper I can view an order confirmation after check out so that I can verify that I haven’t made any mistakes
22. As a Shopper I can receive an email confirmation after checking out so that I can keep the confirmation of what I’ve purchased for my records

------

### Design TO FOLLOW

#### Wireframes created with balsamiq:


#### Brand Colours / Colour Palette


#### Typography
‘Lato’ used as a main font and 'Dancing Script' used as 'logo font'.

--- 

## 3. FEATURES

---

## 4. DATABASE STRUCTURE

I have used a relational database for this project. SQLite/Postgress was used as the main database, all data migrated to Heroku and then due to the recent Heroku changes it was successfully migrated to ElephantSQL.

![database-modeling.png](./docs/images/database-modeling.png)

I have created the following separate apps and inclueded my custom models:

- Contact app / ContacUs model
- Reviews app / ProductReview model
- Newsletter app/ Newsletter model


---

## 5. CRUD OPERATIONS AND DEFENSIVE DESIGN

---

## 6. TECHNOLOGIES USED

### Languages Used
- HTML5, Boostrap framework
- CSS3
- JavaScript
- Python, Django library
- SQLLite/Postgress

### Frameworks, Libraries and Programs Used

- Canva.com: Canva Color Palette Generator was used to create a color palette and Canva was used to create a mock-up design, and for resizing and editing images.
- Git: Git was used for version control by utilizing the Gitpod terminal - to commit to Git and push to GitHub
- GitHub: Github is used to store the project's code after being pushed from Git.
- GoogleDev Tools used to see the element positioning and responsiveness
- [Google Fonts](https://fonts.google.com/): Google fonts ‘Lato’ and 'Dancing Script' were used. 
- favicon.io was used to create the favicon
- FontAwesome used for social media icons: FB, IG, YT

- [amiresponsive](http://ami.responsivedesign.is/) was used to create the mockup for Readme
- Validation services: W3C Markup Validation, W3C CSS Validation, PEP8 Validation

---

## 7. TESTING

I have tested this project manually and completed also some auto testing via the online validation services. See the full details on a separate page [HERE.](https: add THE TESTING.md FILE LINK HERE!!)

---

## 8. DEPLOYMENT

### Deployment to Heroku

This site was deployed to Heroku pages by taking the following steps:

1. Log into your Heroku account
2. On your right hand side, click on the button ‘New’ and then click ‘create a new app’
3. Name your app and chose a region, then click ‘Create app’ button below
4. Click on the Settings in the tab
5. Click add Buildpack to add 2 buildpack as follows: first `heroku/python` and then `heroku/nodejs`, save changes
6. You must then create a Config var (click reveal Config Vars under the Settings, just above the Buildpack) called `PORT` (under key) and set it to `8000` (under value) and click add, then hide Config Vars
7. Click Deploy on the tab and chose deployment method: connect to your GitHub repository
8. Search for your repository, once found, connect.
9. Scroll down to Manual deploy and click ‘Deploy branch’. Your app will be built.
10. Once you ‘App was successfully deployed’ message and button with your deployed link, you can click on it to see your app.


## Forking the GitHub Repository OR Making a Local Clone

If you are interested how to fork this repository or how to make a local clone, this information can be found in Github documentation [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

---

## 9. Marketing and SEO

### Marketing

As this business has currently no marketing budget for paid advertising, it relies purely on the two following unpaid marketing strategies:

**Social Media Presence**
posting on Facebook - the Facebook page can be found [here](https://www.facebook.com/DarkChocolateForEver/)

**Email Marketing Strategy**
enabled by signing up to a newsletter via a Newsletter signup form.

### SEO

Keyword Serch carried out:



---

## 10. Credits

### Code

- The majority of the code came from the Django Walkthrough projects (Boutique Ado and Blog) and the Diploma in Software Development study materials, my notes taken during going through the materials and by working with Google DevTools - trial and error approach.

- Additonal knowledge used from the following courses: [The Boostrap 4 Camp](https://www.udemy.com/course/bootstrap-4-bootcamp/)

- [MDN Web Docs](https://developer.mozilla.org/en-US/): Used extensively to deepen my knowledge and understanding of HTML and CSS, and chek for ideas and solutions, specifically:  

- For Contact form/ Query model: Youtube [Django Tutorial #9: A More Complex Form (2022) by Django tutorials](https://www.youtube.com/watch?v=-qAf_Qx6Ygg)

- [Djangoproject documentation](https://docs.djangoproject.com/en/4.1/)

- Stackoverflow

- For 404 and 500 Error pages [this youtube tutorial](https://www.youtube.com/watch?v=zSEexM0GspU) and [this article](https://freefrontend.com/html-funny-404-pages/)

-  Mentor’s advice

### Content

- All content was written by the developer. 

### Media

- Hero image taken by [XXX](https://unsplash.com/photos/Wu7hYE7Lzzs)  
 downloaded from unspleash.com


### Acknowledgements

- My family
- My Mentors Guido Cecilio and Chris Quinn for their patience and great insights.
- Tutor support at Code Institute for their support.

- Code Institute Slack Community for all their advice and support.

------
