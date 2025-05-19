import sys


speed_limit = int(sys.stdin.readline().strip())
speed = int(sys.stdin.readline().strip())


delta_result = speed - speed_limit
fine = 0

if 1 <= delta_result <= 20:
    fine = 100

elif 21<= delta_result <30:
    fine = 270

elif delta_result >30:
    fine = 500


if fine !=0:
    print(f'You are speeding and your fine is ${fine}.')

else:
    print('Congratulations, you are within the speed limit!')