'use strict';
// -------------------------------------------------------------------------------- 푼 문제
// 문자열 내 p와 y의 개수
// x만큼 간격이 있는 n개의 숫자
// 핸드폰 번호 가리기
// 콜라츠 추측
// 짝수와 홀수
// 제일 작은 수 제거하기
// 자연수 뒤집어 배열로 만들기
// 정수 내림차순으로 배치하기
// 하샤드 수
// 이상한 문자 만들기


// -------------------------------------------------------------------------------- API
// --------------------------------------- int 관련
// a = 1
// a = a.toString()
// console.log(typeof(a))
// ------------------ 자동 형 변환
// console.log(1); 
// console.log(1+''); 
// console.log(typeof(1+'')); 

// console.log('8'); 
// console.log('8' * 2); 
// console.log(typeof('8' * 1)); 

// console.log('8' + 2); 
// console.log(typeof('8' + 2)); 

// --------------------------------------- 문자열 관련
// let string = 'StRing1';
// string1 = string.toLowerCase();
// string2 = string.toUpperCase();
// 인자만큼 왼쪽에서 빼기
// string3 = string.substring(3);
// 'string'. 
// 'string'.

// console.log(string1)
// console.log(string2)
// console.log(string3)

// 문자열을 배열로
// console.log(string.split(''))

//문자열은 기본적으로 배열취급
// 파이썬과 같이 문자열에 인덱싱으로 값 설정은 불가
// const a = 'apple'
// for(let i in a){
//   if (i%2 == 0){
//     a[i] = a[i].toUpperCase();
//   }
//   console.log(a[i]);
// }
// console.log(a)
// --------------------------------------- 배열 관련
// let array = [1,2,3,4,5]
// let array1 = Array(array.length)
// let array2 = Array(array.length+1).join('*')
// splice = 기존 요소를 삭제 또는 교체하거나 새 요소를 추가하여 배열의 내용을 변경
// array.splice(index, deleteTime, string1, string2, ...)
// ref: https://tocomo.tistory.com/31

// console.log(array.indexOf(3))
// Array.map()
// Array.forEach()
// Array.filter()
// ------------------ 배열 뒤집기
// console.log(array.reverse());

// console.log(array1)
// console.log(array2)
// delete로 규민이꺼 임시방편 해결 가능하려나?
// --------------------------------------- 반복문
// for (let i = 0; i++){
//   //something
// }
// ------------------ for(let i in Array){}
// array 안에서 인덱스 돌릴 때 사용.
// 일반 for문보다 훨씬 많이 쓸 듯.
// const a = [1,2,34,5];

// for (let i in a){
//   a[i] += 1
// }
// console.log(a);
// while()


// Math.min(Array)
// Math.max(Array)
// -------------------------------------------------------------------------------- 1. 문자열 내 p와 y의 개수
// 1. 전부 소문자로 바꾼 후,
// 2. p갯수,y갯수 선언
// 3. s돌면서, 2 개의 갯수가 같으면 True 다르면 Flase
// ------------------------------------------- 내꺼
// function solution(s) {
//   s = s.toLowerCase();
//   let countP = 0;
//   let countY = 0;
//   for (let i = 0; i < s.length; i++){
//     if (s[i] === 'p'){
//       countP += 1
//     } else if(s[i] === 'y'){
//       countY += 1
//     };
//   };
//   if (countP === countY){
//     return true
//   } else{
//     return false
//   };
// };

// console.log(solution("pPoooyY"))
// console.log(solution("Pyy"))
// console.log(solution(""))

// -------------------------------------------------------------------------------- 2. x만큼 간격이 있는 n개의 숫자
// ------------------------------------------- 내꺼

// function solution(x, n) {
//   const answer = [];
//   for (let i=1; i<=n; i++){
//     now = i*x
//     answer.push(now)
//   };
//   return answer;
// };

// ------------------------------------------- 커뮤니티
// function solution(x, n) {
//   return Array(n).fill(x).map((v, i) => (i + 1) * v)
// }
// console.log(solution(2, 5))
// console.log(solution(4, 3))
// console.log(solution(-4, 2))

// -------------------------------------------------------------------------------- 3. 핸드폰 번호 가리기
// phone_number는 길이 4 이상, 20이하인 문자열
// ------------------------------------------- 내꺼
// function solution(phone_number) {
//   let answer = '';
//   for(let i=0; i<phone_number.length; i++){
//     if (i < phone_number.length-4){
//       answer += '*'
//     } else{
//       answer += phone_number[i]
//     }
//   };
//   return answer;
// };

// ------------------------------------------- 커뮤니티
// function solution(s){
//   var result = Array(s.length-3).join("*") 
//   console.log(result)
//   var cut = s.substring(s.length-4) 

//   return result+cut;
// }

// console.log(solution("01033334444"))
// console.log(solution("027778888"))
// console.log(solution("2778"))

// -------------------------------------------------------------------------------- 4. 콜라츠 추측
// ------------------------------------------- 내꺼
// function solution(num) {
//   let i = 0
//   while(i<=500){
//     if (num === 1){
//       break;
//     }
//     if (num %2 === 0){
//       num = num /2
//     } else{
//       num = num * 3 + 1
//     }
//     i += 1
//   }
//   if (num !== 1){
//     return -1
//   } else{
//     return i
//   }
// };

// console.log(solution(6))
// console.log(solution(16))
// console.log(solution(626331))

// -------------------------------------------------------------------------------- 5. 짝수와 홀수
// ------------------------------------------- 내꺼

// function solution(num) {
//   if (num%2 === 0){
//     return 'Even';
//   } else{
//     return 'Odd';
//   };
// }

// console.log(solution(3))
// console.log(solution(4))

// -------------------------------------------------------------------------------- 6. 제일 작은 수 제거하기
// ------------------------------------------- 내꺼
// function solution(arr) {
//   const miniValue = Math.min(...arr);
//   const filterArray = arr.filter((each)=>{
//     return each !== miniValue;
//   });

//   if (filterArray.length === 0){
//     return [-1]
//   } else{
//     return filterArray
//   };
// };

// ------------------------------------------- 커뮤니티 splice
// function solution(arr) {
//   if (arr.length > 1) {
//       var minNum = Math.min(...arr);
//       var idx = arr.indexOf(minNum);
//       arr.splice(idx, 1);
//   } else {
//       arr = [-1];
//   }
//   return arr;
// }

// console.log(solution([4,3,2,1]));
// console.log(solution([1,2,3,4]));
// console.log(solution([10]));

// -------------------------------------------------------------------------------- 7. 자연수 뒤집어 배열로 만들기
// ------------------------------------------- 내꺼
// function solution(n) {
//   n_array = n.toString().split('');
//   answer = n_array.reverse().map(item => parseInt(item)); 
  
//   return answer;
// };

// console.log(solution(12345))
// -------------------------------------------------------------------------------- 8. 정수 내림차순으로 배치하기
// ------------------------------------------- 내꺼
// function solution(n) {
//   return parseInt(n.toString().split('').sort().reverse().join(''));
// };

// console.log(solution(118372));
// -------------------------------------------------------------------------------- 9. 하샤드 수
// ------------------------------------------- 내꺼
// function solution(x) {
//   const xArray = x.toString().split('');
//   let sumValue = 0;
//   for(let i in xArray){
//     sumValue = sumValue + parseInt(xArray[i]);
//   };
//   if (x % sumValue === 0){
//     return true
//   } else{
//     return false
//   }
// };

// ------------------------------------------- 커뮤니티 10진법 수 나누기 속도는 내꺼가 더 빠름
// function solution(n){
//   var result ;
//   //함수를 완성하세요
//     var ori_n = n;
//   var sum =0;
//   while(n){
//     sum += n%10;
//     n /= 10;
//     n = Math.floor(n);
//   }
//   if(ori_n%sum == 0)
//     result = true;
//   else
//     result = false;
//   return result;
// }

// console.log(solution(1047));
// console.log(solution(12));
// console.log(solution(11));
// console.log(solution(13));

// -------------------------------------------------------------------------------- 10. 이상한 문자 만들기;
// ------------------------------------------- 내꺼
// function solution(s) {
//   const splitedS = s.split(' ');
//   let answer = []
//   for(let i in splitedS){
//     console.log(splitedS[i]);
//     let tmp = ''
//     for (let j in splitedS[i]){
//       if (j%2 === 0){
//         tmp += splitedS[i][j].toUpperCase();
//       } else{
//         tmp += splitedS[i][j].toLowerCase();
//       }
//     }
//     answer.push(tmp)
//   }
//   return answer.join(' ')
// }

// console.log(solution("try hello world"))

