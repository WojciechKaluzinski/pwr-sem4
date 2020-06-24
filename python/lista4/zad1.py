#!/usr/bin/python3

from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrap_time(*args, **kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.time() - start
            print(f"Czas wykonywania funkcji to: {end if end > 0 else 0} s")
    return wrap_time

@timer
def addition():
  result = 0
  for i in range(0,1000000):
    result += i
  print("Suma dodawania to: ", result)

if __name__ == "__main__":
	timer(addition())
