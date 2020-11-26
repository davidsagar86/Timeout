import pytest
from where_should_we_go import can_attendee_eat_at_the_venue

def test_for_no_match():
    """Testing that 'can_attendee_eat_at_the_venue' returns a True when the attendee's wont_eat food doesn't
    match what the venue serves"""
    venue = {'name': 'El Cantina', 'food': ['Mexican'], 'drinks': ['Soft drinks', 'Tequila', 'Beer']}
    attendee = {'name': 'Danielle Ren', 'wont_eat': ['Fish'], 'drinks': ['Cider', 'Rum', 'Soft drinks']}
    assert can_attendee_eat_at_the_venue(venue, attendee) == True


def test_for_match():
    """Testing that 'can_attendee_eat_at_the_venue' returns a False when the attendee's wont_eat food is the only
     food being served at the venue"""
    venue = {'name': 'Tally Joe', 'food': ['Fish'], 'drinks': ['Beer', 'Cider', 'Soft Drinks', 'Sake']}
    attendee = {'name': 'Danielle Ren', 'wont_eat': ['Fish'], 'drinks': ['Cider', 'Rum', 'Soft drinks']}
    assert can_attendee_eat_at_the_venue(venue, attendee) == False


def test_for_match_but_other_options():
    """Testing that 'can_attendee_eat_at_the_venue' returns a True when the attendee's wont_eat food is served
     by the venue but other options are available"""
    venue = {'name': 'Tally Joe', 'food': ['Fish', 'Mexican'], 'drinks': ['Beer', 'Cider', 'Soft Drinks', 'Sake']}
    attendee = {'name': 'Danielle Ren', 'wont_eat': ['Fish'], 'drinks': ['Cider', 'Rum', 'Soft drinks']}
    assert can_attendee_eat_at_the_venue(venue, attendee) == True


def test_for_no_attendee_food():
    """Testing that 'can_attendee_eat_at_the_venue' returns a True when the attendee has no food they won't_eat"""
    venue = {'name': 'Tally Joe', 'food': ['Fish'], 'drinks': ['Beer', 'Cider', 'Soft Drinks', 'Sake']}
    attendee = {'name': 'Danielle Ren', 'wont_eat': [''], 'drinks': ['Cider', 'Rum', 'Soft drinks']}
    assert can_attendee_eat_at_the_venue(venue, attendee) == True


def test_for_missing_venue_food():
    """Testing that 'can_attendee_eat_at_the_venue' returns a False if restaurant doesnt server any food"""
    venue = {'name': 'El Cantina', 'food': [''], 'drinks': ['Soft drinks', 'Tequila', 'Beer']}
    attendee = {'name': 'Danielle Ren', 'wont_eat': ['Fish'], 'drinks': ['Cider', 'Rum', 'Soft drinks']}
    assert can_attendee_eat_at_the_venue(venue, attendee) == False
    #TODO: Failure found - users need to eat but current logic returns a false positive if the food they wont_eat isn't
    # found in the venue food
