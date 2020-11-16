"""A Budget App."""


class Category:
    """
    The Categories object contains different budget categories.

    Parameters
    ----------
    category_name : str
        The name of the category

    Attributes
    ----------
    name : str
        The name of the category
    ledger : list
        The account or record used to store entries for balance-sheet and transactions

    """

    def __init__(self, category_name):
        """Initialize a Category."""
        self.name = category_name
        self.ledger = []

    def deposit(self, amount, description=""):
        """
        Append an object to the ledger list.

        Parameters
        ----------
        amount : float
            The amount to add to ledger
        description : string
            The description of the transaction

        Returns
        -------
        self.ledger
            An update of the ledger list
        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        Append an object to the ledger list.

        Parameters
        ----------
        amount : float
            The amount to remove from ledger
        description : str
            The description of the transaction

        Returns
        -------
        self.ledger
            An update of the ledger list
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": (-1) * amount, "description": description})
            return True
        return False

    def get_balance(self):
        """
        Calculate the current balance of the budget category.

        Returns
        -------
        balance
            The total amount in the ledger
        """
        balance = 0
        for action in self.ledger:
            balance += action['amount']
        return balance

    def transfer(self, amount, other):
        """
        Add a withdrawal with the amount and the description to the this object and \
        a deposit to another budget category.

        Parameters
        ----------
        amount : float
            The amount to remove from ledger
        other : object
            The budget category that the money are transferred to

        Returns
        -------
        bool
            True if the transfer is possible otherwise False
        """
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to {}".format(other.name))
            other.deposit(amount, "Transfer from {}".format(self.name))
            return True
        return False

    def check_funds(self, amount):
        """
        Check if there are enough funds.

        Parameters
        ----------
        amount : float
            The amount to remove from ledger

        Returns
        -------
        bool
            True if enough funds otherwise False
        """
        if amount <= self.get_balance():
            return True
        return False

    def __str__(self):
        """Display the budget object."""
        output = self.name.center(30, '*') + "\n"
        for action in self.ledger:
            output += "{:<23}".format(action["description"][:23])
            output += "{:>7.2f}".format(action["amount"])
            output += "\n"
        output += "Total: {}".format(self.get_balance())
        return output


def create_spend_chart(categories):
    """
    Show the percentage spent in each category.

    Parameters
    ----------
    categories : list
        A list of the budget categories

    Returns
    -------
    output
        A string that is a bar chart
    """
    names = []
    withdrawals = []

    for category in categories:
        names.append(category.name)
        withdrawals.append(category_withdrawals(category))

    percentages = [round_down(100 * withdrawal / sum(withdrawals),
                              10) for withdrawal in withdrawals]

    output = "Percentage spent by category\n"
    output += print_percentages(percentages)
    output += print_names(names)
    return output


def category_withdrawals(category):
    """
    Sum the amount of withdrawals in a category.

    Parameters
    ----------
    category : object
        A budget object

    Returns
    -------
    withdrawals
        The total amount of withdrawals in category
    """
    withdrawals = 0
    for action in category.ledger:
        if action["amount"] < 0:
            withdrawals += abs(action["amount"])
    return withdrawals


def round_down(num, divisor):
    """
    Round a number down.

    Parameters
    ----------
    num : float
        The number to round down
    divisor : int
        The nearest number to round to
    """
    return num - (num % divisor)


def print_percentages(percentages):
    """
    Draw the bar chart of the percentages.

    Parameters
    ----------
    percentages : list
        The list of percentages of the withdrawals in the categories

    Returns
    -------
    output
        A string that is a bar chart
    """
    output = ""
    for num in range(100, -1, -10):
        output += "{:>3}| ".format(num)
        for perc in percentages:
            output += 'o  ' if perc >= num else '   '
        output += "\n"
    output += " " * 4 + "-" * (3 * len(percentages) + 1) + "\n"
    return output


def print_names(names):
    """
    Draw the bar chart of the percentages.

    Parameters
    ----------
    names : list
        The list of names of the categories

    Returns
    -------
    output
        A string that is the x-label of the bar chart
    """
    output = ""
    for i in range(max_length(names)):
        output += " " * 4
        for name in names:
            output += " " + name[i] + " " if i < len(name) else " " * 3
        output += " \n" if i < (max_length(names) - 1) else ""
    output += " "
    return output


def max_length(names):
    """Calculate the max length in names."""
    return max([len(name) for name in names])
