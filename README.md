# Re-Right Backend
The backend consists of two main apps: UserApp and PostApp. UserApp includes classes and functions for user authentication, registering, and logging in users as well as updating user information. PostApp includes Post, Like, and Comment classes and functions that allow users to create, edit, and delete posts, like and unlike posts, and add and delete comments. Using the REST framework, we built APIs for both posts and users which allow you to add, view and modify data. The backend also includes the chat feature which is in a separate repository (Re-Right-chat-app: https://github.com/TechForGoodInc/Re-Right-chat-app). 

## Getting Started
1. Clone this repository
2. Create a virtual environment
3. Install Django and Django REST Framework
4. Follow the steps in this document to complete setting up: [backend setup.pdf](https://github.com/TechForGoodInc/Re-Right-Backend/files/6977248/backend.setup.pdf)

  ## PostApp
   Includes classes, functions, and APIs for viewing and modifying posts, liking and unliking posts, and adding and deleting comments. 
   * **models.py**: contains Post, Like, and Comment classes. The Post class includes a Tag enum class which stores the Human Rights as stated by the UN. 
      * **Note**: In order to display comments under their respective posts, a custom manager may need to be used. This will allow only the comments pertaining to each post to be displayed (this should be done by filtering the comments according to the post ID). 


   * **serializers.py**: includes serializers which allow data corresponding to Post, Comment, and Like objects to be converted to/from JSON.
   * **urls.py**: includes the urls that map to the views defined in views.py. As of now, creating, editing, and deleting posts can be done through the API, for example, to create a post, go to localhost:8000/papi/post-creation/ and to edit a post with an id of 1, go to localhost:8000/papi/post-edit/1

   * **views.py**: contains views, functions, and viewsets that allow viewing and modifying data regarding posts through the APIs, posts cannot be liked or commented on using the APIs, however the functions for liking/unliking and adding/deleting comments should work as expected. 
    
  ## UserApp
   Includes classes, functions, and API's for registering, logging in, and managing users. 
   * **models.py**: includes a User class, an account manager that creates users, and a function that creates tokens when users are added.
   * **serializers.py**: contains a serializer for the User API and a serializer for registering users. 
   * **urls.py**: includes url that maps to the registration_view, go to localhost:8000/uapi/ to view the User API.
   * **views.py**: includes API view for registration, viewsets for User and functions for updating user information and for user authentication. 

