### Timeout 'Where should we go' tool ###

The Time Out team loves to socialise, some of them are also really fussy! In order to spend less time deciding where to go a programme has been created decides for them.

This programme has been written in Python to meet the following user requirements: 
- All members of the team will want both food and drink so if a member of staff cannot eat anything, or no drinks are served that they like, the team will not visit the venue.


## Contents

2 x Python scripts:
- where_should_we_go.py (<-- the __main__ function)
- test_where_should_we_go.py (<-- the unit tests)

2 x JSON input files:
- users.json
- venues.json
...both of these have been cleansed from the original files provided fromm (https://gist.github.com/benjambles/ea36b76bc5d8ff09a51def54f6ebd0cb)

1 x Readme file


## Prerequisites

In addition to Python, the following libraries are required:
- json
- pytest


## Getting Started

The __main__ function should be ran in a python console or command line.

The tool will look through the user list and ask you one by one whether a person is attending - you should answer 'Y' or 'N'.

The tool will then output the results (as per the requirement) into the console / command line


## Sample Output

Below is the json output from current function if all persons are attending the night out
```yaml
{
    "places_to_visit": [
        "Spice of life",
        "The Cambridge"
    ],
    "places_to_avoid": [
        {
            "name": "El Cantina",
            "reason": [
                "There is nothing for Karol to drink",
                "There is nothing for Rosie to eat"
            ]
        },
        {
            "name": "Twin Dynasty",
            "reason": [
                "There is nothing for Wen to eat"
            ]
        },
        {
            "name": "Wagamama",
            "reason": [
                "There is nothing for Karol to drink"
            ]
        },
        {
            "name": "Sultan Sofrasi",
            "reason": [
                "There is nothing for Karol to drink"
            ]
        },
        {
            "name": "Spirit House",
            "reason": [
                "There is nothing for Tom to drink"
            ]
        },
        {
            "name": "Tally Joe",
            "reason": [
                "There is nothing for Karol to drink"
            ]
        },
        {
            "name": "Fabrique",
            "reason": [
                "There is nothing for Karol to drink",
                "There is nothing for Wen to drink"
            ]
        }
    ]
}


## Running the tests

Unit tests, using pytest, have also been created.

You should run pytest test_where_should_we_go.py in a command line or python console.

This will run five unit tests. One of these is known to fail and documented in technical debt. 

See 'test_where_we_should_go.py' for more details on the tests.


## Technical Debt

- Potential ticket to address test_for_missing_venue_food, which tests where function 'can_attendee_eat_at_the_venue' returns a False if restaurant doesnt server any food. 
  At present it returns True, as the food the attendee wont_eat isn't found in the restaurant list, however as per the requirements, all members of the team will want food


## Built With

* [Python 3.8.1]
* [PyCharm Community Edition] (https://www.jetbrains.com/pycharm/) - IDE for Python


## Author(s)

* **David Sagar** - *Initial work* - [davidsagar86@gmail.com]


## License

n/a
