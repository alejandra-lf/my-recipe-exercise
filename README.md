<!-- TEMPLATE SOURCE: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<!-- <br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
 -->
  <h3 align="center">Onboarding backend exercise</h3>

  <p align="center">
    Basic CRUD API for creating and editing recipes
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
	<ul>
        	<li><a href="#get">Get</a></li>
        	<li><a href="#post">Post</a></li>
		<li><a href="#update">Update</a></li>
        	<li><a href="#delete">Delete</a></li>
      </ul>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
The project is focused on managing recipes and ingredients through a CRUD REST API. Built using Python, Django REST Framework, and Docker, this API serves as a practical assessment of the skills and concepts learned throughout an online course.

Required models: 
* Recipe: Name, Description
* Ingredient: Name, Recipe (ForeignKey) ← assume a given ingredient belongs only to one recipe, even if that means multiple Ingredient instances with the exact same name.


For more details take a look in [this notion page](https://www.notion.so/travelperk/Description-of-the-exercise-5db39976c0b34ff0a10ed5c84a6f7fe9)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* Django
* Django REST Framework
* Postgres

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Let's run this... thingy

### Prerequisites

Having installed:
* docker
* docker-compose

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/alejandra-lf/my-recipe-exercise.git
   ```
   
2. Build, start and run the app  
   ```sh
   docker-compose build
   docker-compose up
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Usage -->

## Usage

Note: App should be running by now :)


### Get

In a browser, go to
   ```
   http://localhost:8000/recipes/
   ```

### Post

In the same URL
   ```
   http://localhost:8000/recipes/
   ```
Go to the text field and  paste the following recipe. Then click on POST. Voilà!
   
```
   	{
	"name": "Cheese sandwich",
	"description": "Just put some cheese between two slices of bread.",
	"ingredients": [{"name": "cheese"}, {"name": "bread"}]
	}
   ```
   
### Update

Under construction

### Delete

Under construction


### Django-admin info..create superuser ..
   
<!-- ROADMAP -->
## Roadmap

- [x] Create Docker image
- [x] Create Django project and app
- [x] Create models
- [x] Create serializers, views and urls
- [x] Create GET and POST recipes with ingredients
- [ ] UPDATE and DELETE features
- [ ] Search by name
- [ ] A lot of tests!!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/alejandra-lf/my-recipe-exercise](https://github.com/alejandra-lf/my-recipe-exercise)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
udemy courses, google, stackoverflow, medium, django official docs... Cthulhu!


<p align="right">(<a href="#readme-top">back to top</a>)</p>

