# Cainthus Challange

# Requirements
- datetime
- re

# How to Execute
- ```python date_diffrence.py```<br/>
- ```python validate_email.py```<br/>

## Task List
- First task : Computing absolute difference in seconds of given time.
- Second task : Validating given email address

# Results
# Task 1 
### First Run Output
```Number of test cases : 1
1 Pair
Enter first date: Sat 30 May 2005 13:54:36 +0700
Enter second date: Sun 30 Aug 1992 10:10:00 +0530
Output: 
402286476
```
### Second Run Output
```
Number of test cases : 2
1 Pair
Enter first date: Sun 10 May 2015 13:54:36 -0700
Enter second date: Sun 10 May 2015 13:54:36 -0000
2 Pair
Enter first date: Sat 02 May 2015 19:54:36 +0530
Enter second date: Fri 01 May 2015 13:54:36 -0000
Output: 
25200
88200
```

# Task 2
### First Run Output
```
Number of email addresses : 2
Enter email 1 : A.lakmale@gma_il.com
Enter email 2 : A.lakmale@gmail.com
Outut: ['A.lakmale@gmail.com']
```
### Second Run Output
```
Number of email addresses : 2
Enter email 1 : incorrect_email@hypen_included@moreThanThreeLetters
Enter email 2 : inc@orrect_email@h_ok@com
Outut: []
```
### Third Run Output
```
Number of email addresses : 4
Enter email 1 : clara@example.com
Enter email 2 : john-doe23@example.com
Enter email 3 : jane_35@example.com
Enter email 4 : joe%bloggs@example.com
Outut: ['clara@example.com', 'jane_35@example.com', 'john-doe23@example.com']
```
