<!-- TEMPLATE SOURCE: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<!-- PROJECT LOGO -->
<!-- <br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
 -->
  <h3 align="center">Django and DRF excercise</h3>

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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

CRUD API with Django and DRF that allows you to CRUD recipes and add/delete ingredients to it. It can be tested it using postman or similar.

Based on Udemy course... blah blah

Reuested models: 
* Recipe: Name, Description
* Ingredient: Name, Recipe (ForeignKey) ← assume a given ingredient belongs only to one recipe, even if that means multiple Ingredient instances with the exact same name.

### Example recipe creation

 ```js
   POST /recipes/
{
	"name": "Pizza",
	"description": "Put it in the oven",
	"ingredients": [{"name": "dough"}, {"name": "cheese"}, {"name": "tomato"}]
}

Response:
{
	“id”: 1,
	“name”: “Pizza”
	“description”: “Put it in the oven”,
	“ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
}
   ```

### Example recipe creation

 ```js
GET /recipes/
[
    {
	    “id”: 1,
      “name”: “Pizza”
	    “description”: “Put it in the oven”,
	    “ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
    }
]
   ```
   
   ### Example recipe edit

 ```js
PATCH /recipes/1/
    {
	    "name": "Pizza",
	    "description": "Put it in the oven",
	    "ingredients": [{"name": "casa-tarradellas"}]
    }


Should delete the previous existing ingredients and put “casa-tarradellas” as only ingredient for recipe.

Response:
{
	“id”: 1,
	“name”: “Pizza”
	“description”: “Put it in the oven”,
	“ingredients”: [{“name”: “casa-tarradellas”}]
}
   ```
   
   ### Example recipe delete

 ```js
DELETE /recipes/1/


Response:
HTTP 204 (NO CONTENT)


Should delete the targeted recipe AND its ingredients.
   ```
Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template!

For more details visit[this notion page](https://www.notion.so/travelperk/Description-of-the-exercise-5db39976c0b34ff0a10ed5c84a6f7fe9)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Django
* Django REST Framework
* Postgres

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Some intro text here

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* docker
* docker-compose
* and so on

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/alejandra-lf/my-recipe-exercise.git
   ```
2. Docker ... 
   ```sh
   docker-compose build
   docker-compose up
   ```
3. ...


<p align="right">(<a href="#readme-top">back to top</a>)</p>



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

Project Link: [https://github.com/your_username/repo_name](https://github.com/alejandra-lf/my-recipe-exercise

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments



<p align="right">(<a href="#readme-top">back to top</a>)</p>

