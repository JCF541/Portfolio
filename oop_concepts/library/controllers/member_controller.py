"""
Member Controller
=================
Manages operations related to library members.
"""

from library_management.models.member import Member


class MemberController:
    """
    Handles operations related to library members.
    """

    def __init__(self):
        self.members = []

    def add_member(self, name, email):
        """
        Creates and registers a new member.
        """
        member_id = f"M{len(self.members) + 1:03d}"  # Generate a unique ID (e.g., M001)
        member = Member(member_id, name, email)
        self.members.append(member)
        return member

    def find_member(self, member_id):
        """
        Finds a member by their ID.
        """
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def list_members(self):
        """
        Returns a list of all registered members.
        """
        return [str(member) for member in self.members]
