import sys
sys.path.insert(0, r"C:\Users\Andrews Razer Laptop\Desktop\CEC Lang")
from core.cec_table_tools import CECTableTools

tools = CECTableTools()
table_data = tools.get_table_data("220.12")

print("="*80)
print("RAW TABLE DATA for Table 220.12")
print("="*80)

# Show raw office row
for row in table_data.get('rows', []):
    if 'Office' in row.get('type_of_occupancy', ''):
        print("\nOffice Row (RAW):")
        print(row)
        break

print("\n" + "="*80)
print("FORMATTED OUTPUT (as LLM sees it)")
print("="*80)

# Now simulate what cec_lookup_table returns
output = [f"CEC 2022 {table_data['table_id']} - {table_data['caption']}"]
output.append(f"Section: {table_data['section']}")
output.append(f"Description: {table_data['description']}")
output.append("")

if table_data.get('headers'):
    output.append("Headers: " + " | ".join(str(h) for h in table_data['headers']))
    output.append("")

# Format rows (THIS IS WHERE THE BUG MIGHT BE)
for row in table_data.get('rows', []):
    if isinstance(row, dict):
        row_parts = []
        for key, value in row.items():
            if key == '_section':
                continue
            # This is the formatting logic from tools.py line 748-751
            key_formatted = key.replace('_', ' ').replace('m2', 'm²').replace('ft2', 'ft²')
            key_formatted = key_formatted.replace(' per ', '/').title()
            row_parts.append(f"{key_formatted}: {value}")
        output.append(" | ".join(row_parts))

print("\n".join(output[:30]))  # Show first 30 lines

# Focus on Office row
print("\n" + "="*80)
print("OFFICE ROW SPECIFICALLY")
print("="*80)
for row in table_data.get('rows', []):
    if 'Office' in row.get('type_of_occupancy', ''):
        row_parts = []
        for key, value in row.items():
            if key == '_section':
                continue
            key_formatted = key.replace('_', ' ').replace('m2', 'm²').replace('ft2', 'ft²')
            key_formatted = key_formatted.replace(' per ', '/').title()
            row_parts.append(f"{key_formatted}: {value}")
        print(" | ".join(row_parts))
        break
