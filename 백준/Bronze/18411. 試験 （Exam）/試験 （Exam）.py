"""
문제

JOI 군은 정보 시험을 3번 봤습니다. 시험 점수는 전부 0 이상 100 이하의 정수입니다.

JOI 군의 성적은 3회 시험 점수 중 가장 높은 두 개를 합한 값입니다.

3회의 시험 점수 A, B, C가 주어질 때, 3회 시험의 점수 중 높은 두 개를 더한 합계를 출력하는 프로그램을 작성합시다.

입력

이하와 같이 표준 입력이 주어집니다. 

A B C

출력

3회 시험 점수 중 높은 2개를 더한 값을 한 줄에 출력합니다.

"""
import sys

score_list = list(map(int,sys.stdin.readline().split()))


score_list.sort()

print(score_list[1]+score_list[2])