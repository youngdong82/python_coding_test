'use strict';
// -------------------------------------------------------------------------------- 푼 문제
// 문자열 내 p와 y의 개수
// x만큼 간격이 있는 n개의 숫자
// 핸드폰 번호 가리기
// 콜라츠 추측
// 짝수와 홀수
// ----------
// 제일 작은 수 제거하기
// 자연수 뒤집어 배열로 만들기
// 정수 내림차순으로 배치하기
// 하샤드 수
// 이상한 문자 만들기
// -------------------------
// 평균 구하기
// 자릿수 더하기
// 최대공약수와 최소공배수
// 정수 제곱근 판별
// 수박수박수박수박수박수?
// ----------
// 문자열 내림차순으로 배치하기
// 문자열 내 마음대로 정렬하기 *
// 서울에서 김서방 찾기
// 없는 숫자 더하기
// 부족한 금액 계산하기
// -------------------------
// 같은 숫자는 싫어
// 음양 더하기
// 소수 만들기
// 문자열 다루기 기본
// 가운데 글자 가져오기
// ----------
// K번째수
// 시저 암호
// 나누어 떨어지는 숫자 배열
// 완주하지 못한 선수
// 3진법 뒤집기

// -------------------------------------------------------------------------------- API
// JS는 Array에서 index 범위 벗어나면 undefined로 처리되지, 에러가 뜨지 않는다.
// const a = [1,2,3,4,5];

// for(let i= 0; i < a.length; i++){
//   console.log(a[i-1], a[i], a[i+1]);
// };
// // for in 으로 반복문 돌릴 때, i는 string이다!!!!!
// for(let i in a){
//   console.log(a[i-1], a[i], a[i+1]);
// };
// ------------------------------------ 반복문 대신 forEach!!!
// 기본 반복문 말고 다른것도 써보자!!

// ------------------------------------ isNaN(문자열)
// 문자열이 숫자가 아니면 true 리턴
// console.log(!isNaN('123'))
// console.log(!isNaN('000'))

// console.log(!isNaN('1r2'))
// console.log(!isNaN([]))
// console.log(!isNaN(null))

// console.log(!isNaN(undefined))
// console.log(!isNaN({}))
// ...이정도면 거의 못쓰는거 아니냐....

// ------------------------------------ JS 여러가지 숫자표기 방식
// JS에서 숫자 표현 방식에는 여러가지 있는데

// 대표적으로 진법을 통한 표기와 지수 표기법이 있습니다.

// 2진법은 0b11 -> 10진법 3
// 8진법은 0o77 -> 10진법 63
// 16진법은 0xff -> 10진법 255

// 지수 표기법은
// 21e6 -> 21x106 으로 21000000
// 3e09 -> 3x109 으로 3000000000

// 10진법을 각각 해당 표기법으로 표기할 수 있는데
// isNaN(string)의 경우
// string -> number 변경하고
// 변경된 값이 NaN 일 경우 true
// 아닐 경우 false를 반환합니다.

// 즉 string 진법 표기에 해당하거나 지수 표기법에 해당 할 경우
// 그 값이 10진수로 변환되어 NaN이 아니게 되므로 숫자가 맞다는 판별이 나오게 됩니다.

// ------------------------------------ JS에서 sort()
// javascript에서 단순 인자 안쓰고 sort()형태로 정렬하면
// 틀립니당
// 왜냐하면 sort의 기본 비교는 string 비교이기 때문
// const a = [1,3,8,6,10,4]
// console.log(a.sort())
// console.log(a.sort((a,b) => a-b))
// console.log(a.sort((a,b) => b-a))

// ------------------------------------  slice
// 파이썬에서 인덱싱이랑 비슷함

// ------------------------------------  아스키 코드 변환
// const a = 'A';
// const b = 'Z';
// const c = 'a';
// const d = 'z';
// console.log(a.charCodeAt());
// console.log(b.charCodeAt());
// console.log(c.charCodeAt());
// console.log(d.charCodeAt());
// console.log(String.fromCharCode(d.charCodeAt()));

// ------------------------------------ for in 반복문에 대해
// for ... in은 성능을 하락시킨다는 의미보다는
// 객체 내의 프로퍼티 속성 중 enumerable: true인 모든 프로퍼티를 순회하여 검색하는 용도이기 때문에 적합하지 않습니다.
// 따라서, 배열에 대해서는 for ... in 구문 보다는 for를 사용하거나 ES6의 forEach 함수를 사용하는 것을 권장합니다.
// 아니면,
// for (let i = 0; i < arr.length; i++) 식으로 씁시다.

// ------------------------------------ JS에서 해시테이블 Map
// 파이썬보다는 좀 귀찮게 되어있네...
// const map = new Map();
// map.set('hello',1);
// map.set('hello', (map.get('hello') || 0) + 1);
// map.set((map.get('hello')||0) + 1)
// console.log(map.get('hello'))

// console.log(map)

// ------------------------------------ JS에서 진수변환
// const a = 1535;
// // 3진수로 변환
// const a3 = a.toString(3)
// // 16진수로 변환
// const a16 = a.toString(16)
// console.log(a3)
// console.log(a16)

// // 10진법으로 돌아오기
// const afterA3 = parseInt(a3,3);
// const afterA16 = parseInt(a16,16);
// console.log(afterA3)
// console.log(afterA16)

// ------------------------------------ Array.includes('특정 값')

// -------------------------------------------------------------------------------- 1. 같은 숫자는 싫어
// ------------------------------------------- 내꺼
// function solution(arr){
//   let answer = [];
//   for(let i = 0; i < arr.length; i++){
//     if(arr[i] !== arr[i + 1]){
//       answer.push(arr[i]);
//     }        
//   }
//   return answer;
// }

// ------------------------------------------- 커뮤니티!!
// function solution(arr){
//   return arr.filter((val,index) => val != arr[index+1]);
// }

// console.log(solution([1,1,3,3,0,1,1]))
// console.log(solution([4,4,4,3,3]))

// -------------------------------------------------------------------------------- 2. 음양 더하기
// ------------------------------------------- 내꺼
// function solution(absolutes, signs) {
//   let sum = 0;
//   for(let i in absolutes){
//     if (signs[i]){
//       sum += absolutes[i]
//     } else{
//       sum -= absolutes[i]
//     }
//   }
//   return sum;
// };

// // ------------------------------------------- 커뮤
// function solution(absolutes, signs) {
//   let answer = 0;
//   absolutes.forEach((v, i) => {
//       if (signs[i]) {
//           answer += v;
//       } else {
//           answer -= v;
//       }
//   })
//   return answer;
// }

// console.log(solution([4,7,12],[true,false,true]))
// console.log(solution([1,2,3],[false,false,true]))

// -------------------------------------------------------------------------------- 3. 소수 만들기
// ------------------------------------------- 내꺼
// function solution(nums) {
//   let answer = 0
//   for(let i = 0; i<nums.length; i++){
//     for(let j = i+1; j<nums.length; j++){
//       for(let k = j+1; k<nums.length; k++){
//         const sum = nums[i]+nums[j]+nums[k];
//         if(check(sum)){
//           answer += 1;
//         }
//       }
//     }
//   }
//   return answer;
// };

// function check(num){
//   if (num <1){
//     return false
//   };
//   for(let i = 2; i < parseInt(Math.sqrt(num))+1; i++){
//     if(num%i == 0){
//       return false
//     }
//   };
//   return true;
// }
// console.log(solution([1,2,3,4]))
// console.log(solution([1,2,7,6,4]))

// -------------------------------------------------------------------------------- 4. 문자열 다루기 기본
// ------------------------------------------- 내꺼
// function solution(s) {
//   if(s.length== 4 | s.length===6){
//     for(let i in s){
//       if(isNaN(s[i])){
//         return false;
//       }
//     }
//     return true
//   }
//   return false;
// };

// console.log(solution('a234'));
// console.log(solution('1234'));
// console.log(solution('1e00'));
// console.log(isNaN('1e22'));
// console.log(isNaN('weer'));

// -------------------------------------------------------------------------------- 5. 가운데 글자 가져오기
// ------------------------------------------- 내꺼
// function solution(s) {
//   const mid = parseInt(s.length/2)
//   if(s.length %2 === 0){
//     //짝수라면
//     return s[mid-1] + s[mid]
//   }else{
//     //홀수라면
//     return s[mid]
//   }
// };

// console.log(solution("abcde"));
// console.log(solution("qwer"));
// console.log(solution("q"));
// console.log(solution("qw"));

// -------------------------------------------------------------------------------- 6. K번째수
// ------------------------------------------- 내꺼 + slice 
// function solution(array, commands) {
//   let answer = [];
//   for(let i in commands){
//     const [start,end,indexValue] = commands[i];
//     const slicedArray = array.slice(start-1,end);
//     slicedArray.sort((a,b) => a-b)
//     answer.push(slicedArray[indexValue-1])
//   }
//   return answer;
// };

// console.log(solution([1,5,2,6,3,7,4], [[2,5,3],[4,4,1],[1,7,3]]))

// -------------------------------------------------------------------------------- 7. 시저 암호
// ------------------------------------------- 내꺼
// function solution(s, n) {
//   const answer = s.split('').map((item) => {
//     if (item === ' '){
//       return item
//     }else if(item === item.toUpperCase()){
//       let afterPlus = item.charCodeAt()+n
//       if (afterPlus > 90){
//         afterPlus -= 26
//       }
//       return String.fromCharCode(afterPlus);
//     } else{
//       let afterPlus = item.charCodeAt()+n
//       if (afterPlus > 122){
//         afterPlus -= 26
//       }
//       return String.fromCharCode(afterPlus);

//     }
//   });
//   return answer.join('')
// }
// console.log(solution("Az", 1))
// console.log(solution("z", 1))
// console.log(solution("a B z", 4))

// -------------------------------------------------------------------------------- 8. 나누어 떨어지는 숫자 배열
// ------------------------------------------- 내꺼
// function solution(arr, divisor) {
//   let answer = [];
//   for(let i in arr){
//     if(arr[i] % divisor === 0){
//       answer.push(arr[i])
//     }
//   };
//   answer.sort((a,b) => a-b)
//   return answer.length === 0 ? [-1] : answer;
// }

// ------------------------------------------- 내꺼 + filter
// function solution(arr, divisor) {
//   const answer = arr.filter(item => item % divisor === 0)
//   answer.sort((a,b) => a-b)
//   return answer.length === 0 ? [-1] : answer;
// }

// console.log(solution([5, 9, 7, 10],5))
// console.log(solution([2, 36, 1, 3],1))
// console.log(solution([3,2,6],10))

// -------------------------------------------------------------------------------- 9. 완주하지 못한 선수
// ------------------------------------------- 내꺼
// function solution(participant, completion) {
//   const map = new Map();

//   for(let i = 0; i < participant.length; i++) {
//     let a = participant[i];
//     let b = completion[i];

//     map.set(a, (map.get(a) || 0) + 1);
//     map.set(b, (map.get(b) || 0) - 1);
//   }

//   for(let [k, v] of map) {
//     if(v > 0){
//       return k;
//     }
//   }
// }

// console.log(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
// console.log(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
// console.log(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))

// -------------------------------------------------------------------------------- 10. 3진법 뒤집기
// ------------------------------------------- 내꺼
// function solution(n) {
//   let afterConvert = n.toString(3);
//   return parseInt(afterConvert.split('').reverse().join(''),3)
// }

// console.log(solution(45))
// console.log(solution(125))