import SearchInput from './SearchInput.js';
import Suggestion from './Suggestion.js';
import SelectedLanguages from './SelectedLanguages.js';

import { fetchLanguages } from '../api.js';

export default function App({ target }) {
  this.state = {
    fetchedLanguages: [],
    selecetedLanguages: [],
  }
  this.setState = (nextState) => {
    this.state = {
      ...this.state,
      ...nextState
    };
    suggestion.setState({
      selectedIndex : 0,
      items: this.state.fetchedLanguages
    });
    selecetedLanguages.setState(this.state.selecetedLanguages);
  };
  const selecetedLanguages = new SelectedLanguages({
    target,
    initialState: []
  });
  const searchInput = new SearchInput({
    target,
    initialState: '',
    onChange : async(keyword) => {
      if (keyword.length === 0){
        this.setState({
          fetchedLanguages: [],
        })
      } else{
        const languaages = await fetchLanguages(keyword)
        console.log(languaages);
        this.setState({
          fetchedLanguages: languaages
        })
      }
    }
  });
  const suggestion = new Suggestion({
    target,
    initialState: {
      selectedIndex: 0,
      items:[]
    },
    onSelect: (language) => {
      alert(language);

      const nextSelectedLanguages = [...this.state.selecetedLanguages];
      console.log(nextSelectedLanguages,language);
      const index = nextSelectedLanguages.findIndex((selecetedLanguage) => selecetedLanguage === language);
      console.log(index);
      if (index > -1){
        nextSelectedLanguages.splice(index,1)
      }
      nextSelectedLanguages.push(language);

      this.setState({
        ...this.state,
        selecetedLanguages: nextSelectedLanguages
      })
    }
  })
}