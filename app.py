from flask import Flask, render_template, request, jsonify, json
from optlang import Model, Variable, Constraint, Objective
from formulator_service import INGREDIENT_DB
from formulator_service import INGREDIENT_PRICE
from formulator_service import ANIMAL_FEED_REQUIREMENT_DB

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
        result = request.form
        fields = [k for k in request.form]
        values = [request.form[k] for k in request.form]
        data = dict(zip(fields, values))
        animal_name = data['animal']
        animal_type = data['animal_type']
        weight = data['weight']
        selected_ingredients = {k: v for k, v in data.items() if k != 'animal' and k != 'animal_type' and k != 'weight'}
        ingredient_names = [*selected_ingredients]
        # for k in ingredient_names:
        #     ration = INGREDIENT_DB[k]
        # print(ration)

        # Computation starts here---

    # animal ration(nutrient requirement)
    animal_ration = ANIMAL_FEED_REQUIREMENT_DB[animal_type]

    # Define variables
    # variables = {}
    # variable_object = {}
    # for i in range(1, len(ingredient_names)+1):
    #     variable_object[ingredient_names[i-1]] = 'x'+str(i)
    # for ration in animal_ration:
    #     variables[ration] = {}
    #     for k, v in variable_object.items():
    #         for name in ingredient_names:
    #             var = Variable(v, lb=0)
    #             variables[ration][name] = var
    variables = {}
    
    for ration in animal_ration:
        variables[ration] = {}
        for name in ingredient_names:
            var = Variable("{}".format(name), lb=0)
            variables[ration][name] = var
    print(variables)
    print(len(variables))

    # Get nutrient level of feed ingredients
    # for name in ingredient_names:
    #     for ration in animal_ration:
    #         # if (INGREDIENT_DB[name] != ration):
    #         #     a.append(animal_ration[ration])
    #         # else:
    #         try:
    #             a.append(INGREDIENT_DB[name][ration])
    #         except Exception as e:
    #             print(e)
    # print(a)

    # Define constraints
    constraints = []

    for ration in animal_ration:
        try:
            const = Constraint(
                sum((INGREDIENT_DB[name][ration]/100) * variables[name][ration]
                    if ration in INGREDIENT_DB[name]
                    else animal_ration[ration] * variables[name][ration]
                    for name in ingredient_names 
                ),
                    lb=animal_ration[ration]
            )
            # print(const)
            constraints.append(const)
        except Exception as e:
            print(e)
    # print(len(constraints))
    {{ ingredient_db[selected_ingredients[i]]["Price"] }}
    {% for i in range( 0, lengthOfIngredients): %}


    # for name in ingredient_names:
    #     print(name)
    #     print("-" * 10)
    # for k, v in variable_object.items():
    #     print(v)

    # Objective function
    for ration in animal_ration:
        obj = Objective(
            sum(INGREDIENT_PRICE[name] * variables[name][ration] for name in ingredient_names),
                direction='min'
    )
    # Objective( 58*x1+150*x2+60*x3+15*x4+50*x5+90*x6+700*x7+1300*x8+550*x9)

    # print(obj)
    # Solve
    model = Model()
    model.objective = obj
    model.add(constraints)
    status = model.optimize()
    print("status:", status)
    print("objective value:", model.objective.value)
    print("-------------")
    for var_name , var in model.variables.items():
        print(var_name, "=", var.primal)
    # result = model.objective.value
        
    return render_template("result.html", animal_type = animal_type)


app.run(debug=True)
