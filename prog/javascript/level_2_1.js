'use strict';
// -------------------------------------------------------------------------------- 푼 문제
// 기능개발
// 프린터
// 다리를 지나는 트럭
// 소수 찾기
// 카펫
// ----------
// 가장 큰 수
// H - Index
// 타겟 넘버
// 구명보트
// 큰 수 만들기

// -------------------------------------------------------------------------------- API
// ---------------------------------------- Array.shift()
// 1. 재귀 돌릴 때,
// 끝나는 조건에 리턴 넣고,
// 함수 마지막에 리턴 넣어야지 undefined 안뜸.answer

// 2. 정답 함수 안에 재귀함수 선언하면,
// 인자로 받지 않은 변수도 사용가능하지만,
// 정답 함수 밖에 선언하면,
// 사용하는 변수는 전부 인자로 넣어줘야 한다.

// 3. 재귀에서 값을 만든 다음에,
// 그 값을 리턴값으로 주지말자.
// 외부의 값을 바꾸는 형식으로!!!! 

// ---------------------------------------- Array.shift()
// ---------------------------------------- 순열과 조합, 구현....ㅅㅂ
// https://nyang-in.tistory.com/212

// -------------------------------------------------------------------------------- 1. 기능개발
// ------------------------------------------- 내꺼 훨씬 빠름.
// function solution(progresses, speeds) {
//   const takeDaysToEnd = []
//   for(let i=0; i<progresses.length; i++){
//     const left = 100-progresses[i];
//     let takeDays = parseInt(left/speeds[i]);
//     if (left%speeds[i] !== 0){
//       takeDays += 1
//     }
//     takeDaysToEnd.push(takeDays);
//   }

//   const answer = [];
//   while(takeDaysToEnd.length >0){
//     let count = 0;
//     const now = takeDaysToEnd[0];
//     for(let i=0; i<takeDaysToEnd.length; i++){
//       if(now <takeDaysToEnd[i]){
//         break
//       } else{
//         count += 1;
//       }
//     }
//     for(let i=0; i<count; i++){
//       takeDaysToEnd.shift()
//     }
//     answer.push(count);
//   }
//   return answer;
// }
// ------------------------------------------- 커뮤
// function solution(progresses, speeds) {
//   let answer = [];
  
//   while(speeds.length > 0){
//     for(let i=0; i<speeds.length; i++){
//       if(progresses[i] < 100){
//         progresses[i] += speeds[i];
//       }
//     }

//     let deploy_count = 0;
//     while(progresses[0] >= 100){
//       progresses.shift();
//       speeds.shift();
//       deploy_count += 1;
//     }
//     if(deploy_count >0) {
//       answer.push(deploy_count);
//     }
//   }
//   return answer;
// }

// console.log(solution([93, 30, 55],[1, 30, 5]))
// console.log(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))

// -------------------------------------------------------------------------------- 2. 프린터
// priorities 돌면서,
// location은 꾸준히 체크
// 앞에꺼 빼고 뒤에꺼 스캔한 후
//   자기가 가장 높으면 
//     printOrder에 넣고,
//   높은게 있다면,
//     그대로 뒤로 넣는다.
// ------------------------------------------- 내꺼
// function solution(priorities, location) {
//   let printOrder = 0;
//   while(priorities.length > 0){
//     const now = priorities.shift();
//     location -= 1;

//     if (now >= Math.max(...priorities)){
//       printOrder+= 1;
//       if (location === -1){
//         break
//       }
//     } else{
//       priorities.push(now)
//       if (location === -1){
//         location = priorities.length-1;
//       }
//     }
//   }
//   return printOrder
// };

// console.log(solution([2, 1, 3, 2],2));
// console.log(solution([1, 1, 9, 1, 1, 1],0));

// -------------------------------------------------------------------------------- 3. 다리를 지나는 트럭
// ------------------------------------------- 내꺼 어휴 ㅅㅂ
// function solution(bridge_length, weight, truck_weights) {
//   const n = truck_weights.length;
//   const passedTruck = [];
//   const ing = [];

//   let time = 0;
//   while(passedTruck.length < n){
//     time += 1;

//     // ing 시간+1씩 하면서, 시간 지난거 있으면, passedTruck에 추가
//     for(let i=0; i<ing.length; i++){
//       ing[i][1] += 1;
//     }

//     if (ing.length > 0 && ing[0][1] > bridge_length){
//       passedTruck.push(ing.shift()[0]);
//     }
//     // 다리로 들어갈 수 있다면, 없다면,
//     if (ing.length <bridge_length && sumArray(ing) + truck_weights[0] <= weight){
//       const now = truck_weights.shift();
//       ing.push([now,1])
//     }
//   };
//   return time;
// };

// function sumArray(array){
//   let sum = 0;
//   for(let i=0; i<array.length; i++){
//     sum += array[i][0]
//   }
//   return sum
// }

// console.log(solution(2,10,[7,4,5,6]))
// console.log(solution(100,100,[10]))
// console.log(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))

// -------------------------------------------------------------------------------- 4. 소수 찾기
// 1. 조합 경우의 수 받은다음에
// 2. set으로 중복 없애고, 정렬
// 3. 소수인지 확인
// ------------------------------------------- 내꺼
// function solution(numbers) {
//   const n = numbers.length;
//   const numbersArray = numbers.split('');

//   let candidates = [];
//   for(let i=1; i<=n; i++){
//     // i개짜리 조합 만들어서, candidates에 넣기
//     const eachCandidate = getPermutations(numbersArray,i);

//     const afterMap = eachCandidate.map((item) => {
//       return parseInt(item.join(''))
//     })
//     candidates = [...candidates,...afterMap];
//   }
//   const realCandi = [...new Set(candidates)].sort((a,b) => a-b);
//   // console.log(realCandi);

//   // 3.소수인지 확인
//   let answer = 0;
//   for(let i=0; i<realCandi.length; i++){
//     if (isPrimeNumber(realCandi[i])){
//       answer += 1;
//     }
//   }
//   return answer;
// }

// function getPermutations(arr, selectNum) {
//   let result = [];
//   if (selectNum === 1){
//     return arr.map((item) => [item]);
//   }
//   arr.forEach((fixed, index, origin) => {
//     const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
//     const permutations = getPermutations(rest, selectNum - 1);
//     const attached = permutations.map((permutation) => [fixed, ...permutation]);
//     result.push(...attached);
//   });
//   return result;
// };

// function isPrimeNumber(number){
//   if (number === 1 ||number === 0){
//     return false
//   }
//   for (let i=2; i< parseInt(Math.sqrt(number))+1; i++){
//     if (number%i === 0){
//       return false
//     }
//   }
//   return true
// }

// console.log(solution('17'))
// console.log(solution('011'))

// -------------------------------------------------------------------------------- 5. 카펫
// ------------------------------------------- 내꺼
// function solution(brown, yellow) {
//   const totalMass = yellow + brown;
//   const candidates = [];
//   for(let i=3; i<parseInt(Math.sqrt(totalMass))+1; i++){
//     if(totalMass%i === 0){
//       candidates.push([parseInt(totalMass/i), i]);
//     }
//   }
//   // console.log(candidates)
//   let answer = [];
//   for(let i=0; i<candidates.length; i++){
//     const now = candidates[i]
//     if ((now[0]-2) * (now[1]-2) === yellow){
//       answer = now
//       break
//     }
//   }
//   return answer
// }
// console.log(solution(10,2))
// console.log(solution(8,1))
// console.log(solution(24,24))

// -------------------------------------------------------------------------------- 6. 가장 큰 수
// ------------------------------------------- 내꺼
// function solution(numbers) {
//   const strNumbers = numbers.map((item) => item.toString());

//   strNumbers.sort((a,b) => {
//     if (a.length > b.length){
//       while(a.length > b.length){
//         b += b[b.length-1];
//       }
//     } else if (a.length < b.length){
//       while(a.length < b.length){
//         a += a[a.length-1];
//       }
//     };

//     return a - b
//   }).reverse();

//   const answer = strNumbers.join('');

//   return parseInt(answer).toString();
// }


// // ------------------------------------------- 커뮤
// function solution(numbers) {
//   numbers.sort(sortFunc)
//   const answer = numbers.join('');
//   if(answer[0] === '0'){
//     return '0'
//   }
//   return answer;
// }
// const sortFunc =  (a,b) =>{
//   const compareA = parseInt(a.toString() + b.toString())
//   const compareB = parseInt(b.toString() + a.toString())
//   return compareB - compareA
// }

// console.log(solution([0,0,0]))
// console.log(solution([1,102]))
// console.log(solution([1,104]))
// console.log(solution([101,1009]))
// console.log(solution([9,998]))
// console.log(solution([6, 10, 2]))
// console.log(solution([3, 30, 34, 5, 9]))
// console.log(solution([5, 54,56,549,4]))

// -------------------------------------------------------------------------------- 7. H - Index
// ------------------------------------------- 내꺼
// function solution(citations){
//   citations.sort((a,b) => a-b);
//   const maxValue = citations[citations.length-1];

//   let answer = 0;
//   for (let i=0; i <= maxValue; i++){
//     let count = 0;
//     for (let j=0; j<=citations.length; j++){
//       if (citations[j] >= i){
//         count += 1;
//       }
//     }
//     if (count < i){
//       answer = i-1
//       break
//     }
//     answer = i
//   }
//   return answer
// }

// console.log(solution([3, 0, 6, 1, 5]));
// console.log(solution([1,1,1,1,1]));

// -------------------------------------------------------------------------------- 8. 타겟 넘버
// ------------------------------------------- 내꺼
// function solution(numbers, target) {
//   let count = 0;
//   dfs(numbers,0,0,count);
//   return count;

//   function dfs(numbers,depth,answer){
//     if (depth == numbers.length){
//       if(target === answer){
//         count ++
//       }
//       return
//     }
//     for(let i=0; i<2; i++){
//       if (i === 0 ){
//         answer += numbers[depth]
//         dfs(numbers,depth+1,answer)
//         answer -= numbers[depth]
//       } else{
//         answer -= numbers[depth]
//         dfs(numbers,depth+1,answer)
//         answer += numbers[depth]
//       }
//     }
//     return
//   }
// }

// ------------------------------------------- 커뮤 깔끔 그 자체!!
// function solution(numbers, target) {
//   let answer = 0;
//   getAnswer(0,0);
//   function getAnswer(x,value) {
//       if(x<numbers.length){
//           getAnswer(x+1,value + numbers[x]);
//           getAnswer(x+1,value - numbers[x]);
//       } else{
//           if(value === target){
//               answer++
//           }
//       }
//   }
//   return answer;
// }

// console.log(solution([1,1,1,1,1], 3))
// console.log(solution([4, 1, 2, 1], 4))

// -------------------------------------------------------------------------------- 9. 구명보트
// ------------------------------------------- 내꺼
// function solution(people, limit) {
//   people.sort((a,b) => a-b)
//   console.log(people);

//   let left = 0;
//   let right = people.length-1;
//   let answer = 0;

//   while(left <=right){
//     const sum = people[left] + people[right];
//     if (sum > limit){
//       right -= 1;
//       answer += 1;
//     } else{
//       left += 1;
//       right -= 1;
//       answer += 1;
//     }
//   }
//   return answer
// }

// console.log(solution([70, 50, 80, 50],100))
// console.log(solution([70, 80, 50],100))

// -------------------------------------------------------------------------------- 10. 큰 수 만들기
// ------------------------------------------- 커뮤
// function solution(number, k) {
//   const answer = [];
//   for(let i=0; i<number.length; i++){
//     while(answer.length > 0 && k>0 && answer[answer.length -1] < number[i] ){
//       answer.pop();
//       k-=1;
//     }
//     answer.push(number[i]);
//     console.log(answer)
//   }
//   if (k >0){
//     return answer.slice(0,answer.length-k).join('');
//   } else{
//     return answer.join('');
//   }
// }

// console.log(solution("1924",2))
// console.log(solution("1231234",3))
// console.log(solution("4177252841",4))