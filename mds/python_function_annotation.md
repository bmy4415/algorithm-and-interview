## python function annotation
- 함수에 대하여 다는 주석과 같은 역할, 문법적 역할이나 강제사항, 효력 등은 없음
    - 단, compile time에 어딘가에 저장됨 : **foo.__annotations__**
    - mypy 등 외부 library를 이용하여 type check 가능
- example
    ```
    def foo(a:int, b:'string'='hi') -> 'hello':
        print(a, b)

    foo('ab', 'cd') # 'ab cd'
    foo(1, 2) # '1 2'

    foo.__annotation__ # {'return': 'hello', 'b': 'string', 'a': <class 'int'>}
    ```

## python function annotation - english
- annotation is comment-like expression which has almost None effect on python code
    - however, it will stored somewhere in compile time : you can check by print **function_name.__annotitaions__**
    - you can utilize annotation via using 3rd party library like `mypy`
- example
    ```
    def foo(a:int, b:'string'='hi') -> 'hello':
        print(a, b)

    foo('ab', 'cd') # 'ab cd'
    foo(1, 2) # '1 2'

    foo.__annotation__ # {'return': 'hello', 'b': 'string', 'a': <class 'int'>}
    ```

reference
- https://blog.hannal.com/2015/03/keyword-only-arguments_and_annotations_for_python3/