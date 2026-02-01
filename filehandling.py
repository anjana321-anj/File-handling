#QN.NO-1
def extract_firstwords(filename):
    first_words_list = []
    with open("sample.txt", 'r') as file:
        for line in file:
            words = line.split()
            if words:
                first_words_list.append(words[0])
    return first_words_list
result = extract_firstwords('sample.txt')
print(result)

#QN.NO-2
with open('a.txt', 'r') as source_file, open('b.txt', 'w') as destination_file:
    for line in source_file:
        destination_file.write(line)
return "File backup completed successfully."


#QN.NO-3
with open("story.txt","r") as file:
    for line_number, line in enumerate(file, start=1):
        words=line.split()
        word_count=len(words)
        print(f"Line {line_number}: {word_count} words")

#QN.NO-4
with open("story.txt","r") as file:
    line_count=0
    for line in file:
        line_count+=1
return f"Total number of lines:{line_count}"


#QN.NO-5
with open('employees.txt', 'r') as source_file, open('management.txt', 'w') as dest_file:
    for line in source_file:
        if 'Python' in line:
            dest_file.write(line)
return "Filtering complete. Lines containing 'Python' have been copied to management.txt."

#QN.NO-6
with open('numbers.txt', 'r') as source, open('squared.txt', 'w') as destination:
    for line in source:
        if line.strip():
            number = int(line.strip())
            squared_number = number ** 2
            destination.write(str(squared_number) + '\n')
return "Calculation complete. Results saved to squared.txt."

#QN.NO-7
user_message = input("Enter the message you want to log: ")
with open('history.log', 'a') as file:
    file.write(user_message + '\n')
return "Message successfully added to history.log."

#QN.NO-8
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        capitalized_line = line.upper()
        outfile.write(capitalized_line)
return "Conversion complete. All text in output.txt is now capitalized."

