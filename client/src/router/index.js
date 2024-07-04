import { createRouter, createWebHistory } from 'vue-router';
import BookList from '../views/BookList.vue';
import BookTable from '../views/BookTable.vue';
import BookDetail from '../views/BookDetail.vue';
import BookForm from '../components/BookForm.vue';

const routes = [
  {
    path: '/',
    name: 'BookList',
    component: BookList
  },
  {
    path: '/book/:id',
    name: 'BookDetail',
    component: BookDetail,
    props: true
  },
  {
    path: '/admin/books',
    name: 'BookTable',
    component: BookTable
  },
  {
    path: '/admin/book/create',
    name: 'BookForm',
    component: BookForm,
    props: { id: 'create' }
  },
  {
    path: '/admin/book/:id',
    name: 'BookForm',
    component: BookForm,
    props: true
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
