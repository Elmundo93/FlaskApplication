
from abc import ABC, abstractmethod

class IStorage(ABC):
    @abstractmethod
    def list_data(self):
        """
        Returns a dictionary of movies.
        Example:
        {
          "Titanic": {"rating": 9, "year": 1999, "poster": "url_to_image"},
          ...
        }
        """
        pass

    @abstractmethod
    def add_data(self, author, title, content ):
        """
        Adds a movie with the given parameters.
        """
        pass

    @abstractmethod
    def delete_data(self, id, author, title):
        """
        Deletes the movie with the given title.
        """
        pass

    @abstractmethod
    def update_data(self, id, author, title, content):
        """
        Updates the movie’s rating.
        """
        pass