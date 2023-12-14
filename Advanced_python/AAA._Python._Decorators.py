import sys
import datetime


sys.stdout.write('Hello, my friend!\n')
# Это метод объектов file-like классов, то есть классов,
# которые реализуют семантику "Меня можно создать,
# из меня можно прочитать и в меня можно записать".

# Самый главный пример такого объекта -- объект `file`,
# являющийся результатом вызова фукнции `open()`.
# Для простоты и универсальности взаимодействия,
# стандартный ввод и стандартный вывод тоже являются файлами,
# из которых можно читать и в которые можно писать.

output = open("./some_test_data.txt", 'w')

output.write('123')

output.close()

# Как вы могли заметить, функция возвращает число записанных байт.
# Это важная часть контракта, которую нужно поддержать,
# если вы хотите как-то подменять эту функцию.

# Задача 1

# Для начала, давайте подменим метод `write` у объекта
# `sys.stdin` на такую функцию, которая перед каждым вызовом оригинальной
# функции записи данных в `stdout` допечатывает к тексту текущую метку времени.


original_write = sys.stdout.write


def my_write(string_text: str) -> None:
    """
    Writes the given string with a timestamp to the standard output.

    Args:
        string_text (str): The text to be written.

    Returns:
        None
    """
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]: ")
    if string_text.strip():
        original_write(timestamp + string_text + "\n")
    else:
        pass


sys.stdout.write = my_write


print('1, 2, 3')

sys.stdout.write = original_write


# Вывод должен был бы быть примерно таким:

# ```
# [2021-12-05 12:00:00]: 1, 2, 3
# ```

# Задача 2

# Упакуйте только что написанный код в декторатор.
# Весь вывод фукнции должен быть помечен временными метками.


def timed_output(func):
    """
    Decorator that adds a timestamp to the standard output
    for the decorated function.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """
    original_write = sys.stdout.write

    def my_write(string_text: str) -> None:
        """
        Writes the given string with a timestamp to the standard output.

        Args:
            string_text (str): The text to be written.

        Returns:
            None
        """
        timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]: ")
        if string_text.strip():
            original_write(timestamp + string_text + "\n")
        else:
            pass

    sys.stdout.write = my_write

    def wrapper(*args, **kwargs):
        """
        Wrapper function that restores the original standard output
        and returns the result of the decorated function.

        Args:
            *args: Variable positional arguments passed
            to the decorated function.
            **kwargs: Variable keyword arguments passed
            to the decorated function.

        Returns:
            Any: The result of the decorated function.
        """
        result = func(*args, **kwargs)
        sys.stdout.write = original_write
        return result

    return wrapper


@timed_output
def print_greeting(name: str) -> None:
    print(f'Hello, {name}!')


print_greeting("Nikita")


# Вывод должен быть похож на следующий:

# ```
# [2021-12-05 12:00:00]: Hello, Nikita!
# ```


# Задача 3

# Напишите декторатор, который будет перенаправлять вывод фукнции в файл.
# Подсказка: вы можете заменить объект sys.stdout каким-нибудь другим объектом.


def redirect_output(filepath: str):
    """
    Decorator that redirects the standard output
    to a file for the decorated function.

    Args:
        filepath (str): The path to the file where
        the output will be redirected.

    Returns:
        callable: The decorated function.
    """
    class FileWrapper:
        def __init__(self, file, original_write):
            self.file = file
            self.original_write = original_write

        def write(self, string_text: str) -> None:
            """
            Writes the given string to both the original output and a file.

            Args:
                string_text (str): The text to be written.

            Returns:
                None
            """
            self.original_write(string_text)
            self.file.write(string_text)

    def decorator(func: callable) -> callable:
        """
        Decorator that redirects the standard output
        to a file for the decorated function.

        Args:
            func (callable): The function to be decorated.

        Returns:
            callable: The decorated function.
        """
        def wrapper(*args, **kwargs):
            """
            Wrapper function that redirects the standard output
            to a file and calls the decorated function.

            Args:
                *args: Variable positional arguments passed
                to the decorated function.
                **kwargs: Variable keyword arguments passed
                to the decorated function.

            Returns:
                Any: The result of the decorated function.
            """
            with open(filepath, 'w') as output_file:
                file_wrapper = FileWrapper(output_file, sys.stdout.write)
                sys.stdout.write = file_wrapper.write
                result = func(*args, **kwargs)
                sys.stdout.write = file_wrapper.original_write
                return result

        return wrapper

    return decorator


@redirect_output('./function_output.txt')
def calculate() -> None:
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


calculate()
