import datetime
 
def get_days_from_today(date):
    try:
        zadana_data = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        potochna_data = datetime.datetime.now().date()
        riznutsa_dniv = potochna_data  - zadana_data 
        return riznutsa_dniv.days
    except ValueError:
        return 'Invalid date format'

print(get_days_from_today("2024-03-15"))  
print(get_days_from_today("2026-01-01")) 
print(get_days_from_today("invalid-date"))  
