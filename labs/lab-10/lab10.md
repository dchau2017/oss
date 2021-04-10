# Lab 10 - Databases

## Check 0
[Blog Link](https://rcos.io/projects/justinchen673/royal-flush/blog)

## Check 1
![Mongod](./check1.png?raw=true)


## Check 2
![Mongo Import](./check2.png?raw=true)


## Check 3

db.definitions.find(): Returns all entries in the database (in this case definitions)

db.definitions.findOne(): Returns 1 (the first entry) in the databasedb.definitions.findOne()

db.definitions.find({word: "Capitaland"}) : Returns corresponding mongo object with word = Capitalland

db.definitions.find({_id: ObjectId("56fe9e22bad6b23cde07b92f")}) : Returns corresponding mongo object with Object ID = 56fe9e22bad6b23cde07b92f

db.definitions.insert({word: "wack", definition: "a new way to say stupid"})


db.definitions.update({ word: "Ack" }, { "definition" : "a way to express disgust", word : "Ack"})

}
Inserted word
![Query Find](./check3_1.png?raw=true)


Updated word
![Update word](./check3_2.png?raw=true)


Git Diff
![Git Diff](./check3.png?raw=true)


## Check 4

Fetch All Records
![All Records](./check4_1.png?raw=true)


Other Results
![Other](./check4_2.png?raw=true)


[Check 4 Code](https://github.com/dchau2017/oss/blob/master/labs/lab-10/checkpoint4.py)


## Check 5

Multiple Dates Added
![Check5](./check5.png?raw=true)


[Check 5 Code](https://github.com/dchau2017/oss/blob/master/labs/lab-10/checkpoint5.py)