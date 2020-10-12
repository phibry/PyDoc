try:
    # f = open('testfile', 'w')
    f = open('testfile', 'r')
    f.write('Write a test line')
except TypeError:
    print('There was a type error!')
except OSError:
    print('Hey you have an OS Error')
except Exception:
    print('All other exceptions!')
finally:
    print('I always run')
    f.close()
    print(f.closed)


def ask_of_int():
    while True:
        try:
            result = int(input('Please provide number: '))
        except Exception:
            print('Whoops! That is not a number')
            continue
        else:
            print(f"Yes thank you for your input: {result}")
            break
        # finally:
        #     print('End of try/except/finally')
        #     print('I will always run at the end!')


ask_of_int()
