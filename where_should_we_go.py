import json

# Load json into dict for both files
venue_file = open("venues.json", "r")
venues_dict = json.load(venue_file)

users_file = open("users.json", "r")
users_dict = json.load(users_file)


def choose_users():
    # Input to choose names and create list of attendees
    attendees = []
    for user in users_dict:
        choice = input(f"Is {user['name']} coming on the night out? Y/N")
        if choice == 'Y':
            attendees.append(user)
    return attendees
    # TODO: Make it graphical?


def can_attendee_eat_at_the_venue(venue, attendee):
    # Looping through all foods served at the venue, compare with the attendees wont eat foods
    for food in venue['food']:
        if food not in attendee['wont_eat']:
            return True  # Only need one food being served by venue to be acceptable by each attendee
    return False  # If all foods being served at a venue are on the attendees won't eat list, that person cannot attend venue


def can_attendee_drink_at_the_venue(venue, attendee):
    # Looping through all drinks liked by a attendee, compare with those server at the venue
    for drink in attendee['drinks']:
        if drink in venue['drinks']:
            return True  # Only need one drink liked by the attendee to be served by the venue
    return False  # If all drinks liked by the attendees are not served at the venue, that person cannot attend the venue


def produce_output(places_to_visit, places_to_avoid):
    # Create the output in the specified format from the requirements doc
    output = {}
    output['places_to_visit'] = places_to_visit
    output['places_to_avoid'] = places_to_avoid
    return json.dumps(output, indent=4)


if __name__ == '__main__':
    attendees = choose_users()

    total_attendees = len(attendees)
    places_to_visit = []
    places_to_avoid = []
    reasons = []

    # Go venue by venue assessing suitability for attendees
    for venue in venues_dict:
        # Create two new lists for every venue being assessed - users that can attend and reasons users cannot attend
        venue_attendees = []
        reasons_for_venue = []

        for attendee in attendees:
            # Assess each attendee's ability to visit the venue
            can_eat = can_attendee_eat_at_the_venue(venue, attendee)
            can_drink = can_attendee_drink_at_the_venue(venue, attendee)

            first_name = attendee['name'].split(" ")[0]  # To be used in the reasons for not attending

            if can_eat and can_drink:
                venue_attendees.append(attendee)  # Add attendee to list if they can eat and drink at a venue
            elif can_eat and not can_drink:
                reasons_for_venue.append(f'There is nothing for {first_name} to drink')  # Add attendee to list if they can eat but not drink
            elif can_drink and not can_eat:
                reasons_for_venue.append(f'There is nothing for {first_name} to eat')  # Add attendee to list if they can't eat
            else:
                reasons_for_venue.append(f'There is nothing for {first_name} to drink')
                reasons_for_venue.append(f'There is nothing for {first_name} to eat')

        # Add the details of why people cant visit venue if any entries exist in reasons_for_venue, otherwise add the venue to places to visit
        if len(reasons_for_venue) > 0:
            places_to_avoid.append({"name": venue['name'], "reason": reasons_for_venue})
            reasons.append(places_to_avoid)
        else:
            places_to_visit.append(venue['name'])

    output_json = produce_output(places_to_visit, places_to_avoid)

    print(output_json)
