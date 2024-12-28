"""
Member View
===========
Provides an interface for displaying member information.
"""

class MemberView:
    """
    Provides a user interface for library member operations.
    """

    @staticmethod
    def display_members(members):
        """
        Displays all registered members.
        """
        if not members:
            print("No members are currently registered.")
        else:
            print("Library Members:")
            for member in members:
                print(f" - {member}")

    @staticmethod
    def display_member_details(member):
        """
        Displays details of a single member.
        """
        if member:
            print(f"Member Details:\n{member}")
        else:
            print("Member not found.")
