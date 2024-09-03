
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        """Initialize the family members with default values."""
        self._members = [
            {
                "id" : self._generate_Id(),
                "first_name":  "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers" : [7, 13, 22]
            },

            {
                "id" : self._generate_Id(),
                "first_name":  "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers" : [10, 14, 3]
            },
            
            {
                "id" : self._generate_Id(),
                "first_name":  "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers" : [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_Id(self):
        """Generate a random ID for a family member."""
        return randint(0, 99999999)

    def add_member(self, member):
        """Add a new member to the family."""
        new_person = {
            "id" : self._generate_Id(),
            "first_name":  member.get("first_name"),
            "last_name": self.last_name,
            "age": member.get("age"),
            "lucky_numbers" : member.get("lucky_numbers")
        }
        self._members.append(new_person)
        return new_person

    def delete_member(self, id):
        """Delete a member from the family by ID."""
        for member_idex in range(len(self._members)):
            if self._members[member_idex]["id"] == id:
                return self._members.pop(member_idex)
        

    def get_member(self, id):
        """Update an existing member's information."""
        for member in self._members:
            if member["id"] == id:
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        """Retrieve a list of all family members."""
        return self._members
