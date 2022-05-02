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

