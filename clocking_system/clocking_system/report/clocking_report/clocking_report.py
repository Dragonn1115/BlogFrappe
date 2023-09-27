import frappe
from datetime import datetime, timedelta
from frappe.utils import getdate

def get_current_week():
    today = datetime.today().date()
    start_date = today - timedelta(days=today.weekday())  # Monday
    end_date = start_date + timedelta(days=6)  # Sunday
    return start_date, end_date

def execute(filters=None):
    # Get dates for the current week
	if filters and filters != {}:
		try:
			filters = frappe.parse_json(filters)
			start_date = getdate(filters["start_time"]["start_time"])
			end_date = getdate(filters["start_time"]["end_time"])
		except Exception as e:
			start_date, end_date = get_current_week()
	else:
		start_date, end_date = get_current_week()

	dates = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range((end_date - start_date).days + 1)]

	# Initialize dictionary to count occurrences of each person's name for each day
	member_counts = {date: {} for date in dates}

	results = frappe.db.get_all("Clocking by Select", fields=["member1", "member2", "member3", "member4", "member5", "member6", "member7", "date"], filters={"date": ["between", [start_date, end_date]]})
    
	for result in results:
		for field in ["member1", "member2", "member3", "member4", "member5", "member6", "member7"]:
			if result[field]:  # if there is a name for this member field in this result
				name = result[field]
				result_date = result["date"].strftime('%Y-%m-%d')
				if result_date in member_counts:  # Ensure the date exists in the member_counts dictionary
					if name not in member_counts[result_date]:
						member_counts[result_date][name] = 1
					else:
						member_counts[result_date][name] += 1
				else:
					print(f"Unexpected date found in results: {result_date}")

    # Prepare data for display
	all_names = set(name for daily_counts in member_counts.values() for name in daily_counts.keys())
	columns = ["Name"] + dates
	data = []
	for name in all_names:
		row = [name]
		for date in dates:
			row.append(member_counts[date].get(name, 0))
		data.append(row)

	return columns, data


# in some file, maybe clocking_system/clocking_system/api.py
@frappe.whitelist(allow_guest=True)
def get_clocking_report(filters=None):
    # call your report function here
    columns, data = execute(filters)  # or whatever function that gives you the report data
    return {
		"columns": columns,
		"data": data
	}
