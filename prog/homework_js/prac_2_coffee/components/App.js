import ProductListPage from './ProductListPage.js';
import ProductDetailPage from './ProductDetailPage.js';
import CartPage from './CartPage.js';


const LOCAL_URL = '/python/prog/homework_js/prac_2_coffee/index.html';

export default function App({target}){
  this.route = () => {
    console.log('hello from app.js',location.pathname)
    const {pathname} = location;
    target.innerHTML = '';
    
    if (pathname === '/'){
      new ProductListPage({target}).render();
    } else if(pathname.indexOf('/products') === 0){
      const [,,productId] = pathname.split('/')
      new ProductDetailPage({ target, productId }).render();
    } else if(pathname === '/cart'){
      new CartPage({ target }).render();
    }
  }
  this.route();
}