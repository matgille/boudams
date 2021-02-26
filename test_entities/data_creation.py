import random
import sys


def main(file):
    random.seed(2324)
    with open(file, "r") as input_file:
        string_list = input_file.readlines()
        output_filename = file.replace(".txt", "dataed.txt")

        output_strings_list = []
        for line in string_list:
            for character in line:
                if character == " ":
                    random_number = random.randint(1, 11)
                    if random_number % 3 == 0:
                        pass
                    else:
                        output_strings_list.append(character)
                else:
                    random_number = random.randint(1, 21)
                    if random_number == 10:
                        output_strings_list.append(" ")
                        output_strings_list.append(character)
                    else:
                        output_strings_list.append(character)
        

        output_strings = "".join(output_strings_list)
        with open(output_filename, "w") as output_file:
            output_file.write(output_strings)



if __name__ == '__main__':
    main(sys.argv[1])

