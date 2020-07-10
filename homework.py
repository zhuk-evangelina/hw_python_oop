import datetime as dt

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        now = dt.date.today()
        today_stats = [record.amount for record in self.records 
            if record.date == now]
        return sum(today_stats)  
             
    def get_week_stats(self):
        now = dt.date.today()
        week_ago = now - dt.timedelta(days = 7)
        week_stats = [record.amount for record in self.records 
            if week_ago <= record.date <= now]
        return sum(week_stats)
    
    def get_today_remained(self):
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        remainder = self.get_today_remained()
        if remainder > 0:
            return ('Сегодня можно съесть что-нибудь ещё, '
                f'но с общей калорийностью не более {remainder} кКал')
        return 'Хватит есть!'
   

class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0
    RUB_RATE = 1.0

    currencies = {
        'eur': ('Euro', EURO_RATE),
        'usd': ('USD', USD_RATE),
        'rub': ('руб', RUB_RATE),
    }

    def get_today_cash_remained(self, currency):
        currency_text, currency_rate = self.currencies[currency]    
        remainder = round(self.get_today_remained() / currency_rate, 2)

        if not remainder: 
            return 'Денег нет, держись'
        elif remainder < 0:
            debt = abs(remainder)
            return f'Денег нет, держись: твой долг - {debt} {currency_text}' 
        return f'На сегодня осталось {remainder} {currency_text}' 
        
            
           
