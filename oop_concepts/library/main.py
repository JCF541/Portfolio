"""
Library Management Application
==============================
Main entry point for the application.
"""

from models.app import App

if __name__ == "__main__":
    app = App()
    app.run()
