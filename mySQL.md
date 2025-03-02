mySQL 
데이터베이스 관리 시스템(RDBMS) 
ohhalim@MacBookAir baekjoonhub % brew install mysql

ohhalim@MacBookAir baekjoonhub % brew services start mysql

==> Successfully started `mysql` (label: homebrew.mxcl.mysql)
ohhalim@MacBookAir baekjoonhub % mysql -u root -p

Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 9.2.0 Homebrew

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY '새로운비밀번호';
Query OK, 0 rows affected (0.01 sec)

mysql> 
mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected, 1 warning (0.01 sec)

mysql> CREATE DATABASE 내_데이터베이스;
Query OK, 1 row affected (0.00 sec)

mysql> USE 내_데이터베이스;
Database changed
mysql> CREATE TABLE 테스트테이블 (
    ->   id INT AUTO_INCREMENT PRIMARY KEY,
    ->   이름 VARCHAR(100),
    ->   생성일 DATETIME DEFAULT CURRENT_TIMESTAMP
    -> );INSERT INTO 테스트테이블 (이름) VALUES ('테스트데이터');
Query OK, 0 rows affected (0.01 sec)

Query OK, 1 row affected (0.01 sec)

mysql> 
mysql> SELECT * FROM 테스트테이블;
+----+--------------------+---------------------+
| id | 이름               | 생성일              |
+----+--------------------+---------------------+
|  1 | 테스트데이터       | 2025-02-28 22:20:47 |
+----+--------------------+---------------------+
1 row in set (0.00 sec)

mysql> 
mysql> 
mysql> 




쿼리 
데이터베이스에 요청을 하는 질의를 쿼리라고 한다, SQL 문법을 이용하여 DB에 명령을 내리는 것을 Query


각 열(줄)을 ‘컬럼’ 혹은 ‘필드’ 라고 부릅니다. 
(앞으로 강의에서는 ‘컬럼’ 이라고 명명) 

select #  어떤 열(column)을 가져올지 지정. 전체 column지정할떄 select * 
from # 데이터를 가져올 테이블을 지정
where # 필터링하는 조건을 지정. 비교연산자 =, <>, >, <, >=, <= 와 논리연산자 사용가능 AND(그리고), OR(또는 ~거나), NOT(아닌)
'''
| 비교연산자 | 의미 | 예시 |
| --- | --- | --- |
| = | 같다 | age=21
gender=’female’ |
| <> | 같지 않다 (다르다) | age<>21
gender<>’female’ |
| > | 크다 | age>21 |
| >= | 크거나 같다 | age>=21 |
| < | 작다 | age<21 |
| <= | 작거나 같다 | age<=21 |
'''

- BETWEEN : A 와 B 사이
- 기본 문법 : **between** a **and** b
- 예시 : 나이가 10 과 20 사이

- IN : ‘포함’ 하는 조건 주기
    - 기본 문법 : **in** (A, B, C)
    - 예시1 : 나이가 15, 21, 31 세인 경우

- LIKE : 완전히 똑같지는 않지만, 비슷한 값을 조건으로 주기
    - 특정한 문자로 시작하는 경우
        - 기본 문법 : **like** ‘시작문자**%**’
        - 예시 : ‘김’ 으로 시작하는 이름


select
from
where
group by
order by
replace #특정 문자를 다른 것으로 바꿀 수 있는 기능
replace(바꿀 컬럼, 현재 값, 바꿀 값)
ex)
select restaurant_name "원래 상점명",
       replace(restaurant_name, 'Blue', 'Pink') "바뀐 상점명"
from food_orders
where restaurant_name like '%Blue Ribbon%'