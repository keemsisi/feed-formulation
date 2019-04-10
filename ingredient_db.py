#####################################################################################################################################
#----------------------------------------LOAD THE ORIGINAL DATA BELOW IN THE GIVEN PATTERN------------------------------------------#
#####################################################################################################################################
ingredient_db = {
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