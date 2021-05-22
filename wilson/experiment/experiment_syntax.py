import datetime

import numpy
import time
from pathlib import Path

import matplotlib.pyplot as plt


from util.common_util import CommonUtil

run_case_idx = 1
max_run_case = 1


# if run_case_idx == max_run_case:    exit()
# else: run_case_idx += 1

if __name__ == '__main__':



    print("start")

    path_name = "wagegw/wabrb.jpeg"
    ext = CommonUtil.obtain_file_extension(path_name)

    print(ext)



    if run_case_idx == max_run_case:    exit();
    else: run_case_idx += 1


    list = [1,2,3,4,5]
    print(list[-2])
    print(list[-2:])


    if run_case_idx == max_run_case:    exit();
    else: run_case_idx += 1


    timer = TimerUtil()
    timer.start_timer()


    for i in range(5):
        CommonUtil.print_on_same_line(i)

        timer.resume_or_start()
        time.sleep(2)
        timer.pause()
        time.sleep(1)


    print("move", len(timer.delta_list), ".   avg: ", timer.avg_time(), timer.avg_time().total_seconds())



    if run_case_idx == max_run_case:    exit();
    else: run_case_idx += 1


    txt = "1, 2"
    txt_list = txt.split(",")

    x = int(txt_list[0].strip())
    y = int(txt_list[1].strip())
    str_tuple = (x, y)


    print(str_tuple)




    if run_case_idx == max_run_case:    exit();
    else: run_case_idx += 1



    timer = TimerUtil()
    timer.start_timer()

    time.sleep(2)
    timer.lap()

    time.sleep(1)
    timer.pause()

    time.sleep(1)
    timer.resume()

    time.sleep(1)
    timer.end()


    print(timer.avg_time())









    if run_case_idx == max_run_case:    exit();
    else: run_case_idx += 1



    start_date_time: datetime = datetime.datetime(2021, 5, 14, 14, 00, 00, 500)
    # time.sleep(2)

    end_date_time: datetime = datetime.datetime(2021, 5, 14, 16, 00, 1, 600)

    diff: datetime.timedelta = end_date_time - start_date_time

    print(diff)



    if run_case_idx == max_run_case:    exit();
    else: run_case_idx += 1


    a = 1
    print(-2 < a < 1)


    if run_case_idx == max_run_case:    exit();
    else: run_case_idx += 1



    data_dict = {}
    data_dict[("a","b")] = [1, 2, 3, 4]

    print(data_dict[("a","b")][-1])






    if run_case_idx == max_run_case:    exit();
    else: run_case_idx += 1



    data = 1
    data_list_list = numpy.array([data])
    print(data_list_list)


    if run_case_idx == max_run_case:    exit();
    else: run_case_idx += 1


    data_list_list = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    tmp = CommonUtil.numpy_list_to_tuple(data_list_list)
    print(tmp)


    if run_case_idx == max_run_case:    exit();
    else: run_case_idx += 1



    data_list_list = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(data_list_list)

    a_data_list = numpy.reshape(data_list_list, 9)
    a_data_list = numpy.append(a_data_list, 10)


    print(a_data_list)



    if run_case_idx == max_run_case:    exit()
    else: run_case_idx += 1




    data_list_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    a_data_list = []
    for data_list in data_list_list:
        a_data_list += data_list

    print(a_data_list)





    for i in range(10):
        CommonUtil.print_on_same_line(i)


    if run_case_idx == max_run_case:    exit()
    else: run_case_idx += 1



    data_list_list = [1, 2, 3, 4, 5]
    print("data_list", data_list_list[::-1])



    if run_case_idx == max_run_case:    exit()
    else: run_case_idx += 1



    print("Path(__file__).stem", Path(__file__).stem)



    if run_case_idx == max_run_case:    exit()
    else: run_case_idx += 1



    initial_epsilon = 1
    decay = 0.8
    episodes_per_drop = 500

    episode_idx = 1

    effective_epsilon_list = []


    for i in range(100000):
        episode_idx += 10
        epi_div_per_drop = episode_idx / episodes_per_drop
        decay_exp_per_drop = decay ** (epi_div_per_drop)
        effective_epsilon = initial_epsilon * decay_exp_per_drop
        effective_epsilon_list.append(effective_epsilon)
        print(epi_div_per_drop, decay_exp_per_drop, effective_epsilon)



        plt.figure(1)
        plt.clf()
        plt.title("test")
        plt.xlabel("exploration rate")
        plt.ylabel("episode")

        plt.plot(effective_epsilon_list)

        plt.pause(0.001)





    print("end")