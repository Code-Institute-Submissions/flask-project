import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from wtforms.validators import (DataRequired, Email,EqualTo,Length,URL)
from wtforms import Form, BooleanField, StringField, PasswordField, validators

from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__,static_url_path='/static')
#mongodb atlas connection below
app.config["MONGO_URI"] = "mongodb://AnthonyKeogh:45hungryhill@cookbookfask-shard-00-00-t3cez.mongodb.net:27017,cookbookfask-shard-00-01-t3cez.mongodb.net:27017,cookbookfask-shard-00-02-t3cez.mongodb.net:27017/test?ssl=true&replicaSet=CookbookFask-shard-0&authSource=admin&retryWrites=true&w=majority"
app.config['MONGO_DBNAME'] = 'CookbookFask'
#app.secret_key = 'super secret key'
mongo = PyMongo(app)

# ----------------- Routes to Pages ------------------ #
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipe')
def recipe():
    recipe = mongo.db.testingthecollection.recipe.find_one()  #find items inside the atlas database from the collection
   
    return render_template("recipe.html", recipe = recipe, mimetype='image/jpeg')

@app.route('/starter')
def starter():
    return render_template("starter.html")

@app.route('/recipes')
def recipes():
    recipe = mongo.db.testingthecollection.recipe.find_one()
    
    return render_template("recipes.html", recipe = recipe )

@app.route('/main_course')
def main_course():
    return render_template("main_course.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/dessert')
def dessert():
    return render_template("dessert.html")





# ---------------------------------------------------------------------------------------------------- #







# ----------------- Add Recipe Data ------------------ #



@app.route('/add_recipe')
def add_recipe():
    recipe_Add = mongo.db.testingthecollection.recipe.find()  #gaining access to mongodb atlas database and able to find items inside the collection
    return render_template("add_recipe.html",  recipe_Add=recipe_Add)

@app.route('/adding_recipes/', methods=['GET', 'POST'])
def adding_recipes():
    recipe_add_var = mongo.db.testingthecollection.recipe  #gaining access to mongodb atlas database and able to find items inside the collection
    recipe_add_var.insert_one({
     
                        'Recipe_Description': request.form.get('Recipe_Description'), #asking user to fill out this form field
                        'Preparation_time': request.form.get('Preparation_time'),
                        'Cooking_Time': request.form.get('Cooking_Time'),
                        'Recipe_Name': request.form.get('Recipe_Name'),
                        'Servings': request.form.get('Servings'),
                        'Course_Name': request.form.get('Course_Name'),
                        'Cuisine_Name': request.form.get('Cuisine_Name'),
                        'Allergen_Name': request.form.get('Allergen_Name'),
                        'Step_Number': request.form.get('Step_Number'),
                        'Step_Description': request.form.get('Step_Description'),
                        'Quantity': request.form.get('Quantity'),
                        'Ingredient_name': request.form.get('Ingredient_name'),
                        'Measurement_Name': request.form.get('Measurement_Name'),
                        'Food_Category_Name': request.form.get('Food_Category_Name'),
                        'Country': request.form.get('Country'),
                        'Author_Name': request.form.get('Author_Name'),
                        'Dietary_Name': request.form.get('Dietary_Name'),
                        "img_upload": request.form.get('img_upload'),
   })
    
    return redirect(url_for('recipes'))

# ----------------- Edit Recipe Data ------------------ #

@app.route('/edit_recipe/<recipe_id>')
def editOne(recipe_id):
    editRecipe = mongo.db.testingthecollection.find_one( {"_id": ObjectId("recipe")}) #gaining access to mongodb atlas database and able to find id of the collection
    return render_template('edit_recipe.html', editRecipe=editRecipe)

@app.route('/update_recipe/<recipe_id>', methods=['GET', 'POST'])
def updateOne(recipe_id):
   updateRecipe = mongo.db.testingthecollection #gaining access to mongodb atlas database and able to find items inside the collection
   updateRecipe.update({"_id": ObjectId("recipe")},
       				 {
       					'Recipe_Description': request.form.get('Recipe_Description'), #asking user to fill out this form field
                        'Preparation_time': request.form.get('Preparation_time'),
                        'Cooking_Time': request.form.get('Cooking_Time'),
                        'Recipe_Name': request.form.get('Recipe_Name'),
                        'Servings': request.form.get('Servings'),
                        'Course_Name': request.form.get('Course_Name'),
                        'Cuisine_Name': request.form.get('Cuisine_Name'),
                        'Allergen_Name': request.form.get('Allergen_Name'),
                        'Step_Number': request.form.get('Step_Number'),
                        'Step_Description': request.form.get('Step_Description'),
                        'Quantity': request.form.get('Quantity'),
                        'Ingredient_name': request.form.get('Ingredient_name'),
                        'Measurement_Name': request.form.get('Measurement_Name'),
                        'Food_Category_Name': request.form.get('Food_Category_Name'),
                        'Country': request.form.get('Country'),
                        'Author_Name': request.form.get('Author_Name'),
                        'Dietary_Name': request.form.get('Dietary_Name'),
                        "img_upload": request.form.get('img_upload'),
                        
                   },)
   return redirect(url_for('edit_recipe', updateRecipe=updateRecipe))

# ----------------- Remove Recipe Data ------------------ #
@app.route('/delete_recipe/<recipe_id>')
def deleteOne(recipe_id):
   mongo.db.testingthecollection.remove({"_id": ObjectId("recipe")})  #gaining access to mongodb atlas database and able to find id of the collection

@app.route('/delete_all')
def deleteAll():
   mongo.db.testingthecollection.remove()






# ----------------------------------------------------------------------------------------------- #











# ----------------- Add User Data  and login ------------------ #


        
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST': 
       
        useremail = request.form['useremail'] #asking user to fill out this form field
        username_profile = request.form['username_profile']
        userpassword = request.form['userpassword']
        userprofile = {'username_profile': username_profile, 'useremail': useremail, 'userpassword': userpassword}
        
        
        if mongo.db.testingthecollection.user.find_one({"useremail": useremail}): #checking mongodb for matching email
            return 'Sorry, this password has already been taken by someone else'
        else:
            mongo.db.testingthecollection.user.insert_one(userprofile)
        session['username_profile'] = request.form['username_profile'] #sessions are important because of tracking a user
        return render_template('index.html', userprofile=userprofile, userpassword=userpassword)
    return render_template("auth/registration.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        
        userpassword = request.form['userpassword'] #asking user to fill out this form field
        useremail = request.form["useremail"]
        username_profile = request.form["username_profile"]

        userprofile = mongo.db.testingthecollection.user.find({"username_profile": username_profile})
        userEmail = mongo.db.testingthecollection.user.find({"useremail": useremail})
        if userprofile and userEmail and mongo.db.testingthecollection.user.find({"userpassword": userpassword}):
        
            session["user"] = request.form.get("username_profile")
            return render_template('add_recipe.html', username_profile=session["user"])
        else:
            return 'sorry wrong password or email'
    return render_template('auth/login.html')



if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)