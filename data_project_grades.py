# IMPORTS
import csv
import statistics

def stats_output(list):
  print("MEAN: ", round(statistics.mean(list), 2))
  print("MEDIAN: ",round(statistics.median(list), 2))
  print("STDEV: ",round(statistics.stdev(list), 2))


# semester variables
fall_semester = []
spring_semeter = []


# opening/reading the CSV file
grades_csv = "sample_grades.csv"
with open(grades_csv, 'r') as file:
  csv_reader = csv.reader(file)

  for line in csv_reader:
    # print(line)
    # print(line[0], line[1], line[3])
    if line[1] == 'Spring 2016':
      spring_semeter.append(eval(line[2]))
    else:
      fall_semester.append(eval(line[2]))

# print(statistics.mean(fall_semester))
file.close()


# main testing function
def main():
  print("SPRING SEMESTER: ", spring_semeter)
  stats_output(spring_semeter)
  print()
  print("FALL SEMESTER:   ", fall_semester)
  stats_output(fall_semester)

main()
