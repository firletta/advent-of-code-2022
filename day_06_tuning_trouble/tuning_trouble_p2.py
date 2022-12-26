input_file = open("input-6.txt","r")
input_data = input_file.read()

for i in range(0, len(input_data) - 13):
    check_for_marker = []
    for j in range(i, i + 14):
        check_for_marker.append(input_data[j])
    if len(set(check_for_marker)) == len(check_for_marker):
            print(f"First start-of-message marker is {check_for_marker}, after {i + 14} characters were processed." )
            break