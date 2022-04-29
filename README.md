# 25Hours-HotelBookingManagementSystem
25 hours is a hotel management system where hotel owners can post their available rooms and information. And the customers can book their hotel rooms they like.

# To run this system following steps should be followed:
1. Database is handled through MySQL as we should create '25 Hours' named database
2. Run code in terminal: python manage.py runserver
3. To create superuser:  python manage.py createsuperuser

# Tools and Technology 
1. HTML5 and CSS3
While talking about web development HTML and CSS comes first as HTML is 
used to structure content on a webpage whereas CSS adds distinctive styles
to it. All the images, texts, forms, buttons, hyperlinks, etc. are inserted and 
positioned, and styling using these in this project. 
2. Bootstrap 5
It is the most widely used CSS framework for creating fully responsive 
websites. As it is easy to learn quickly if we know HTML, CSS, and JavaScript. 
The first step in building a page is to build a grid layout for it. As the use of 
smartphones grows, responsive grid systems are becoming increasingly 
important. Any confusion in front-end design will have a direct influence on the 
website's credibility, and we will lose users' confidence. Bootstrap's grid 
system can divide the screen into twelve equal columns and adapt the 
components according to the screen size because it was created with "MobileFirst" in mind. This makes the front end of our website mobile-friendly. We can 
also use the grid system's classes to hide and expose parts on specific 
devices.
3. JavaScript
JavaScript is used to add interactive components that keep users engaged in 
UI. As it is mostly used programming language in the world. The user's 
bandwidth restricts the communication between JavaScript and the server-side 
software. Therefore, JavaScript functions are prioritized for efficiency, and the 
quantity of data transmitted between applications is kept to a minimum. With 
the use of JavaScript event listeners and functions, my projects will be more 
interactive. 
4. Django (python framework)
Django is an open-source backend web application framework developed on 
Python, one of the most popular online programming languages. Its primary 
aims are simplicity, flexibility, dependability, and scalability. It is one of the 
easiest back-end frameworks, making it easy to learn and apply in projects. 
(Korsun, 2021)
There are many frameworks like Node.js, PHP, Laravel, etc. but I have chosen 
to manage the backend system with this framework as it is easy to learn and 
understand. The automated admin interface reads information from our models 
to make a model-centric interface for dependable users to manage content on 
the website. The admin's suggested usage is confined to the inner
management means of an organization. It is not supposed to be the base for 
our entire front end.
Django itself gives user authentication as well as its authorization which means 
all these authentication and authorization are managed by the Django 
authentication system. In common sense, authentication justifies that a user is 
who they say they are, however, authorization chooses what an authenticated 
individual can do. Both tasks are stated as authentication in this perspective.
This helps us to manage users easier for us.
5. MySQL
MySQL is a relational database management system that you might utilize to 
operate our databases. It is Oracle-backed open-source software. It indicates
that we may use MySQL for free. We may also edit the source code to suit 
your needs if you like. (Anon., n.d.)
All the database of my system is managed with this database management 
system. All though Django itself gives MySQL lite to manage system data I 
have chosen MySQL. MySQL is supported by a large number of cluster 
servers. Whether we are storing huge volumes of significant e-Commerce data 
or making serious business intelligence projects, MySQL can assist us to run 
efficiently and instantly. As well it is free to use.


# User Manual
25 Hours website is easy to use as it has been developed user-friendly website as you can see on the home page of the system below.
![image](https://user-images.githubusercontent.com/95069886/165972388-d281cc0d-ee59-4a09-a81c-983e2d500a2a.png) 
Figure: Home page of 25 Hours

1)	Registration
a)	Simply click on the signup button for the registration of the user.
 ![image](https://user-images.githubusercontent.com/95069886/165972674-afaec6da-e695-4c15-a249-066d6994a8e5.png)
Figure: Sign up page of 25 Hours

b)	After we fill up the signup form click on the signup button to register.
![image](https://user-images.githubusercontent.com/95069886/165972744-8ccc3a41-f555-4130-ac66-a564ce0032f1.png)
Figure: Input forms on the signup page


2)	Log in

a)	After successful registration click on the login button from the navbar of the home page
![image](https://user-images.githubusercontent.com/95069886/165972809-0d1c7d2d-f130-4bd5-99d2-8a5345e6fd52.png)
Figure: Login page of 25Hours

b)	After we need to put a valid username and password and click on the login button for opening our user’s home page.
 ![image](https://user-images.githubusercontent.com/95069886/165972925-2f3c511d-b6db-4905-a35e-b016cada157e.png)
Figure: Input form on the login page

3)	Search
a)	Now users can search for their needed place rooms through the search bar by filling queries needed there.
 ![image](https://user-images.githubusercontent.com/95069886/165972979-6a6f0297-bc26-4b3b-acde-fd6eee644c0a.png)
Figure: Search function on 25 Hours home page

b)	Now we can see available rooms for such queries on the available rooms page
 ![image](https://user-images.githubusercontent.com/95069886/165973061-291c4e92-0fdd-4c1e-ac2e-d0e29bcb6270.png)
Figure: Available rooms page on 25 Hours

c)	As we can see from the above figure our search results will appear on the available rooms page.

4)	View Details
By clicking the view details button, we can view the details of the selected rooms.
![image](https://user-images.githubusercontent.com/95069886/165973129-f7226bcc-34d9-45c9-b5b9-938dd8558d5c.png)
Figure: Selected room details page on 25 Hours

5)	Reserve Room
Now we can reserve rooms by filling in check-in and check-out dates on the right side form of the room details and clicking the reserve button.
 ![image](https://user-images.githubusercontent.com/95069886/165973179-e1036132-525e-4f14-b42d-1e108ba0a83d.png)
Figure: Reserving room in 25 Hours

6)	Payment
a)	After reservations payment page will load where we must pay the given price to book.
 ![image](https://user-images.githubusercontent.com/95069886/165973230-42fd5e0e-3f55-4d6a-8667-f9361dd8af90.png)
Figure 51 Payment page of 25 Hours

b)	Now we can pay using Khalti for booking our room through the payment with the Khalti button.
 ![image](https://user-images.githubusercontent.com/95069886/165973257-c39391bb-2468-4cf8-a92d-bc2a0c300829.png)
Figure: Khalti payment method on 25 Hours

c)	Above popup form will appear where we must give a valid Khalti mobile number and pin. And then we need to confirm it by filling confirmation code on it. After that, we can pay for the booking of this room will be booked. 

7)	User Profile
From the profile button on the navbar, we can view our booking details as shown below figure.
![image](https://user-images.githubusercontent.com/95069886/165973312-7eb083b5-112e-40f4-8d21-de4b5a320ae4.png)
Figure: Booking details on the user profile of 25 Hours

8)	Adding rooms
a)	Hotel owners must contact an admin so that they can add their room details on this website.
b)	After they are registered, they can now log in through the same page where other users are logged in.
c)	After they were logged in the main difference between customer users and hotel owners is while the hotel owner will log in there become a host button will appear on the navbar where they can fill in their available room details,
 ![image](https://user-images.githubusercontent.com/95069886/165973424-36965b40-80ea-4bb3-a54c-e954ba73edf1.png)
Figure: Home page for hotel owner user in 25 Hours

d)	Now hotel owners can add their rooms details on add room page
![image](https://user-images.githubusercontent.com/95069886/165973467-7ec122ad-107c-417e-82ab-dce6bc61241e.png)
Figure: Add room page in 25 Hours


e)	Now we can fill up forms and click on the register now button to host our hotel room
![image](https://user-images.githubusercontent.com/95069886/165973511-e3c6eae0-39f4-442a-a1fc-7ee35d009dbd.png)
Figure: Filling forms in add room page of 25 Hours


9)	Owner Profile
We can view hotel details which we have added and who book our hotel rooms from the profile button.
 ![image](https://user-images.githubusercontent.com/95069886/165973573-7f034a58-897e-410d-8e7d-c5fd1a1bda68.png)
Figure: Owner profile on 25 Hours

10)	Logout
Users can simply log out by just clicking the logout button from the navbar.

