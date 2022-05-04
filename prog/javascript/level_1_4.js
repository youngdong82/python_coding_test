// const lang = ['abcd','abc','ab','a','abcde'];

// const filteredLang = lang.filter((each) => each.includes('abc'))

// console.log(filteredLang);

// Suggestion에 있는
// e.target.closest()

// data-index로 값이 적용되어있는 것은
// const {index} = sli.dataset으로 가져올 수 있다.

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
// -------------------------
// 예산
// 로또의 최고 순위와 최저 순위
// 체육복
// 두 개 뽑아서 더하기
// 모의고사
// ---------- 카카오 7문제
// 비밀지도
// 숫자 문자열과 영단어
// 크레인 인형뽑기 게임
// [1차] 다트 게임
// 신고 결과 받기
// 신규 아이디 추천
// 키패드 누르기

// -------------------------------------------------------------------------------- API
// ------------------------------------------- set
// python이랑 비슷
// new Set(Array) 이렇게 사용하자.
// ------------------------------------------- padStart, padEnd


// ------------------------------------------- 2차원 배열 초기화
// const graph = Array(arr1.length);
// for(let i=0; i<arr1.length; i++){
//   graph[i] = Array(arr2.length).fill(0)
// }
// console.log(graph);
// ------------------------------------------- Map과 Set
// https://ko.javascript.info/map-set
// function test() {
//   const digitAlpha = ['zero','one','two','three','four','five','six','seven','eight','nine'];
//   const digitMap = new Map();
//   for(let i=0; i<digitAlpha.length; i++){
//     digitMap.set(digitAlpha[i],i)
//   }
//   console.log(digitMap)
//   console.log(digitMap.keys())
//   console.log(digitMap.values())
//   console.log(digitMap.entries())
// }

// https://lakelouise.tistory.com/38

// ------------------------------------------- 문자열 숫자인지 확인
// 1. isNaN()
//   NaN이라면 true,
//   숫자라면 false
// 2. Number()
//   가능하면 숫자,
//   불가능하면 NaN
// 3. parseInt()
//   가능하면 숫자,
//   불가능하면 NaN

// 여러가지 쓰다보면 그래도 isNaN이 가장 나은듯...?

// ---------------------- 비교
// if(Number('1')){
//   console.log('good')
// }
// if(parseInt('a')){
//   console.log('good')
// }
// 그러나 직접 비교시 통과되지 않는다.
// ===는 false 뜨지만, ==는 같다고 뜬다.

// 그.러.나.
// NaN == false
// 이거는 또 false 뜸...

// ---------------------- parseInt와 Number의 차이
// https://velog.io/@blackwidow/parseInt%EC%99%80-Number%EC%9D%98-%EC%B0%A8%EC%9D%B4

// ---------------------- replace JS와 파이썬의 차이...
// 파이썬은 모조리 다 바꾸지만,
// JS는 왼쪽부터 딱 하나만 바꾼다... 평신이야??

// ---------------------- 정규표현식...
// ---------------------- Map과 object의 차이
// 타입은 같지만 전혀 다르다.
// const a = new Map();
// const b = {};


// console.log(typeof(a));
// console.log(typeof(b));
// console.log(a);
// console.log(b);

// -------------------------------------------------------------------------------- 1. 예산
// ------------------------------------------- 내꺼
// function solution(d, budget) {
//   d.sort((a,b) => a-b);
//   let sum = 0;
//   let count = 0;
//   for(let i = 0; i<d.length; i++){
//     sum += d[i];
//     count += 1;
//     if (sum === budget){
//       break
//     } else if(sum > budget){
//       count -=1;
//       break
//     };
//   }
//   return count
// }

// console.log(solution([4],3))
// console.log(solution([4],9))
// console.log(solution([1,3,2,5,4],9))
// console.log(solution([2,2,3,3],10))

// -------------------------------------------------------------------------------- 2. 로또의 최고 순위와 최저 순위
// ------------------------------------------- 내꺼 + 커뮤 훨씬 깔끔
// function solution(lottos, win_nums) {
//   const rank = [6,6,5,4,3,2,1]
//   let match = 0;
//   let zeroCount = 0;
//   for(let i = 0; i<lottos.length; i++){
//     if (lottos[i] === 0){
//       zeroCount += 1;
//     }
//     for(let j = 0; j<win_nums.length; j++){
//       if (lottos[i] === win_nums[j]){
//         match += 1;
//       }
//     }
//   }
//   return [rank[match+zeroCount], rank[match]];
// };

// console.log(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
// console.log(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
// console.log(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))

// -------------------------------------------------------------------------------- 3. 체육복
// ------------------------------------------- 내꺼
// function solution(n, lost, reserve) {
//   const init = Array(n).fill(0);

//   for(let i=0; i<lost.length; i++){
//     init[lost[i]-1] -= 1;
//   }
//   for(let i=0; i<reserve.length; i++){
//     init[reserve[i]-1] += 1;
//   }

//   let cant = 0;
//   for(let i=0; i<n; i++){
//     if(init[i] === -1){
//       if(init[i-1] >= 1){
//         init[i-1] -= 1;
//         init[i] += 1;
//       } else if(init[i+1] >= 1){
//         init[i+1] -= 1;
//         init[i] += 1;
//       }
//     }
//     if(init[i] === -1){
//       cant += 1
//     }
//   }
//   return n-cant
// }
// console.log(solution(5,[2, 4],[1, 3, 5]))
// console.log(solution(5,[2, 4],[3]))
// console.log(solution(3,[3],[1]))

// -------------------------------------------------------------------------------- 4. 두 개 뽑아서 더하기
// ------------------------------------------- 내꺼
// function solution(numbers) {
//   let answer = [];
//   for(let i = 0; i<numbers.length; i++){
//     for(let j = i+1; j<numbers.length; j++){
//       const sum = numbers[i]+numbers[j];
//       if(!answer.includes(sum)){
//         answer.push(sum)
//       }
//     }
//   }
//   answer.sort((a,b) => a-b);
//   return answer;
// }
// ------------------------------------------- 커뮤 Set 내꺼보다 훨씬 빠르다. 잘 이용하자!! python set함수랑 비슷함.
// function solution(numbers) {
//   let tmp = [];
//   for(let i = 0; i<numbers.length; i++){
//     for(let j = i+1; j<numbers.length; j++){
//       tmp.push(numbers[i]+numbers[j])
//     }
//   }
//   const answer = [...new Set(tmp)];
//   answer.sort((a,b) => a-b);
//   return answer;
// }

// console.log(solution([2,1,3,4,1]))
// console.log(solution([5,0,2,7]))

// -------------------------------------------------------------------------------- 5. 모의고사
// ------------------------------------------- 내꺼
// function solution(answers) {
//   const student1 = [1,2,3,4,5];
//   const student2 = [2,1,2,3,2,4,2,5];
//   const student3 = [3,3,1,1,2,2,4,4,5,5];
//   const answerArray = [0,0,0];

//   for(let i = 0; i < answers.length; i++){
//     if(student1[i % student1.length] === answers[i]){
//       answerArray[0] += 1;
//     }
//     if(student2[i% student2.length] === answers[i]){
//       answerArray[1] += 1;
//     }
//     if(student3[i % student3.length] === answers[i]){
//       answerArray[2] += 1;
//     }
//   }
//   const maxValue = Math.max(...answerArray)

//   const answer = [];
//   for(let i=0; i<3; i++){
//     if (answerArray[i] === maxValue){
//       answer.push(i+1);
//     }
//   }
//   return answer;
// }

// console.log(solution([1,2,3,4,5]));
// console.log(solution([1,3,2,4,2]));

// -------------------------------------------------------------------------------- 6. 비밀지도
// ------------------------------------------- 내꺼
// function solution(n, arr1, arr2) {
//   const answer = [];

//   for(let i=0; i<n; i++){
//     const tmpArray1 = arr1[i].toString(2).padStart(n,'0').split('');
//     const tmpArray2 = arr2[i].toString(2).padStart(n,'0').split('');

//     let mergedString = '';
//     for(let j=0; j<n; j++){
//       const mergedValue = parseInt(tmpArray1[j]) + parseInt(tmpArray2[j]);
//       if (mergedValue === 0){
//         mergedString += ' ';
//       } else{
//         mergedString += '#';
//       }
//     }
//     answer.push(mergedString);
//   }
//   return answer;
// }

// console.log(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]));
// console.log(solution(6, [46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]));

// -------------------------------------------------------------------------------- 7. 숫자 문자열과 영단어
// ------------------------------------------- 내꺼
// function solution(s) {
//   const digitAlpha = ['zero','one','two','three','four','five','six','seven','eight','nine'];
//   const digitMap = new Map();
//   for(let i=0; i<digitAlpha.length; i++){
//     digitMap.set(digitAlpha[i],i)
//   }
  
//   let answer = '';
//   let tmp = '';
//   for(let i=0; i<s.length; i++){
//     if(Number(s[i])){
//       answer += s[i];
//     } else{
//       tmp += s[i];
//     };
//     if (digitMap.has(tmp)){
//       answer += digitMap.get(tmp);
//       tmp = '';
//     }
//   }
//   return parseInt(answer);
// }

// console.log(solution("one4seveneight"))
// console.log(solution("23four5six7"))
// console.log(solution("2three45sixseven"))
// console.log(solution("123"))

// -------------------------------------------------------------------------------- 8. 크레인 인형뽑기 게임
// ------------------------------------------- 내꺼
// function solution(board, moves) {
//   const n = board.length;
//   const stack = [];
//   let answer = 0;


//   for(let i=0; i<moves.length; i++){
//     const outIndex = moves[i]-1;
//     for(let j=0; j<n; j++){
//       if(board[j][outIndex] != 0){
//         if (board[j][outIndex] === stack[stack.length-1]){
//           stack.pop();
//           answer += 2
//         } else{
//           stack.push(board[j][outIndex]);
//         }
//         board[j][outIndex] = 0
//         break
//       }
//     }
//   }
//   return answer;
// }

// console.log(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

// -------------------------------------------------------------------------------- 9. [1차] 다트 게임
// ------------------------------------------- 내꺼
// function solution(dartResult) {

//   let afterConvert = dartResult;
//   while(afterConvert.replace('10','A') !== afterConvert){
//     afterConvert = afterConvert.replace('10','A');
//   };

//   const answerReck = [];
//   const mutiple = ['S','D','T'];
//   const bonus = ['*','#'];

//   for(let i=0; i<afterConvert.length;i++){
//     const now = afterConvert[i];
//     if (!isNaN(now) || now === 'A'){
//       if (now === 'A'){
//         answerReck.push(10);
//       } else{
//         answerReck.push(parseInt(now));
//       }
//     } else if(mutiple.includes(now)){
//       if (now === 'D'){
//         answerReck[answerReck.length-1] **= 2
//       } else if(now === 'T'){
//         answerReck[answerReck.length-1] **= 3
//       }
//     } else if(bonus.includes(now)){
//       if (now === '*'){
//         if(answerReck.length >1){
//           answerReck[answerReck.length-2] *= 2
//           answerReck[answerReck.length-1] *= 2
//         }else{
//           answerReck[answerReck.length-1] *= 2
//         }
//       } else{
//         answerReck[answerReck.length-1] = -answerReck[answerReck.length-1]
//       }
//     }
//   }
//   // console.log(answerReck);
//   return answerReck.reduce((a,b) => a+b);
// }

// console.log(solution('1S2D*3T'));
// console.log(solution('1D2S#10S'))
// console.log(solution('1D2S0T'))
// console.log(solution('1S*2T*3S'))
// console.log(solution('1D#2S*3S'))
// console.log(solution('1T2D3D#'))
// console.log(solution('1D2S3T*'))
// console.log(solution('2T#1S*1S'))
// console.log(solution('10S10S10S'))

// -------------------------------------------------------------------------------- 10. 신고 결과 받기
// ------------------------------------------- 내꺼
// function solution(id_list, report, k) {
//   let reports = [...new Set(report)].map(a => {return a.split(' ')})
//   let reportTo = new Map();
//   for(const bad of reports){
//     reportTo.set(bad[1], reportTo.get(bad[1])+1 || 1)
//   }
  
//   let reportFrom = new Map();
//   for(const bad of reports){
//     if (reportTo.get(bad[1]) >= k){
//       reportFrom.set(bad[0],reportFrom.get(bad[0])+1 || 1)
//     }
//   }

//   let answer = id_list.map(a => reportFrom.get(a) || 0 );
//   return answer;
// }

// console.log(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2));
// console.log(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3));

// -------------------------------------------------------------------------------- 11. 신규 아이디 추천
// ------------------------------------------- 내꺼
// function solution(new_id) {
//   const alpha = /[a-zA-Z0-9]/;
//   const useChar = ['_','-','.'];
//   //1
//   const lowerId = new_id.toLowerCase();
//   //2,3
//   let answer = '';
//   for(let i=0; i<lowerId.length; i++){
//     const now = lowerId[i];
//     if (alpha.test(now) || useChar.includes(now)){
//       if (now === '.' && answer[answer.length-1] === '.'){
//         continue
//       }
//       answer += now;
//     }
//   }
//   //4
//   if (answer[0] === '.'){
//     answer = answer.slice(1);
//   }
//   // console.log(answer);
//   if (answer[answer.length-1] === '.'){
//     answer = answer.slice(0,answer.length-1);
//   }
//   //5
//   if (answer === ''){
//     answer += 'a';
//   };
//   // console.log(answer)
//   //6
//   if (answer.length >= 16){
//     answer = answer.slice(0,15);
//     if (answer[answer.length-1] === '.'){
//       answer = answer.slice(0,answer.length-1);
//     };
//   };
//   //7
//   if(answer.length <=2){
//     while(answer.length <=2){
//       answer += answer[answer.length-1];
//     }
//   };
//   return answer
// }

// ------------------------------------------- 커뮤 + 정규식 개쩐다....
// function solution(new_id) {
//   const answer = new_id
//       .toLowerCase() // 1
//       .replace(/[^\w-_.]/g, '') // 2
//       .replace(/\.+/g, '.') // 3
//       .replace(/^\.|\.$/g, '') // 4
//       .replace(/^$/, 'a') // 5
//       .slice(0, 15).replace(/\.$/, ''); // 6
//   const len = answer.length;
//   return len > 2 ? answer : answer + answer.charAt(len - 1).repeat(3 - len);
// }

// console.log(solution("...!@BaT#*..y.abcdefghijklm"))
// console.log(solution("z-+.^."))
// console.log(solution(	"=.="))
// console.log(solution(	"123_.def"))
// console.log(solution("abcdefghijklmn.p"))

// -------------------------------------------------------------------------------- 12. 키패드 누르기
// ------------------------------------------- 내꺼
// function solution(numbers, hand) {
//   const btnMap = {1: [0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], '*':[3,0], 0:[3,1], '#':[3,2]}
//   const leftPart = [1,4,7,'*'];
//   const rightPart = [3,6,9,'#'];
//   let leftNow = '*';
//   let rightNow = '#';

//   let answer = ''
//   for(let i=0; i<numbers.length; i++){
//     if (leftPart.includes(numbers[i])){
//       leftNow = numbers[i];
//       answer += 'L';
//     } else if (rightPart.includes(numbers[i])){
//       rightNow = numbers[i];
//       answer += 'R';
//     } else{
//       const nowXY = btnMap[numbers[i]];
//       const leftXY = btnMap[leftNow];
//       const rightXY = btnMap[rightNow];

//       const leftDist =  Math.abs(nowXY[0]-leftXY[0]) + Math.abs(nowXY[1]-leftXY[1]);
//       const rightDist =  Math.abs(nowXY[0]-rightXY[0]) + Math.abs(nowXY[1]-rightXY[1]);

      
//       if (leftDist<rightDist){
//         leftNow = numbers[i]
//         answer += 'L';
//       }else if(leftDist>rightDist){
//         rightNow = numbers[i]
//         answer += 'R';
//       }else{
//         if(hand === 'left'){
//           leftNow = numbers[i]
//           answer += 'L';
//         } else{
//           rightNow = numbers[i]
//           answer += 'R';
//         };
//       };
//     }
//   };
//   return answer;
// }

// console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
// console.log(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
// console.log(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))