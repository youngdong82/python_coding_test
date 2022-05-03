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
// ---------- 카카오 5문제


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
function solution(n, arr1, arr2) {
  const answer = [];

  for(let i=0; i<n; i++){
    const tmpArray1 = arr1[i].toString(2).padStart(n,'0').split('');
    const tmpArray2 = arr2[i].toString(2).padStart(n,'0').split('');

    let mergedString = '';
    for(let j=0; j<n; j++){
      const mergedValue = parseInt(tmpArray1[j]) + parseInt(tmpArray2[j]);
      if (mergedValue === 0){
        mergedString += ' ';
      } else{
        mergedString += '#';
      }
    }
    answer.push(mergedString);
  }
  return answer;
}

console.log(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]));
// console.log(solution(6, [46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]));

// -------------------------------------------------------------------------------- 7. 
// ------------------------------------------- 내꺼
// -------------------------------------------------------------------------------- 8. 
// ------------------------------------------- 내꺼
// -------------------------------------------------------------------------------- 9. 
// ------------------------------------------- 내꺼
// -------------------------------------------------------------------------------- 10. 
// ------------------------------------------- 내꺼