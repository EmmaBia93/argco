<template>
  <div class="book-card">
    <img :src="book.cover" :alt="book.title">
    <h3>{{ book.title }}</h3>
    <p>{{ `${book.author.last_name}` + ', ' + `${book.author.first_name}` }}</p>
  </div>
</template>

<style>
.book-card {
  padding: 16px;
  margin: 8px;
  text-align: center;
  width: 200px;

  & img {
    width: 100%;
    height: 50vh;
  }
}
</style>

<script>
export default {
  props: {
    book: {
      type: Object,
      required: true
    }
  }
}
</script>