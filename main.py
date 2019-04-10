from flask import Flask, render_template, request, jsonify, json
from optlang import Model, Variable, Constraint, Objective
from animal_db import animal_db
from ingredient_db import ingredient_db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('feed_form.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        fields = [k for k in request.form]
        values = [request.form[k] for k in request.form]
        data = dict(zip(fields, values))
        animal_name = data['animal']
        animal_type = data['animal_type']
        weight = data['weight']
        ingredients = {k: v for k, v in data.items() if k != 'animal' and k != 'animal_type' and k != 'weight'}
        selected_ingredients = [*ingredients]
        print(selected_ingredients)

        ################################################
        variable_objects = [] # stores all the contraints for the formulation
        """The feed size is the amount in kilogram (kg) the buyer wants to get from the feed formulator, this should be collected from the client side"""
        feed_size = weight
        animal_selected = animal_name
        #################################
        selected_animal_stage = animal_type

        variable_objects = [] # stores all the contraints for the formulation

        variable_sum  = None
        for i in range( 1 , len(selected_ingredients) + 1 ):
            ing = Variable('x{0}'.format(i), lb=0)
            if i == 1 :
                variable_sum = ing
            elif i > 1 :
                variable_sum += ing
            variable_objects.append(ing)
        print("THE VARIABLE SUM FOR THE CONSTRAINT =>>>>>",variable_sum)

        #the next step is to build the constraints for the formulation
        #we will build the contraints using the value of the ingredients respective nutrients compositions for the the particular animal maximum and minimum nutrient value
        #let's build the first contraint for the formulation

        #but before then, the demand reqirement will be the variable_sum, so all we need to do is to assign the variable_sum to the first contraint
        # contraint_sum = None

        #this should be constants to solve the formulation
        #do not change
        c1 = Constraint(variable_sum,lb = feed_size )
        # c2 = Constraint(variable_sum,ub = feed_size )
        contraints_list = []
        #append the fisrt two constraints into the contraints_list.
        contraints_list.append(c1)
        # contraints_list.append(c2)

        # the temp sum to hold the temporary sum of all the varible for the formulation
        temp_var_sum =None

        # print(animal_db[animal_selected][selected_animal_stage])
        # if the user selects finisher broiler

        #This will return the keys in the finisher's feed contraints
        # This will return the keys in the finisher's feed contraints
        for nutrient in animal_db[animal_selected][selected_animal_stage]:
            """now we will iterate through the returned nutrient compositions for the finisher broiler"""
            for bound in animal_db[animal_selected][selected_animal_stage][nutrient]:
                count = 0
                # print("BOUND=>",bound)

                for ing_name in selected_ingredients:
                    # print("\nIngredient ====>",ing_name,"\n")
                    if count == 0:
                        # print("\n\n--------------Another contraints goes from here-----------------------------")
                        if nutrient != "Energy":
                            temp_var_sum = (ingredient_db[ing_name]["ing"][nutrient] / 100) * variable_objects[count]
                            # print(temp_var_sum,end=" ")
                            count = count + 1
                        else:
                            temp_var_sum = ingredient_db[ing_name]["ing"][nutrient] * variable_objects[count]
                            # print(temp_var_sum,end=" ")
                            count = count + 1

                        # print(count)
                    elif count > 0:
                        # print("\n\n--------------Another contraints goes from here-----------------------------")
                        if nutrient != "Energy":
                            temp_var_sum += (ingredient_db[ing_name]["ing"][nutrient] / 100) * variable_objects[count]
                            # print(temp_var_sum,end=" ")
                            count = count + 1
                        else:
                            temp_var_sum += ingredient_db[ing_name]["ing"][nutrient] * variable_objects[count]
                            # print(temp_var_sum,end=" ")
                            count = count + 1

                ############################Then we build the contraints from here after the sum of the constraints has been generated##############################

                # print("\n\n--------------Another contraints goes from here-----------------------------")
                # print("NUTRIENT ===> ",nutrient)
                # print(temp_var_sum, end=" ")
                # print("BOUND=>",bound, end=" ")
                # print("=",animal_db[animal_selected][selected_animal_stage][nutrient][bound])

                if bound == "Min":
                    contraints_list.append(Constraint(temp_var_sum, lb=
                    animal_db[animal_selected][selected_animal_stage][nutrient][bound]))
                    print(temp_var_sum, ">=", animal_db[animal_selected][selected_animal_stage][nutrient][bound])

                elif bound == "Max":
                    contraints_list.append(Constraint(temp_var_sum, ub=
                    animal_db[animal_selected][selected_animal_stage][nutrient][bound]))
                    print(temp_var_sum, "<=", animal_db[animal_selected][selected_animal_stage][nutrient][bound])

                elif bound == "Equal":
                    contraints_list.append(Constraint(temp_var_sum, lb=
                    animal_db[animal_selected][selected_animal_stage][nutrient][bound]))
                    contraints_list.append(Constraint(temp_var_sum, ub=
                    animal_db[animal_selected][selected_animal_stage][nutrient][bound]))
                    print(temp_var_sum, ">=", animal_db[animal_selected][selected_animal_stage][nutrient][bound])
                    print(temp_var_sum, "<=", animal_db[animal_selected][selected_animal_stage][nutrient][bound])

                # all_const+=temp_var_sum

        ####################################################################################################################################################

        print("\nCONTRAINTS===>",contraints_list,end="\n\n\n")

        #constructing the object function from here
        objective_sum = None
        for i in range( 0 , len(selected_ingredients)):
            if i == 0 :
                objective_sum  = ingredient_db[selected_ingredients[i]]["Price"]*variable_objects[i]
            elif i > 0 :
                objective_sum += ingredient_db[selected_ingredients[i]]["Price"]*variable_objects[i]
            print(objective_sum)
        print("OBJECTIVE FUNCTION ====> ",objective_sum,end="\n\n\n\n")

        obj = Objective(objective_sum,direction='min')
        # Variables, constraints and objectives are combined in a Model object, which can subsequently be optimized.
        model = Model(name='Simple model')
        model.objective = obj
        model.add(contraints_list)
        status = model.optimize()

        print("status:", status)
        print("objective value:", model.objective.value)
        print("---------------------------------------------------------------------")
        variable_quantity = model.variables
        objValue = round(model.objective.value, 2)

        variables = []
        for a, n in variable_quantity.items():
            value = a, round(n.primal, 2)
            variables.append(value)

        price = []
        for i in selected_ingredients:
            value = i, ingredient_db[i]["Price"]
            price.append(value)
        collection = dict(zip(variables, price))
        
    return render_template("result.html",
            collection = collection,
            animal_type = animal_type,
            objValue = objValue
            )


app.run(debug=True)
