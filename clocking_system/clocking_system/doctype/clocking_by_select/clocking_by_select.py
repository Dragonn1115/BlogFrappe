# Copyright (c) 2023, Jinglong Zhao and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document


class ClockingbySelect(Document):
	
	
	def before_save(self):
		return
		# Split the time_period field to extract start and end times
		start_time_str, end_time_str = self.time_period.split(" - ")

		# Set the read-only fields with the parsed values
		self.start_time = start_time_str
		self.end_time = end_time_str