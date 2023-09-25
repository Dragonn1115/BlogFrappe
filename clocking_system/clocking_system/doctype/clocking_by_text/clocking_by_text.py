from frappe.website.website_generator import WebsiteGenerator
import json
import frappe

class Clockingbytext(WebsiteGenerator):

    def before_save(self):
        self.process_data()

    def process_data(self):
        # Process data
        temp_text = self.hour_1 + self.hour_2

        print (self.host)
        self.textArray = [str_ for str_ in temp_text.split('@') if str_]
        self.myData = {}

        for key in self.textArray:
            trimmed_key = key.strip()
            if trimmed_key in self.myData:
                self.myData[trimmed_key] += 1
            else:
                self.myData[trimmed_key] = 1

        self.result = f"--童话镇打卡表--\n{self.date}\n{self.host}\n{self.time_period}\n"
        for key, value in self.myData.items():
            self.result += f"@{key} {value} "

        frappe.msgprint(self.result,as_table=True)


        # Emulate local storage using a file or a dictionary
        # try:
        #     with open('local_storage.json', 'r') as f:
        #         all_data = json.load(f)
        # except (FileNotFoundError, json.JSONDecodeError):
        #     all_data = {}

        # if self.selectedDate not in all_data:
        #     all_data[self.selectedDate] = {}

        # total = all_data[self.selectedDate]
        # for key in self.textArray:
        #     trimmed_key = key.strip()
        #     if trimmed_key in total:
        #         total[trimmed_key] += 1
        #     else:
        #         total[trimmed_key] = 1

        # all_data[self.selectedDate] = total

        # with open('local_storage.json', 'w') as f:
        #     json.dump(all_data, f)
