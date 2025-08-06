import datetime


class Transaction:
    def __init__(self, amount, type, category, date, note):
        self.amount = amount
        self.type = type
        self.category = category
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.note = note
        
    
    def __str__(self):
        return f"{self.date.date()} - {self.trans_type.upper()} - {self.category}: ${self.amount:.2f} - {self.note}"

        