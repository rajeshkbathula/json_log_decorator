# json-log-decorator
python log decorator with info and exception, captures time taken by function or method and stdout in json format

To install package 
```
pip install json-log-decorator
```

* Example usage with just decorator
> NOTE: this takes file name as name while logging
```python
from json_log_decorator.logdecorator import LogDecorator as log
import time

@log()
def test_decorator(x,y):
    time.sleep(2)
    return x + y

test_decorator(1,2)
```
> Above one gives below log

```json
{"name": "test", "levelname": "INFO", "asctime": "2021-06-22 23:32:18,564", "message": "Function Called:[test_decorator]"}
{"name": "test", "levelname": "INFO", "asctime": "2021-06-22 23:32:20,568", "message": "Function Ended:[test_decorator] timetaken:[2] Seconds"}```
```

* Incase of exception, it logs with error and raises the exception

```python
from json_log_decorator.logdecorator import LogDecorator as log
import time

@log()
def test_decorator(x,y):
    time.sleep(2)
    return x + y

test_decorator(1,'s')
```
> Above one gives below log 

```json
{"name": "test", "levelname": "INFO", "asctime": "2021-06-22 23:29:01,097", "message": "Function Called:[test_decorator]"}
{"name": "test", "levelname": "ERROR", "asctime": "2021-06-22 23:29:03,100", "message": "Exception in test_decorator", "exc_info": "Traceback (most recent call last):\n  File \"/json-log-decorator/json_log_decorator/logdecorator.py\", line 17, in wrapper\n    val = func(*args, **kwargs)\n  File \"/json-log-decorator/json_log_decorator/test.py\", line 7, in test_decorator\n    return x + y\nTypeError: unsupported operand type(s) for +: 'int' and 'str'"}
```

* To give a name to logger and for using decorator and you can add loggin messages if required

```python
from json_log_decorator.logdecorator import LogDecorator,get_logger

logger = get_logger('test-this')
log = LogDecorator(logger)

@log
def test_decorator(x,y):
    logger.warning('to hava a warning message')
    return x + y

@log
def sum(x):
    return x+2

@log
def main():
    x = sum(test_decorator(2,3))
    logger.info(x)

main()
```

* To set logging Level 

```python
import logging
from json_log_decorator.logdecorator import LogDecorator,get_logger

logger = get_logger('test-debug')
logger.setLevel(logging.DEBUG)
log = LogDecorator(logger)

@log
def test_decorator(x,y):
    logger.warning('just a warning test message')
    return x + y

@log
def sum(x):
    return x+2

@log
def main():
    x = sum(test_decorator(2,3))
    logger.info(x)

main()
```