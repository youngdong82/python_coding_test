'use strict';
// -------------------------------------------------------------------------------- 푼 문제
// 문자열 내 p와 y의 개수
// x만큼 간격이 있는 n개의 숫자
// 핸드폰 번호 가리기
// 콜라츠 추측
// 짝수와 홀수
// -----
// 제일 작은 수 제거하기
// 자연수 뒤집어 배열로 만들기
// 정수 내림차순으로 배치하기
// 하샤드 수
// 이상한 문자 만들기
// -----
// 평균 구하기
// 자릿수 더하기
// 최대공약수와 최소공배수
// 정수 제곱근 판별
// 수박수박수박수박수박수?
// -----
// 문자열 내림차순으로 배치하기
// 문자열 내 마음대로 정렬하기
// 서울에서 김서방 찾기
// 없는 숫자 더하기
// 부족한 금액 계산하기

// -------------------------------------------------------------------------------- API
// --------------------------------------------- unshift()
// --------------------------------------------- shift()
// --------------------------------------------- reduce()
// Array.reduce(함수)
// -------------------------------------------------------------------------------- 1. 평균 구하기
// ------------------------------------------- 내꺼
// function solution(arr) {
//   let sum = 0
//   for(let i in arr){
//     sum += arr[i]
//   }
//   return sum/arr.length
// }

// console.log(solution([1,2,3,4]))
// console.log(solution([5,5]))
// -------------------------------------------------------------------------------- 2. 자릿수 더하기
// ------------------------------------------- 내꺼
// function solution(n){
//   const stringN = n.toString();
//   let sum = 0;
//   for(let i in stringN){
//     sum += parseInt(stringN[i]);
//   }
//   return sum
// }

// console.log(solution(123));
// console.log(solution(987));

// -------------------------------------------------------------------------------- 3. 최대공약수와 최소공배수
// ------------------------------------------- 내꺼
// function solution(n, m) {
//   let gcd = 1;
//   for(let i = 2; i <= Math.min(n,m); i++){
//     if (n%i === 0 && m % i === 0){
//       gcd = i;
//     }
//   }
//   const lcm = (n*m)/gcd;

//   return [gcd,lcm];
// }

// console.log(solution(3,12));
// console.log(solution(2,5));
// console.log(solution(12,24));

// -------------------------------------------------------------------------------- 4. 정수 제곱근 판별
// ------------------------------------------- 내꺼
// function solution(n){
//   var root = Math.sqrt(n);
//   if((parseInt(root) - root) === 0){
//     return (root + 1 ) **2;
//   } else{
//     return -1;
//   }
// }

// console.log(solution(1))
// console.log(solution(121))
// console.log(solution(3))
// console.log(solution(16))

// -------------------------------------------------------------------------------- 5. 수박수박수박수박수박수?
// ------------------------------------------- 내꺼
// function solution(n) {
//   let answer = '';
//   for(let i = 1; i <= n; i++){
//     if (i%2 == 1){
//       answer += '수';
//     } else{
//       answer += '박';
//     }
//   }
//   return answer
// };

// console.log(solution(3));
// console.log(solution(4));

// -------------------------------------------------------------------------------- 6. 문자열 내림차순으로 배치하기
// ------------------------------------------- 내꺼
// function solution(s) {
//   const splitedS = s.split('');
//   const sortedS = splitedS.sort().reverse();
//   return sortedS.join('');
// };

// console.log(solution("Zbcdefg"));

// -------------------------------------------------------------------------------- 7. 문자열 내 마음대로 정렬하기
// ------------------------------------------- 내꺼
// function solution(strings, n) {
//   for(let i=0; i<strings.length; i++){
//     strings[i] = strings[i].split("");
//     strings[i].unshift(strings[i].splice(n,1).join(""));
//     strings[i] = strings[i].join('');
//   }
//   strings.sort();
//   for(let j=0; j<strings.length; j++){
//     strings[j] = strings[j].split("");
//     strings[j].splice(n,0,strings[j].shift());
//     strings[j] = strings[j].join('');
//   }

//   return strings;
// };

// console.log(solution(["sun", "bed", "car"],1))
// console.log(solution(["abce", "abcd", "cdx"],2))

// -------------------------------------------------------------------------------- 8. 서울에서 김서방 찾기
// ------------------------------------------- 내꺼
// function solution(seoul) {
//   const i = seoul.indexOf('Kim');
//   return `김서방은 ${i}에 있다.`
// };

// console.log(solution(["Jane", "Kim"]))

// -------------------------------------------------------------------------------- 9. 없는 숫자 더하기
// ------------------------------------------- 내꺼
// function solution(numbers) {
//   let answer = 0;
//   for(let i=0; i<10; i++){
//     if(numbers.indexOf(i) == -1){
//       answer += i;
//     };
//   };
//   return answer;
// }

// console.log(solution([1,2,3,4,6,7,8,0]))
// console.log(solution([5,8,4,0,6,7,9]))

// -------------------------------------------------------------------------------- 10. 부족한 금액 계산하기
// ------------------------------------------- 내꺼
// function solution(price, money, count) {
//   let sum = 0;
//   for(let i = 1; i <=count; i++){
//     sum += (price*i)
//   }
//   return money > sum? 0 : sum-money;
// };

// console.log(solution(3,20,4))