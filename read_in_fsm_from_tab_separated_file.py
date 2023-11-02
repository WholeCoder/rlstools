import csv

# Provide the path to your file
file_path = './fsm_states.tsv'

# Initialize an empty list to store the data
data = []

def split_string_at_comma(input_string):
    return input_string.split(',')

# Open the file using the 'with' statement to ensure proper closing
with open(file_path, 'r', newline='') as file:
    # Specify the delimiter as tab
    tsv_reader = csv.reader(file, delimiter='\t')
    
    # Iterate over each row and append it to the data list
    for row in tsv_reader:
        data.append(row)

transition_events = data[0][1:]

print(transition_events)

states = []
for row in data[1:]:
    states.append(row[0])

print(states)

out = "\t\tstateDict = {\n"
i = 1
for state in states:
    out += "\t\t\t'" + state + "':{\n"
    
    
    j = 1
    for event in transition_events:
        new_state_and_action_to_take = split_string_at_comma(data[i][j]) 
        out += "\t\t\t\t'" + event + "':('"+  new_state_and_action_to_take[0] + "',"+ new_state_and_action_to_take[1] +")"
        if event != "e":
            out += ","
        out += "\n"
        j += 1
    #out += "\t}"
    i += 1
    out += "\t\t\t}" 
    if state != "M":
        out += ","
    
    out += "\n"

out += "\t\t}\n"
print(out)
