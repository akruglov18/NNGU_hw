import numpy as np
import matplotlib.pyplot as plt

def calculate(average_student_count, count_groups, isOffline) :
    overall = 0 # the entire cost
    full_rate = 10                      # one lecturer conducts 10 lessons in a week if he work full time
    conducting_different_lessons = 3    # one lecturer can't conduct more different lections than 3
    labor_tax = 0.3                     # employer pays tax for each employee
    count_lessons_month = 8             # count month when lessons are conducted 
    
    # array for all persons
    all_count_array = []
    
    #average needed classrooms
    average_count_classroom = count_groups * 3
    
    # 1 semester
    lections = [8, 8, 8, 8, 16, 16, 16, 8, 8, 16]
    practics = [8, 8, 16, 8, 8, 16]
    labs     = [8, 8, 8]
    # one year
    lections = lections * 2
    practics = practics * 2
    labs = labs * 2
    
    if(isOffline == 1) :
        all_count_array.append(average_student_count * count_groups)
    # salaries
    #calculated for one month
    salaries = []
    
                                                    # service workers
    # supercomputer's supporters
    salary_supporters = 30000
    count_supporters = 2
    salaries.append(salary_supporters * count_supporters)
    all_count_array.append(count_supporters)
    
    # lab's supporters
    salary_supporters = 30000
    count_supporters = 2
    salaries.append(salary_supporters * count_supporters)
    all_count_array.append(count_supporters)
    
                                                    # cloakroom_attendants
    salary_cloakroom_attendants = 25000
    count_cloakroom_attendants = 4
    salaries.append(salary_cloakroom_attendants * count_cloakroom_attendants)
    all_count_array.append(count_cloakroom_attendants)
    
                                                    # cleaners
    salary_cleaners = 25000
    count_cleaners = 8
    salaries.append(salary_cleaners * count_cleaners)
    all_count_array.append(count_cleaners)
    
                                                    # accountants
    salary_accountants = 50000
    count_accountants = 2
    salaries.append(salary_accountants * count_accountants)
    all_count_array.append(count_accountants)
    
                                                    # guards 
    salary_guards = 35000
    count_guards = 6
    salaries.append(salary_guards * count_guards)
    all_count_array.append(count_guards)
    
                                                    # methodists
    salary_methodists = 45000
    count_methodists = 3
    salaries.append(salary_methodists * count_methodists)
    all_count_array.append(count_methodists)
    
                                                    # some inside university workers
    #university workers who organize university infrastructure
    salary_others_employees = 40000
    count_others_employees = 25
    salaries.append(salary_others_employees * count_others_employees)
    all_count_array.append(count_others_employees)
    
                                                    # some outside university workers
    #responsible for outside's university (cleaning snow, etc...)
    salary_cleaners = 25000
    count_cleaners = 4
    salaries.append(salary_cleaners * count_cleaners)
    all_count_array.append(count_cleaners)
    
                                                    #dormitory workers
    # administrator                                        
    salary_administrator = 50000
    count_administrator = 1
    salaries.append(salary_administrator * count_administrator)
    all_count_array.append(count_administrator)
    
    # commandant                                        
    salary_commandant = 50000
    count_commandant = 1
    salaries.append(salary_commandant * count_commandant)
    all_count_array.append(count_commandant)
    
    # guards
    salary_guards = 35000
    count_guards = 3
    salaries.append(salary_guards * count_guards)
    all_count_array.append(count_guards)
    
    # castellan
    salary_castellan = 35000
    count_castellan = 1
    salaries.append(salary_castellan * count_castellan)
    all_count_array.append(count_castellan)
                                          
                                                    # in buffet
    #saleswoman(cleaning snow, etc...)
    salary_saleswomans = 25000
    count_saleswomans = 2
    salaries.append(salary_saleswomans * count_saleswomans)
    all_count_array.append(count_saleswomans)
    
    # cooks
    salary_cooks = 25000
    count_cooks = 4
    salaries.append(salary_cooks * count_cooks)
    all_count_array.append(count_cooks)
    
                                                    # web-sites developers
    salary_developers = 80000
    count_developers = 3
    salaries.append(salary_developers * count_developers)
    all_count_array.append(count_developers)
    
                                                    # lectors
    average_lectors_salary = 50000
    # needed count lector
    all__count_lessons = (sum(lections) + sum(practics)*count_groups + sum(labs) * count_groups)
    count_lectors = (all__count_lessons + full_rate - 1) // full_rate
    different_count_lessons = (len(lections) + len(practics)*count_groups + len(labs)*count_groups)
    count_lectors = max(count_lectors, different_count_lessons // conducting_different_lessons)
    salaries.append(average_lectors_salary * count_lectors)
    
    salaries.append(salary_others_employees * count_others_employees)
    all_count_array.append(count_lectors)
    
    # all people
    all_persons_count = sum(all_count_array)
    without_students_count = all_persons_count - count_groups * average_student_count
    
    #calculations
    added_payment = 0
    
                                                                            # Internet
    needed_internet = 10000 * 12
    added_payment = added_payment + needed_internet
    
                                                                            # update tecnhical equipment every 5 year
    # projector, tables
    updating_equipment = average_count_classroom * 30000 // 5
    added_payment = added_payment + updating_equipment
    
    # 1/3 is a terminal classes
    # computer for each student in classrom
    average_computer_count = 0
    average_computer_count = average_computer_count + average_count_classroom * average_student_count // 3
    average_computer_count = average_computer_count + count_methodists
    average_computer_count = average_computer_count + count_others_employees
    average_computer_count = average_computer_count + count_lectors
    
    # reserve and for some reasons
    average_computer_count = average_computer_count + 40
    
                                                                            # keyboards, mouses...
    added_payment = added_payment + average_computer_count * 1000
    
                                                                            # additional licensed software
    additional_licensed_software = average_computer_count * 20000
    added_payment = added_payment + additional_licensed_software
    
                                                                            #lego robots, boards
    # every 5 years
    added_payment = added_payment + 100000 // 5
    
                                                                            # update computers every 5 year(costs for one year)    
    updating_computers = average_computer_count * 50000 // 5
    added_payment = added_payment + updating_computers
    
    # update tables, chairs ...
    added_payment = added_payment + all_persons_count * 25000 // 5
    
                                                                            # educational supplies
    # average officies(papers, pencils ....) in one year
    added_payment = added_payment + all_persons_count * 2000 * 12
    
    # chalk, markers
    added_payment = added_payment + 2000 * 12
    added_payment = added_payment + 2000 * 12
    
                                                                            # buffet
    # value is low because some foods are paybecked
    # and not all students eats in canteen
    # 25 days at month all year
    food = (average_student_count // 2) * 5000 * count_lessons_month
    added_payment = added_payment + food
                                                                            # personal hygiene products
    # liquid soap
    added_payment = added_payment + 300 * all_persons_count * 12
    
    # napkins, paper towels
    added_payment = added_payment + 500 * all_persons_count * 12
    
                                                                            # anti-covid measures
    # 3 masks on each persons
    added_payment = added_payment + all_persons_count * 3 * 100
    
    # disinfection lamps
    added_payment = added_payment + 500000
    
    # antiseptic
    added_payment = added_payment + 100 * all_persons_count * 12
    
    # room's disinfection
    added_payment = added_payment + 10000 * 12
    
                                                                            # events
    # university pays student's trips for year
    # 5 % of all students
    added_payment = added_payment + (average_student_count // 20) * 1500
                                                                            
                                                                            # web-site support
    #servers
    added_payment = added_payment + 10000 * 12
    
                                                                            # electricity
    #when studying is going
    needed_electricity = average_computer_count * 3000 * count_lessons_month
    # when studying isn't going
    # it is unnecessary to turn on computers in terminal
    unnecessary = average_count_classroom * average_student_count // 3
    needed_electricity = needed_electricity + (average_computer_count - unnecessary) * 3000 * (12 - count_lessons_month)
    
    #lighting
    needed_electricity = needed_electricity + 20000
    #charging laptops, phones ...
    needed_electricity = needed_electricity + all_persons_count * 300 * count_lessons_month
    needed_electricity = needed_electricity + without_students_count * 200 * (12 - count_lessons_month)
    added_payment = added_payment + needed_electricity
                                                                            # water
    # 150 is payment for each person
    #when studying is going
    needed_water = all_persons_count * 150 * count_lessons_month
    added_payment = added_payment + all_persons_count * 150 * count_lessons_month
    #when studying isn't going   
    needed_water = without_students_count * 150 * (12 - count_lessons_month)
    added_payment = added_payment + needed_water
    
                                                                            # heating
    # sitting places, wardrobe, work places ....
    # 15 m^2 for each persons
    average_heating_square = all_persons_count * 15
    added_payment = average_heating_square * 12 * 40
    
                                                                            # rent
    added_payment = all_persons_count* 15 * 1500
    
    added_payment = added_payment + sum(salaries) * (1 + labor_tax)
    overall = overall + added_payment
    
    return added_payment

count_groups = 4
average_count_students_in_group = np.arange(10, 30, 2)
learning_costs = []
isOffline = 1
for x in average_count_students_in_group :
    value = calculate(x, count_groups, isOffline)
    learning_costs.append(value)

students_count = average_count_students_in_group * count_groups
print("Online")
print("Learning costs summary:")
print(learning_costs)
plt.semilogy(students_count,learning_costs, linewidth = 5)
plt.xlabel('Количество студентов')
plt.ylabel('Суммарная стоимость стоимость обучения')
plt.title('Стоимость обучения')
plt.show()
pass

print("Learning costs ratio:")
print(learning_costs / students_count)
plt.semilogy(students_count, learning_costs / students_count, linewidth = 5)
plt.xlabel('Количество студентов')
plt.ylabel('Относительная стоимость стоимость обучения')
plt.title('Относительная стоимость обучения')
plt.show()
pass

count_groups = 4
average_count_students_in_group = np.arange(10, 30, 2)
learning_costs = []
isOffline = 0
for x in average_count_students_in_group :
    value = calculate(x, count_groups, isOffline)
    learning_costs.append(value)

students_count = average_count_students_in_group * count_groups
print("Offline")
print("Learning costs summary:")
print(learning_costs)
plt.semilogy(students_count,learning_costs, linewidth = 5)
plt.xlabel('Количество студентов')
plt.ylabel('Суммарная стоимость стоимость обучения online')
plt.title('Стоимость обучения online')
plt.show()
pass

print("Learning costs ratio:")
print(learning_costs / students_count)
plt.semilogy(students_count, learning_costs / students_count, linewidth = 5)
plt.xlabel('Количество студентов')
plt.ylabel('Относительная стоимость стоимость обучения online')
plt.title('Относительная стоимость обучения online')
plt.show()
pass
