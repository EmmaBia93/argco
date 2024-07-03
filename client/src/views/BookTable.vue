<template>
  <router-link :to="'/admin/book/create'">Crear</router-link>

  <table>
    <thead>
      <tr>
        <th>#</th>
        <th>Título</th>
        <th>Autor</th>
        <th colspan="2">Acciones</th>
      </tr>
    </thead>
    <tbody>
      <BookRow
        v-for="(book, index) in books"
        :key="book.id"
        :book="book"
        :index="index + 1"
      />
    </tbody>
  </table>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import BookRow from '../components/BookRow.vue';

export default {
  components: {
    BookRow
  },
  computed: {
    ...mapState('books', { books: state => state.books}),
  },
  methods: {
    ...mapActions('books', ['fetchBooks']),
  },
  created() {
    this.fetchBooks();
  }
}
</script>