import { createStore } from 'vuex';
import bookModule from '../modules/book';
import categoryModule from '../modules/category';

export default createStore({
  modules: {
    books: bookModule,
    categories: categoryModule
  }
});
