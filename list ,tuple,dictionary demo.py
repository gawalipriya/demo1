values = [1,"SAP", 9.4]

print(values[0])    #print perticular index
print(values)       #print whole list

values.insert(2,"bap")   #insertion to th list
print (values)

values.append("piya")     #append
print(values)

del values[0]              #deletion
print(values)

values[3]="PIYA"           #updation
print (values)

print(values[0:2])          #sublist printing


# tuple: same as list only difference is that its an immutable(can not update) once we declared.

val= (1, 9.7, "piya'")
print (val[1])


# Dictionary : its an unordered sewuence of key valur pair form.

val={1:2, 2:"sap", 3:9.8, "m":"pyiya gandhi" }
print(val[1])
print(val[3])
print(val)

#dynamically create dictionary(Build dictionary by adding nwe key:value paires

val= { }

val["FNAME"]="PIYA"
val["LNAME"]="PANDE"
val["add"]="pune"
print(val["LNAME"])
print(val)

