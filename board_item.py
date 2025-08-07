from datetime import date, timedelta
from item_status import ItemStatus

def add_days_to_now(d):
    return date.today() + timedelta(days = d)

class BoardItem:
    
    def __init__(self, title : str, due_date):
        
        if not 4 < len(title) < 31:
            return 'Description should be between 5 and 30 characters.'
        if due_date < date.today():
            return 'Due Date should not be in the past.'

        self.title = title
        self.due_date = due_date
        self.status = ItemStatus.OPEN

    def revert_status(self):
        if self.status != 'Open':
            new_status = ItemStatus.previous(self.status)
            self.status = new_status

    def advance_status(self):
        if self.status != 'Verified':
            new_status = ItemStatus.next(self.status)
            self.status = new_status
    
    def info(self):
        return f'{self.title}, [{self.status} | {self.due_date}]'