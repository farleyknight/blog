# Clojure Functions

Being a Lisp-based language, Clojure is naturally functional.

Map a function over a vector
```clojure
(map inc [1 2 3]) ; => (2 3 4)
```

Given a function, reduce a vector.
```clojure
(reduce + [1 2 3 4]) ; => 10 = 1 + 2 + 3 + 4
```

Anonymous functions.
```clojure
(fn [] "Hello World")
```

Bind the function to a name.
```clojure
(def hello (fn [] "Hello World"))
(defn hello [] "Hello World") ;; The shorthand!
```

As you would expect, the argument is provided in square brackets.
```clojure
(defn hello [name]
  (str "Hello " name))
(hello " Farley") ; => "Hello Farley"
```

