"""
Member Controller
==================
Manages operations related to library members.
"""

from models.member import Member


class MemberController:
    """
    Handles operations related to library members including addition, updates, and deletions.
    """

    def __init__(self):
        self.members = []

    def add_member(self, name, email):
        """
        Create and register a new member.

        Args:
            name (str): Name of the member.
            email (str): Email of the member.
        
        Returns:
            Member: The newly added member instance.
        """
        member = Member(name=name, email=email)
        self.members.append(member)
        return member

    def find_member(self, member_id):
        """
        Find a member by their ID.

        Args:
            member_id (str): The ID of the member.
        
        Returns:
            Member: The member instance if found, None otherwise.
        """
        return next((member for member in self.members if member.member_id == member_id), None)

    def update_member(self, member_id, **updates):
        """
        Update a member's attributes.

        Args:
            member_id (str): The ID of the member to update.
            updates (dict): The fields to update with their new values.
        
        Returns:
            bool: True if the member was found and updated, False otherwise.
        """
        member = self.find_member(member_id)
        if not member:
            return False

        for key, value in updates.items():
            if hasattr(member, key) and value is not None:
                setattr(member, key, value)

        return True

    def delete_member(self, member_id):
        """
        Remove a member by their ID.

        Args:
            member_id (str): The ID of the member to delete.
        
        Returns:
            bool: True if the member was found and deleted, False otherwise.
        """
        member = self.find_member(member_id)
        if member:
            self.members.remove(member)
            return True
        return False

    def list_members(self):
        """
        List all registered members.

        Returns:
            list: A list of string representations of the members.
        """
        return [str(member) for member in self.members]
