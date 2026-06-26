#List

environments = ["dev","prod","stg","test"]
print(environments[0])
print(environments[3])

print(len(environments))


environments.append("bastion")

#to know what can we do with commanf
print(dir(environments))

# to see how to use command
print(environments.insert.__doc__)
environments.insert(1, "qa")


#dictonary

device_info = {
    "name" : "Apple Mac book pro",
    "RAM"  : "26 gb",
    "cpu"  : 8,
    "isNew" : False
}

print(device_info.get("cpu"))
#or
print(device_info["cpu"])

#adding new key
device_info.update({"environments":environments})
print(device_info)


#sets
device_ids = {1,2,3,4,2,4,5,6,7,8,5,9,10}
new_device_ids = {11,12,13}
print(device_ids.union(new_device_ids))