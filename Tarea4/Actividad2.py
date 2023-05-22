dictionary1= {"perro":"dog", "gato":"cat", "vaca":"cow", "caballo":"horse", "tiburon":"shark"}
dictionary2= {"dog":"perro", "cat":"gato", "cow":"vaca", "horse":"caballo", "shark":"tiburon"}
dictionary1["cisne"]="swan"
dictionary1.update({"pato": "duck"})
dictionary2["swan"]="cisne"
dictionary2.update({"duck": "pato"})

print(dictionary1)
print(dictionary2)