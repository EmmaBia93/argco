import { createStore } from 'vuex';
import bookModule from '../modules/book';
import authorModule from '../modules/author';
import categoryModule from '../modules/category';

export default createStore({
  modules: {
    books: bookModule,
    authors: authorModule,
    categories: categoryModule
  }
});
