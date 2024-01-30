from datetime import datetime


def format_date(date: datetime, format: str='%Y-%m-%d') -> str:
    """
        Formatting the datetime variable

        Parameters
        ----------
            date: datetime,
                Datetime variable
            format: str, default value is '%Y-%m-%d'
                The format to be applied to the date

        Returns
        -------
            A string with the date formatted

        Example
        -------
            format_date(date='1996-10-25 00:00:00.000000', format='%Y-%m-%d')
    """
    return datetime.strftime(date, format=format)


def string_validation(text: str) -> bool:
    """
        Validate a string to ensure it only contains letters 

        Parameters
        ----------
        text : str
            The string to be validated.

        Returns
        -------
        bool
            True if the string is valid, False otherwise.

        Example
        -------
        is_valid = string_validation("Valid_String_123") # Returns False
        is_valid = string_validation("DROGA MAIS") # Returns True
    """
    if any(char.isdigit() or not char.isalnum() and char not in ['_', '-', ' '] for char in text):
        return False
    return True


def string_date_validation(date: str) -> bool:
    """
        Validate a string to ensure it only contains letters 

        Parameters
        ----------
        date : str
            The date as stringto be validated.

        Returns
        -------
        bool
            True if the date is valid, False otherwise.

        Example
        -------
        is_valid = string_date_validation("Valid_String_123") # Returns False
        is_valid = string_date_validation("DROGA MAIS") # Returns True
    """
    if not all(char.isalnum() or char in ['/', '-'] for char in date):
        return False
    return True