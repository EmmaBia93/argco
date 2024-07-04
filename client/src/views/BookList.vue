<template>
  <div class="book-list">
    <div class="book-grid">
      <router-link 
        v-for="book in books" 
        :key="book.id" 
        :to="'/book/' + book.id"
      >
        <BookCard :book="book" />
      </router-link>
    </div>
  </div>
</template>

<style>
.book-list {
  padding: 16px;
}

.book-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: center;
}
</style>

<script>
import { mapState, mapActions } from 'vuex';
import BookCard from '../components/BookCard.vue';

export default {
  components: {
    BookCard
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
