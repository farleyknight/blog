# Clojure Lists & Vectors

You can check the class of anything in Clojure with the function `class` (which would probably be more readable as `class-of`).
```clojure
(class [1 2 3]); => clojure.lang.PersistentVector
(class '(1 2 3)); => clojure.lang.PersistentList
```

## Question: Which is more useful, vectors or lists?

As it turns out, [vectors are](http://stackoverflow.com/questions/1147975/in-clojure-when-should-i-use-a-vector-over-a-list-and-the-other-way-around). Note that rhickey = Rich Hickey = creator of Clojure:

```
[12:22] <Raynes>	When would you want to use a list over a vector?
[12:22] <rhickey>	when generating code, when generating back-to-front
[12:23] <rhickey>	not too often in Clojure
```

So lists are mostly for doing heterogeneous linked-lists, such as in metaprogramming, whereas vectors are used for generating something closer to a C/C++/Java array.

## Manipulating vectors

Getting elements from a vector. 
```clojure
(get [3 2 1] 0) ; => 3
```

Appending to vectors.
```clojure
(cons 4 [1 2 3]) ; => (4 1 2 3)
```

Concatenating lists.
```clojure
(concat [1 2] [3 4]) ; => (1 2 3 4)
```
