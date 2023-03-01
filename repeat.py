def f(*args):
    return list(
                map(
                    lambda s: sum(
                                  map(
                                      int,
                                      list(str(s))
                                  )
                    ),
                    args)
    )


print(f(10, 20, 30))
# слова 471711
# строки 32379
# слова из трех букв 43147