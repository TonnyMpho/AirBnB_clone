## 0x00. AirBnB clone - The console

![hbnd logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230814%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230814T125846Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cc8da31b198238fdc584e3ae3996eaf96afd3ad2135516285efca7838defa15d)

### AirBnB clone project!

It's a clone of the AirBnB webapp

#### Command interpreter

Do you know the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

#### What our command interpreter can do:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

##### Execution
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

non-nteractive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```


