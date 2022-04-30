from datetime import datetime, timedelta
import requests
import sys

start_date = datetime.strptime(sys.argv[1], "%Y%m%d")
end_date = datetime.strptime(sys.argv[2], "%Y%m%d")
days = (end_date - start_date).days + 1

json_res_list = []
rate_list = []


class Excange:
    def __init__(self, url):
        self.url = url

    def get_info(self):
        for day in range(days):
            date = start_date + timedelta(days=day)
            date_str = date.strftime('%Y%m%d')
            url = self.url
            json_res = requests.get(f"{url}={date_str}&json").json()
            json_res_list.append(json_res)
            rate_list.append(json_res[0]['rate'])
            print(json_res)

    def print_info(self):
        print(f"Min rate {json_res_list[rate_list.index(min(rate_list))]}")
        print(f"Max rate {json_res_list[rate_list.index(max(rate_list))]}")


exchange = Excange("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=THB&date")
exchange.get_info()
exchange.print_info()
