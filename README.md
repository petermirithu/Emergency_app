# E_may

## Built By [E_may](https://github.com/petermirithu/Emergency_app)

## Description
An application that allows users to use that one minute wisely. The users will be able to post an Emergency post and the viewers get the chance of commenting and also having the priviledge of starting a conversation(chatting) about a particular Emergency post.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* View the latest Emergency news posted.
* Comment on the Emergency news.
* View the most recent news(Emergency) posts
* Alerted when a new Emergency news post is made by joining a subscription.
* comment on the different Emergency news and leave feedback.

## Viewer Abilities
These are the behaviours/features that the application implements for use by the writter/viewer

Viewer would like to:
* Sign in to the Emergency News application
* Start a conversation about a particular Emergency news posted from the application

## [Specifications](SPECS.md)

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/petermirithu/Emergency_app/
        $ cd Blogs

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test

## Technologies Used
* Python3.6
* Flask

## [License](license.txt)