## python function argument and \*(asterisk)
- python function의 argument는 `positional argument`와 `keyword argument`가 있음
- positional argument는 argument의 위치에 따라 값을 넘겨받음
- keyword argument는 argument의 keyword에 의해 값이 정해짐
- example
    ```
    def foo(arg1, arg2, arg3=None, arg4='hi'):
        print(arg1, arg2, arg3, arg4)

    foo('a', 'b', 'c', 'd') # correct
    foo('a', 'b', arg3='c', arg4='d') # correct
    foo('a', arg3='c', arg4='d', arg2='b') # correct
    foo('a', arg3='c', arg4='d') # error
    ```
- positional argument는 생략이 불가능하고 정해진 위치에 넣어야함, 단 위의 3번째 예시처럼 positional argument를 keyword argument 방식처럼 (즉 arg2를 생략하지 않았음) call은 가능함
- keyword argument는 function call을 할 때 생략이 가능하고, default 값을 설정할 수 있으며, 생략할 경우 default 값이 들어감
- keyword argument가 function call 시에 생략이 가능하므로 function definition에서 positional argument보다 먼저 등장할 수 있음, 즉 다음의 예시는 error임
    - example
    ```
    def foo(arg1, arg2='hi', arg3):
        print(arg1, arg2, arg3)
    ```
- keyword argument의 경우 function definition에 있는 argument의 순서를 잘 맞추면 keyword 없이도 function call을 할 수 있음
    - example
    ```
    def foo(arg1, arg2, arg3='hello'):
        print(arg1, arg2, arg3)

    foo('my', 'name', 'tom') #  print 'my name tom'
    foo('my', 'name') # print 'my name hello'
    ```
- \*은 keyword인자의 강제 / 가변인자(variadic argument)에 사용할 수 있음
- bare \*는 \*이후의 인자에 keyword argument를 강제함
- example
    ```
    def foo(arg1, *, arg2, arg3):
        print(arg1, arg2, arg3)

    foo('my', 'name', 'a') # error
    foo('my', arg2='name', arg3='c') # print 'my name c'
    foo('my', arg3='name', arg2='c') # print 'my c name'
    ```
- \*args, \*\*kwargs의 경우 variadic argument를 받음
    - \*을 1개 사용하는 \*args는 variadic positional argument, \*을 2개 사용하는 \*\*kwargs는 variadic keyword argument를 받음
    - 즉 \*args가 아니라 \*required, \*\*kwargs가 아니라 \*\*optional 등으로 사용 가능, 그러나 (\*args, \*\*kwargs)가 convention임
    - 단, 앞의 예시에서 positional argument를 keyword argument처럼 call 했던것과 달리 반드시 positional argument를 앞에, keyword argument를 뒤에 두고 call 해야함
    - example
    ```
    def foo(*args, **kwargs):
        print(args, kwargs)

    foo('a', 'b', name='c', 15) # error
    foo('a', 'b', name='jw', age=15) # ('a', 'b') {'age': 15, 'name': 'jw'}
    ```

## python function argument and \*(asterisk) - english
- there are 2 argument types in python : `positional argument`, `keyword argument`
    - `positional argument` gets its value depending on order of argument
    - `keyword argument` gets its value depending on keyword(name)
        - you can set default value for keyword argument and you can omit keyword argument which, in that case, will have default value you set
- example
    ```
    def foo(arg1, arg2, arg3=None, arg4='hi'):
        print(arg1, arg2, arg3, arg4)

    foo('a', 'b', 'c', 'd') # correct
    foo('a', 'b', arg3='c', arg4='d') # correct
    foo('a', arg3='c', arg4='d', arg2='b') # correct
    foo('a', arg3='c', arg4='d') # error
    ```
- you cannot omit any positional argument or you will get error, but like `foo('a', arg3='c', arg4='d', arg2='b') # correct` on above example, you can use keyword argument when you call funciton to replace positional argument
- because you can omit keyword argument when you call function, **keyword argument cannot not precede positional argument in function definition**. So the next example is error
    - example
    ```
    def foo(arg1, arg2='hi', arg3):
        print(arg1, arg2, arg3)
    ```
- when you use keyword argument, if you omit keyword and only use value, it will do like positional argument
    - example
    ```
    def foo(arg1, arg2, arg3='hello'):
        print(arg1, arg2, arg3)

    foo('my', 'name', 'tom') #  print 'my name tom'
    foo('my', 'name') # print 'my name hello'
    ```
- \*(asterisk) has 2 functionality
    - enforce keyword argument
        - bare \* will enforce keyword argument after \*
        - example
        ```
        def foo(arg1, *, arg2, arg3):
            print(arg1, arg2, arg3)

        foo('my', 'name', 'a') # error
        foo('my', arg2='name', arg3='c') # print 'my name c'
        foo('my', arg3='name', arg2='c') # print 'my c name'
        ```
    - variadic argument
        - single \* will get positional argument as **tuple**
        - double \* will get keyword argument as **dict**
        - also you can use another variable name (\*args, \*\*kwargs) => (\*what, \*\*ever) but (\*args, \*\*kwargs) is convention and you also have to keep this order when you define function and when you call function
            - example
            ```
            def foo(*args, **kwargs):
                print(args, kwargs)

            foo('a', 'b', name='c', 15) # error
            foo('a', 'b', name='jw', age=15) # ('a', 'b') {'age': 15, 'name': 'jw'}
            ```

reference
- https://stackoverflow.com/questions/14301967/bare-asterisk-in-function-arguments
- https://mingrammer.com/understanding-the-asterisk-of-python/
- https://blog.hannal.com/2015/03/keyword-only-arguments_and_annotations_for_python3/