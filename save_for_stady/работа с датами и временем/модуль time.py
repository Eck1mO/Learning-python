# c помощью этого модуля можно останавливать выполнение кода на определенное время
# либо замерять сколько времени заняла та или иная операция
import time

print(time.ctime())  # текущее время

print(time.ctime())

# sleep остановка программы (полезно когда нужно подключится к базе данных через какое то время)
start_time = time.time()
print(start_time)
# программа остановится и не будет выполнять операции в секундах
time.sleep(2.5)
end_time = time.time()
print(end_time)
print(end_time - start_time)


# замер времени выполнения задачи
start_time = time.time()

my_list = list(range(10000))
print(my_list[1000])

end_time = time.time()

print("Total duration of the operation: ", end_time - start_time)
