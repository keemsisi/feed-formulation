'''
	Objective function: Maximize 10x1 + 6x2 + 4x3
		Subject to   x1 + x2 + x3 <= 100
			     10x1 + 4x2 + 5x3 <= 600
			     2x1 + 2x2 + 6x3 <= 300
			     x1 >= 0, x2 >= 0, x3 >= 0
'''

from optlang import Model, Variable, Constraint, Objective

# All the (symbolic) variables are declared, with a name and optionally a lower and/or upper bound.
x1 = Variable('x1', lb=0)
x2 = Variable('x2', lb=0)
x3 = Variable('x3', lb=0)
x4 = Variable('x4', lb=0)
x5 = Variable('x5', lb=0)
x6 = Variable('x6', lb=0)
x7 = Variable('x7', lb=0)
x8 = Variable('x8', lb=0)
x9 = Variable('x9', lb=0)

# LOWER BOUND >=
#UPPER BOUND <=

"""--------------------------==============----------------New Modification goes thus--------==============--------------------------------------"""
# A constraint is constructed from an expression of variables and a lower and/or upper bound (lb and ub).
# the number of ingredients selected is N... so Variable(x,bound=value) for the formulation will range from 1... N + 1
#Let N be the total number of ingredients selected...
#Another thing we will do is to sum up all the contraints and save them in another object called variable_sum
#N  = 100

variable_objects = [] # stores all the contraints for the formulation
#assuming the user selected the following ingredients
selected_ingredients = ['Maize', 'Soybean_meal','Wheat_bran','Oyster_shell','Bone_meal','Salt','Lysine','Methionine','Premix']
#Note: the selected ingredients will be used to get the value of their nutrients composition from the database of the animal feed ingredients
"""The feed size is the amount in kilogram (kg) the buyer wants to get from the feed formulator, this should be collected from the client side"""
feed_size = 100
#assuming the user selected finisher as the animal stage for broilers
selected_animal_stage = "Finisher"
#assuming the user select the following type of animal
animal_selected = "Broiler"
all_const = "";

variable_sum  = None
for i in range( 1 , len(selected_ingredients)+1 ):
    ing = Variable('x{0}'.format(i), lb=0)
    if i == 1 :
        variable_sum = ing
    elif i > 1 :
        variable_sum += ing
    variable_objects.append(ing)
# print(variable_objects)
# print(variable_sum)

#the next step is to build the constraints for the formulation
#we will build the contraints using the value of the ingredients respective nutrients compositions for the the particular animal maximum and minimum nutrient value
#let's build the first contraint for the formulation

#but before then, the demand reqirement will be the variable_sum, so all we need to do is to assign the variable_sum to the first contraint
contraint_sum = None

#############################################---- LOAD THE CORRECT VALUES FOR THE FEEDING COMPOSITION------##############################################
#########################################################################################################################################################
dummy_animal_db = {
    "Broiler":{
         "Starter":{
            "Fat":{
                "Max":3.55,
            },
            "Energy":{
                "Min":2826.39
            },
            "Lysine":{
                "Min":1.26,
            },
            "Methionine":{
                "Min":0.42,
            },

            "Crude_Fibre":{
                "Max":4.09
            },

            "Crude_Protein":{
                "Min":20.87,
            },

            "Phosphorus":{
                "Min":0.58
            },

            "Calcium":{
                "Equal":1.86,
            },
            "Salt":{
                "Equal":0.3,
            },
            "premix":{
                "Equal":0.3
            }
        },




#################################################################################################
        "Finisher":{
            "Fat":{
                "Max":3.51
            },
            "Energy":{
                "Min":2766.67
            },
            "Lysine":{
                "Min":1.16,
            },
            "Methionine":{
                "Min":0.40,
            },

            "Crude_Fibre":{
                "Max":4.11
            },

            "Crude_Protein":{
                "Min":19.25,
            },

            "Phosphorus":{
                "Min":0.56
            },

            "Calcium":{
                "Equal":2.20,
            },

            "Salt":{
                "Equal":0.30
            },
            "premix":{
                "Equal":0.30
            }
        }
    }
}
#####################################################################################################################################
#----------------------------------------LOAD THE ORIGINAL DATA BELOW IN THE GIVEN PATTERN------------------------------------------#
#####################################################################################################################################
dummy_ing_db = {
    "Maize": {"ing":{
                "Fat":4.00,"Crude_Protein": 8.8,"Energy":3432, "Crude_Fibre": 2.00,"Lysine":0.25,"Methionine":0.18,"Phosphorus":0.09,"Calcium":0.01,"Salt":0.00,"premix":0.00},"Price":58},

    "Soybean_meal":  {"ing":{
                "Fat":3.50,"Crude_Protein": 44.0,"Energy":2230, "Crude_Fibre": 6.50,"Lysine":2.80,"Methionine":0.59,"Phosphorus":0.20,"Calcium":0.20,"Salt":0.00,"premix":0.00},"Price":150},

    "Fish_meal": {"ing": {
        "Fat": 4.50, "Crude_Protein": 60.065, "Energy": 2820, "Crude_Fibre": 1.00, "Lysine": 4.50, "Methionine": 1.80,"Phosphorus": 3.00, "Calcium": 6.10, "Salt": 0.00,"premix":0.00}, "Price": 36},

    "PKC":  {"ing":{
        "Fat": 4.00, "Crude_Protein": 8.50, "Energy": 3350, "Crude_Fibre": 2.00, "Lysine": 0.25, "Methionine": 0.18,"Phosphorus": 0.9, "Calcium": 0.01, "Salt": 0.00,"premix":0.00}, "Price": 105},

    "GNC":{"ing":{
        "Fat": 4.00, "Crude_Protein": 8.50, "Energy": 3350, "Crude_Fibre": 2.00, "Lysine": 0.25, "Methionine": 0.18,"Phosphorus": 0.9, "Calcium": 0.01, "Salt": 0.00,"premix":0.00}, "Price": 105},

    "Wheat_offal":{"ing":{
        "Fat": 3.50, "Crude_Protein": 10.20, "Energy": 3120, "Crude_Fibre": 0.00, "Lysine": 0.00, "Methionine": 0.00,"Phosphorus": 0.00, "Calcium": 0.00, "Salt": 0.00,"premix":0.00}, "Price": 56
    },
    "Wheat_bran":{"ing":{
        "Fat": 0.00, "Crude_Protein": 15.70, "Energy": 1300, "Crude_Fibre": 5.10, "Lysine": 0.59, "Methionine": 0.42,"Phosphorus": 1.15, "Calcium": 0.14, "Salt": 0.00,"premix":0.00}, "Price": 60
    },
    "Oyster_shell": {"ing":{
                            "Fat": 0.00, "Crude_Protein": 0, "Energy": 0.00, "Crude_Fibre": 0.00, "Lysine": 0.00, "Methionine": 0.00,"Phosphorus": 18.50, "Calcium": 21.00, "Salt": 0.00,"premix":0.00}, "Price": 15},
    "Bone_meal": {"ing":{
                            "Fat": 0.00, "Crude_Protein":0.00, "Energy": 0, "Crude_Fibre": 0.00, "Lysine": 0.00, "Methionine": 0.00,"Phosphorus": 1.50, "Calcium":38.00, "Salt": 0.00,"premix":0.00}, "Price": 50},

    "Lime_stone": {"ing":{
        "Fat": 0.00, "Crude_Protein": 0.00, "Energy": 0, "Crude_Fibre": 0.00, "Lysine": 0.00, "Methionine": 0.00,"Phosphorus": 0.00, "Calcium": 35.00, "Salt": 0.00,"premix":0.00}, "Price": 8,
    },

    "Salt": {"ing":{
                            "Fat": 0.00, "Crude_Protein": 0.00, "Energy": 0, "Crude_Fibre": 0.00, "Lysine": 0.00, "Methionine": 0.00,"Phosphorus": 0.00, "Calcium": 0.00, "Salt": 100.00,"premix":0.00}, "Price": 90},
    "Lysine": {"ing":{
        "Fat": 0.00, "Crude_Protein": 60.00, "Energy": 0, "Crude_Fibre": 0.00, "Lysine": 100.00, "Methionine": 0.00,"Phosphorus": 0.00, "Calcium": 0.00, "Salt": 0.00,"premix":0.00}, "Price": 700},

    "Methionine": {"ing":{
        "Fat": 0.00, "Crude_Protein": 60.00, "Energy": 0, "Crude_Fibre": 0.00, "Lysine": 0.00, "Methionine": 100.00,
        "Phosphorus": 0.00, "Calcium": 0.00 ,"Salt": 0.00,"premix":0.00}, "Price": 1300},

    "Premix": {"ing":{
        "Fat": 0.00, "Crude_Protein": 0.00, "Energy": 0, "Crude_Fibre": 0.00, "Lysine": 0.00, "Methionine": 0.00,
        "Phosphorus": 0.00, "Calcium": 0.00, "Salt": 0.00,"premix":100.00}, "Price": 550},
}
##############################################----------------------------------#############################################
#############################################################################################################################


#this should be constants to solve the formulation
#do not change
c1 = Constraint(variable_sum,lb = feed_size )
# c2 = Constraint(variable_sum,ub = feed_size )
contraints_list = []
#append the fisrt two constraints into the contraints_list.
contraints_list.append(c1)
# contraints_list.append(c2)

print(variable_sum, "LB",feed_size, "\n")


temp_var_sum =None

# print(dummy_animal_db[animal_selected][selected_animal_stage])
# if the user selects finisher broiler


#This will return the keys in the finisher's feed contraints
for nutrient in dummy_animal_db[animal_selected][selected_animal_stage]:
    """now we will iterate through the returned nutrient compositions for the finisher broiler"""
    for bound in dummy_animal_db[animal_selected][selected_animal_stage][nutrient]:
        count = 0
        # print("BOUND=>",bound)

        for ing_name in selected_ingredients:
            # print("\nIngredient ====>",ing_name,"\n")
            if count == 0:
                # print("\n\n--------------Another contraints goes from here-----------------------------")
                if nutrient !="Energy":
                    temp_var_sum = (dummy_ing_db[ing_name]["ing"][nutrient]/100)*variable_objects[count]
                    # print(temp_var_sum,end=" ")
                    count = count + 1
                else :
                    temp_var_sum = dummy_ing_db[ing_name]["ing"][nutrient] * variable_objects[count]
                    # print(temp_var_sum,end=" ")
                    count = count + 1

                # print(count)
            elif count > 0 :
                # print("\n\n--------------Another contraints goes from here-----------------------------")
                if nutrient != "Energy":
                    temp_var_sum += (dummy_ing_db[ing_name]["ing"][nutrient] / 100) * variable_objects[count]
                    # print(temp_var_sum,end=" ")
                    count = count + 1
                else :
                    temp_var_sum += dummy_ing_db[ing_name]["ing"][nutrient] * variable_objects[count]
                    # print(temp_var_sum,end=" ")
                    count = count + 1

############################Then we build the contraints from here after the sum of the constraints has been generated##############################

        # print("\n\n--------------Another contraints goes from here-----------------------------")
        # print("NUTRIENT ===> ",nutrient)
        # print(temp_var_sum, end=" ")
        # print("BOUND=>",bound, end=" ")
        # print("=",dummy_animal_db[animal_selected][selected_animal_stage][nutrient][bound])


        if bound == "Min":
                contraints_list.append(Constraint(temp_var_sum,lb=dummy_animal_db[animal_selected][selected_animal_stage][nutrient][bound]))
                print(temp_var_sum,">=", dummy_animal_db[animal_selected][selected_animal_stage][nutrient][bound])

        elif bound == "Max":
                contraints_list.append(Constraint(temp_var_sum,ub=dummy_animal_db[animal_selected][selected_animal_stage][nutrient][bound]))
                print(temp_var_sum,"<=", dummy_animal_db[animal_selected][selected_animal_stage][nutrient][bound])

        elif bound == "Equal":
            contraints_list.append(Constraint(temp_var_sum, lb=dummy_animal_db[animal_selected][selected_animal_stage][nutrient][bound]))
            contraints_list.append(Constraint(temp_var_sum, ub=dummy_animal_db[animal_selected][selected_animal_stage][nutrient][bound]))
            print(temp_var_sum, ">=",dummy_animal_db[animal_selected][selected_animal_stage][nutrient][bound])
            print(temp_var_sum, "<=",dummy_animal_db[animal_selected][selected_animal_stage][nutrient][bound])

        # all_const+=temp_var_sum

####################################################################################################################################################

print("\nCONTRAINTS===>",contraints_list.__len__(),end="\n\n\n")
print("ALl Constraints =================================")
print(all_const)

#constructing the object function from here
objective_sum = None
for i in range( 0 , len(selected_ingredients)):
    if i == 0 :
        objective_sum  = dummy_ing_db[selected_ingredients[i]]["Price"]*variable_objects[i]
    elif i > 0 :
        objective_sum += dummy_ing_db[selected_ingredients[i]]["Price"]*variable_objects[i]
    # print(objective_sum)
print("OBJECTIVE FUNCTION ====> ",objective_sum,end="\n\n\n\n")


obj = Objective(objective_sum,direction='min')
# Variables, constraints and objectives are combined in a Model object, which can subsequently be optimized.
model = Model(name='Simple model')
model.objective = obj
model.add(contraints_list)
status = model.optimize()

print("status:", model.status)
print("objective value:", model.objective.value)
print("---------------------------------------------------------------------")
for var_name,  var in model.variables.items():
    print(var_name, "=", var.primal)







#c1 = Constraint(x1+ x2+ x3+ x4+ x5+ x6+ x7+ x8+ x9,lb= 100 )
# c2 = Constraint(x1+ x2+ x3+ x4+ x5+ x6+ x7+ x8+ x9,ub= 100 )
# c3 = Constraint(0.088*x1+0.44*x2+0.157*x3+ 0*x4 + 0*x5 + 0*x6 + 0.6*x7+0.6*x8 + 0*x9, lb=20.87)
# c4 = Constraint(0.04*x1 +0.035*x2 + 0*x3 + 0*x4 + 0*x5 + 0*x6 + 0*x7 + 0*x8 + 0*x9 ,ub= 3.55)
# c5 = Constraint(0.02*x1+0.065*x2+0.051*x3 + 0*x4 + 0*x5 + 0*x6 + 0*x7 + 0*x8 + 0*x9 ,ub= 4.09)
# c6 = Constraint(0.0001*x1+0.002*x2+0.0014*x3+0.21*x4+0.38*x5 + 0*x6 + 0*x7 + 0*x8 + 0*x9 ,ub= 1.86)
# c7 = Constraint(0.0009*x1+0.002*x2+0.0115*x3+0.185*x4+0.015*x5 + + 0*x6 + 0*x7 + 0*x8 + 0*x9 ,lb=0.58 )
# c8 = Constraint(0.0025*x1+0.028*x2+0.0059*x3 + 0*x5 + 0*x6 + x7 + 0*x8 + 0*x9,lb= 1.26 )
# c9 = Constraint(0.0018*x1+0.0059*x2+0.0042*x3+0*x5 + 0*x6 + 0*x7 + x8 + 0*x9,lb=0.42 )
# c10 = Constraint(3432*x1 + 2230*x2 + 1300*x3+ + 0*x4 + 0*x5 + 0*x6 + 0*x7 + 0*x8 + 0*x9,lb= 2826.39)
# c11 = Constraint(0*x1 + 0*x2 + 0*x3 + 0*x4 + 0*x5 + x6 + 0*x7 + 0*x8 + 0*x9, ub=0.3)
# c12 = Constraint(0*x1 + 0*x2 + 0*x3 + 0*x4 + 0*x5 + x6 + 0*x7 + 0*x8 + 0*x9, lb=0.3)
# c13 = Constraint(0*x1 + 0*x2 + 0*x3 + 0*x4 + 0*x5 + 0*x6 + 0*x7 + 0*x8 + x9, ub=0.3)
# c14 = Constraint(0*x1 + 0*x2 + 0*x3 + 0*x4 + 0*x5 + 0*x6 + 0*x7 + 0*x8 + x9, lb=0.3)
# c15 = Constraint(0.0001*x1+0.002*x2+0.0014*x3+0.21*x4+0.38*x5 + 0*x6 + 0*x7 + 0*x8 + 0*x9 ,lb= 1.86)









# # An objective can be formulated
# obj = Objective( 58*x1+150*x2+60*x3+15*x4+50*x5+90*x6+700*x7+1300*x8+550*x9
#  ,direction='min')
#
# # Variables, constraints and objectives are combined in a Model object, which can subsequently be optimized.
# model = Model(name='Simple model')
# model.objective = obj
# model.add([c1, c2, c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15])
# status = model.optimize()
#
# print("status:", model.status)
# print("objective value:", model.objective.value)
# print("-------------")
# for var_name,  var in model.variables.items():
#     print(var_name, "=", var.primal)


# Installation
# | Install optlang using pip:

# pip install optlang
