import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import BookDetail from '../views/BookDetail.vue';
import BookList from '../views/BookList.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/books',
    name: 'BookList',
    component: BookList
  },
  {
    path: '/books/:id',
    name: 'BookDetail',
    component: BookDetail,
    props: true
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
