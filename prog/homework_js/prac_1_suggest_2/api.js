const LANGS = [
  'html',
  'css',
  'javascript',
  'typescript',
  'java',
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

export const fetchLanguages = async(keyword) => {
  const matchLang = LANGS.filter((eachLang) => eachLang.includes(keyword));
  return matchLang;
};