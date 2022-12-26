input_file = open("input-6.txt","r")
input_data = input_file.read()

for i in range(0, len(input_data) - 3):
    check_for_marker = [input_data[i], input_data[i + 1], input_data[i + 2], input_data[i + 3]]
    if len(set(check_for_marker)) == len(check_for_marker):
            print(f"First start-of-packet marker is {check_for_marker}, after {i + 4} characters were processed." )
            break