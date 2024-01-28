from datetime import datetime


def format_date(date: datetime, format: str) -> str:
    """
        Formatting the datetime variable

        Parameters
        ----------
            date: datetime,
                Datetime variable
            format: str,
                The format to be applied to the date

        Returns
        -------
            A string with the date formatted

        Example
        -------
            format_date(date='1996-10-25 00:00:00.000000', format='%Y-%m-%d')
    """
    return datetime.strftime(date, format=format)