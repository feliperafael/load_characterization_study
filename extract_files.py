import os
file_temp = "temp_file_sizes.txt"
mylist = [] #contem a lista com o tamanho dos arquivos

# return 1 for int, 2 for float, -1 for not a number
def is_number(s):
    try:
        float(s)
        return 1 if s.count('.')==0 else 2
    except ValueError:
        return -1

def take_file_sizes():
	os.system("ls -l -R | cut -d' ' -f5 > "+str(file_temp))

def clean_file():
	take_file_sizes()
	input_file = open(file_temp, 'r')

	text = input_file.readlines()
	with open(file_temp) as f:
	    temp_list = f.read().splitlines() 

	for item in temp_list :
		if is_number(item) > 0 :
			mylist.append(item)

	input_file.close()

clean_file()

output_file = open('files_sizes.txt', 'w')

for item in mylist:
  output_file.write("%s\n" % item)

os.system("rm "+str(file_temp))
