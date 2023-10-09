while True:
    h1, m1, h2, m2 = map(int, input().split())
 
    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break
 
    current_time = h1 * 60 + m1
    alarm_time = h2 * 60 + m2
 
    if alarm_time <= current_time:
        alarm_time += 24 * 60
 
    sleep_time = alarm_time - current_time
    print(sleep_time)
