import datetime as dt

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.datetime.now().date()

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        now = dt.datetime.now().date()
        today_stats = 0
        for record in self.records:
            if record.date == now:
                today_stats += record.amount
        return today_stats    
             
    def get_week_stats(self):
        now = dt.datetime.now().date()
        week_ago = now - dt.timedelta(days = 7)
        week_stats = 0
        for record in self.records:
            if week_ago <= record.date <= now:
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        today_stats = self.get_today_stats()
        if today_stats < self.limit:
            remainder = self.limit - today_stats
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remainder} кКал'
        else:
            return 'Хватит есть!'
   
class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0
    
    def convert_cash(self, cash, currency):
        if currency == 'usd':
            cash = '%.2f' % (cash / self.USD_RATE) 
            return f'{cash} USD'
        elif currency == 'eur':
            cash = '%.2f' % (cash / self.EURO_RATE)
            return f'{cash} Euro'
        return f'{cash} руб'

    def get_today_cash_remained(self, currency):
        
        total_today = self.get_today_stats()
        if total_today < self.limit:
            remainder = self.limit - total_today
            return 'На сегодня осталось ' + self.convert_cash(remainder, currency)
        elif total_today > self.limit:
            debt = total_today - self.limit
            return 'Денег нет, держись: твой долг - ' + self.convert_cash(debt, currency)
        else:
            return 'Денег нет, держись'
