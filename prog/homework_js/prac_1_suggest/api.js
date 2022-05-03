export const API_END_POINT = 'API END POINT'

const LANGS = [
  'html',
  'css',
  'javascript',
  'typescript',
  'react',
  'redux',
  'vue',
  'node',
  'express',
  'next',
  'go',
  'rust',
  'c++',
  'c#',
  'python',
  'django',
  'nest',
  'react native',
  'andloid',
  'swift',
  'mysql',
];

// const request = async(inputFromClient) => {
//   const matchLang = LANGS.filter((eachLang) => eachLang.includes(inputFromClient))
// }

export const fetchLanguages = async(keyword) => {
  const matchLang = LANGS.filter((eachLang) => eachLang.includes(keyword));
  return matchLang;
};
  
//   const res = await fetch(url);

//   if (res.ok){
//     const json = await res.json()
//     return json
//   }
//   throw new Error('요청 실패')
// }

// export const fetchLanguages = async(keyword) => request(
//   `${API_END_POINT}/languaages?keyword=${keyword}`
//   );