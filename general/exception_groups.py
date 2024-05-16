def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )
try:
    f()
except* OSError as e:
    print("OS Erros")
except* SystemError as e:
    print("System Error")
