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
        Validate a string to ensure it only contains numbers and characters such as '/', '-'. 

        Parameters
        ----------
        date : str
            The date as string to be validated.

        Returns
        -------
        bool
            True if the date is valid, False otherwise.

        Example
        -------
        is_valid = string_date_validation("2020-01-08a") # Returns False
        is_valid = string_date_validation("2020-01-08") # Returns True
    """
    if not all(char.isalnum() or char in ['/', '-'] for char in date):
        return False
    return True


def string_amount_validation(amount: str) -> bool:
    """
        Validate a string to ensure it only contains numbers and ',' to ensure that the string
        represents a amount value.

        Parameters
        ----------
        amount : str
            The amount as string to be validated.

        Returns
        -------
        bool
            True if the amount is valid, False otherwise.

        Example
        -------
        is_valid = string_amount_validation("40.68A") # Returns False
        is_valid = string_amount_validation("400.14") # Returns True
    """
    try:
        amount = float(amount)
        return True
    except:
        return False


def string_is_alphanumeric(text: str) -> bool:
    """
        Verifies if the string is alphanumeric or not.

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
        is_valid = string_date_validation("Yuri_Domaradzki") # Returns True
    """
    if not all(char.isalnum() for char in text):
        return False
    return True