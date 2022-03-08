from datetime import datetime

class Portfolio:
    def __init__(self, stocks):
        self.stocks = list(stocks)

    def profit(self, init_date, end_date):
        """
        Returns the profit between two dates.
        Parameters:
            init_date (str): Initial date; format %Y-%m-%d
            end_date (str): End date; format %Y-%m-%d
        Returns:
            (float): Profit between init_date and end_date
        """
        try:
            if len(self.stocks) > 0:
                date_format = "%Y-%m-%d"
                d1 = datetime.strptime(init_date, date_format)
                d2 = datetime.strptime(end_date, date_format)

                if d1 < d2:
                    init_price, end_price = 0, 0
                    for i in range(len(self.stocks)):
                        init_price += self.stocks[i].price(init_date)
                        end_price += self.stocks[i].price(end_date)
                    return end_price - init_price
                else:
                    raise ValueError("init_date must be minor than end_date.")
            else:
                raise ValueError("There are no stocks in the portfolio.")
        except Exception as e:
            print(e)
    
    def __str__(self):
        return f"Portfolio({self.stocks})"