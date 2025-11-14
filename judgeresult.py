#inputs come in here

test_count=0
test_expect=[]
test_actual=[]
time_taken=[]
memory=[]
error=[]
for i in range(test_count):
    test_expect[i]=0
    test_actual[i]=0
    time_taken[i]=0
    memory[i]=0
    error[i]=0

#inputs done here

#results and processing done here
success=0
for i in range(test_count):
    if test_expect[i]==test_actual[i] and time_taken[i]<2 and memory[i]<256:
        print(f'Testcase {i}: Passed')
        print(f'Expected Outcome: {test_expect[i]}\nActual Outcome: {test_actual[i]}')
        success+=1
    elif test_expect[i]==test_actual[i] and time_taken[i]>=2 and memory[i]<256:
        print(f'Testcase {i}: Time limit exceeded')
        print(f'Expected Outcome: {test_expect[i]}\nActual Outcome: {test_actual[i]}')
        success=-1
        loc=i
        break
    elif test_expect[i]==test_actual[i] and time_taken[i]<2 and memory[i]>=256:
        print(f'Testcase {i}: Memory limit exceeded')
        print(f'Expected Outcome: {test_expect[i]}\nActual Outcome: {test_actual[i]}')
        success=-1
        loc=i
        break
    elif test_expect[i]==test_actual[i] and time_taken[i]>=2 and memory[i]>=256:
        print(f'Testcase {i}: Time limit and Memory limit exceeded')
        print(f'Expected Outcome: {test_expect[i]}\nActual Outcome: {test_actual[i]}')
        success=-1
        loc=i
        break
    elif test_expect[i]!=test_actual[i]:
        print(f'Testcase {i}: Time limit and Memory limit exceeded')
        print(f'Expected Outcome: {test_expect[i]}\nActual Outcome: {test_actual[i]}')
        success=-2
        loc=i
        break
print('\nOverall:',end=' ')
elif success==test_count: print('Accepted')
elif success==-1: print('Limits exceeded')
elif success==-2: print('Output mismatch')